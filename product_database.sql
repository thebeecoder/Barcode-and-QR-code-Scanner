-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2024 at 07:38 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `product_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `barcode_no` varchar(20) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `exp_date` date DEFAULT NULL,
  `mfg_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `barcode_no`, `product_name`, `company_name`, `price`, `exp_date`, `mfg_date`) VALUES
(1, '123456789012', 'Garnier Shampoo', 'Garnier', 800.00, '2025-12-31', '2023-01-01'),
(2, '234567890123', 'Bread', 'Dawn', 150.00, '2024-12-30', '2023-04-01'),
(3, '345678901234', 'Head and Shoulders shampoo', 'Head and Shoulders ', 600.00, '2026-10-15', '2023-03-01'),
(4, '456789012345', 'Hair Dye', 'Garnier', 999.00, '2025-09-25', '2023-04-01'),
(5, '567890123456', 'glucometer', 'biolandintl.com', 1200.00, '2024-08-20', '2023-05-01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `barcode_no` (`barcode_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
