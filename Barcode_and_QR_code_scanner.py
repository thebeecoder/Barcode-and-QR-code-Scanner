import cv2
import numpy as np
from pyzbar import pyzbar
import mysql.connector

def fetch_product_info(barcode_no):
    try:

        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_database"
        )

        cursor = db_connection.cursor()

        query = "SELECT barcode_no, product_name, company_name, price, exp_date, mfg_date FROM products WHERE barcode_no = %s"
        cursor.execute(query, (barcode_no,))
        product_info = cursor.fetchone()

        cursor.close()
        db_connection.close()

        return product_info

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def decode_codes(frame):
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        codes = pyzbar.decode(gray)
        barcodes = []
        for code in codes:
            code_data = code.data.decode('utf-8')
            (x, y, w, h) = code.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
            pts = np.array([code.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
            code_type = code.type
            text = f"{code_type}: {code_data}"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

            barcodes.append((code_type, code_data))

        return frame, barcodes
    except Exception as e:
        print(f"Error decoding codes: {e}")
        return frame, []

def main():
    cap = cv2.VideoCapture(0)
    processed_barcodes = set()

    if not cap.isOpened():
        print("Error: Couldn't open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        frame, barcodes = decode_codes(frame)
        cv2.imshow('Barcode/QR Code Scanner', frame)

        for code_type, barcode_data in barcodes:
            if barcode_data not in processed_barcodes:
                if code_type == 'QRCODE':
                    print(f"QR Code Data: {barcode_data}")
                elif code_type == 'CODE128' or code_type == 'EAN13' or code_type.startswith('CODE'):
                    # print(f"Barcode Data: {barcode_data}")
                    product_info = fetch_product_info(barcode_data)
                    if product_info:
                        print(f"Barcode Number: {product_info[0]}")
                        print(f"Product Name: {product_info[1]}")
                        print(f"Company Name: {product_info[2]}")
                        print(f"Price: {product_info[3]}")
                        print(f"Expiry Date: {product_info[4]}")
                        print(f"Manufacturing Date: {product_info[5]}")
                    else:
                        print("Product not found in the database.")

                processed_barcodes.add(barcode_data)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if _name_ == "_main_":
    main()
