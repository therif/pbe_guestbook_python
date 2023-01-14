-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 14, 2023 at 02:35 PM
-- Server version: 8.0.18
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbe_kel4`
--

-- --------------------------------------------------------

--
-- Table structure for table `gb`
--

CREATE TABLE `gb` (
  `id` int(11) NOT NULL,
  `tgl` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nama` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `hp` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `gender` varchar(2) COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'L',
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gb`
--

INSERT INTO `gb` (`id`, `tgl`, `nama`, `hp`, `email`, `gender`, `status`) VALUES
(1, '2022-12-26 18:42:30', 'anam', '0834242124', 'itts.keren@gmail.com', 'L', 1),
(2, '2022-12-26 18:47:49', 'qwe', '0834242124', 'itts.keren@gmail.com', 'L', 1),
(3, '2022-12-27 18:15:34', 'test24', '0834242124', 'itts.keren@gmail.com', 'L', 1),
(4, '2022-12-28 05:47:15', 'Test ITTS', '0834242124', 'itts.keren@gmail.com', 'L', 1),
(5, '2023-01-10 19:16:33', 'Test ITTS', '0834242124', 'itts.keren@gmail.com', 'L', 1),
(6, '2023-01-14 16:22:24', 'Caya', '1234567', 'asdas@das.sd', 'P', 1),
(7, '2023-01-14 16:27:30', 'tata', '123123', 'asdas', 'P', 1),
(8, '2023-01-14 16:31:57', 'lalala', '034235', 'werwe@sff', 'P', 1),
(9, '2023-01-14 16:35:22', 'asdasd', '342423', 'adasd', 'L', 1),
(10, '2023-01-14 16:52:38', 'dasdas', '32423', 'sdawd@sdas', 'P', 1),
(11, '2023-01-14 16:53:56', 'asdasd', '23423', 'asdsa', 'L', 1),
(12, '2023-01-14 16:54:36', 'asdas', 'asd', 'sada', 'L', 1),
(13, '2023-01-14 16:55:15', 'asdas', '23423', 'asd', 'L', 1),
(14, '2023-01-14 17:00:17', 'asdas', '3242', 'awdwa', 'L', 1),
(15, '2023-01-14 17:00:51', 'asdasd', '23423', 'asd', 'L', 1),
(16, '2023-01-14 17:00:52', '', '', '', 'L', 1),
(17, '2023-01-14 17:01:37', 'dawd', '2231', 'awd', 'L', 1),
(18, '2023-01-14 17:02:29', 'test', '342423', 'asdsdas', 'L', 1);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `username` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gb`
--
ALTER TABLE `gb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gb`
--
ALTER TABLE `gb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
