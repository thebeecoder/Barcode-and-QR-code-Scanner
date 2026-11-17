import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, barcode_type='code128', output_path='barcode'):
    try:

        barcode_class = barcode.get_barcode_class(barcode_type)
        barcode_instance = barcode_class(data, writer=ImageWriter())

        filename = barcode_instance.save(output_path)
        print(f"Barcode saved as {filename}")
    except Exception as e:
        print("Error:", e)

data = '234567890123'
barcode_type = 'code128'
output_path = 'barcode'
generate_barcode(data, barcode_type, output_path)
