-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 07, 2022 at 10:54 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clean_blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `Serial` int(50) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `date` datetime(6) DEFAULT current_timestamp(6),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`Serial`, `name`, `phone_num`, `message`, `date`, `email`) VALUES
(1, 'Atkinson', '6457938574', 'First_post', '0000-00-00 00:00:00.000000', 'atkinson@bean.com'),
(2, 'atkinson', '0192837465', 'C\'mon, not this time...', '2022-08-21 10:55:22.611128', 'email@address.com'),
(3, 'Daniel Radcliffe', '6574839201', 'Lumos....', '2022-08-21 11:33:49.159785', 'harry@potter.com'),
(4, 'Abhinav', 'newnum', 'newmsg', '2022-09-04 20:49:27.831360', 'newmail@flask.fl');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `Serial` int(11) NOT NULL,
  `Title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `img_file` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`Serial`, `Title`, `tagline`, `slug`, `content`, `date`, `img_file`) VALUES
(1, 'First_post_title', '123Edited_this shall be my tagline', '123first-post_Edited', 'Excited about my first post123', '2022-09-04 01:37:33', '123.png'),
(2, '123Second_post', 'tagline for second post', 'second-post', 'Content for the send post. Try adding something from the web. Something that amounts to about 80 words in total', '2022-09-04 02:22:53', ''),
(5, 'e le Title', '123456', 'e-le-slug', 'E-le-content', '2022-09-04 11:53:50', 'jutus.png'),
(7, 'box_title', 'Aaj ki tagline', 'tmp-blog', 'Aaj ka content', NULL, 'img.png'),
(8, 'box_title', 'fourth tagline', 'fourth-slug', 'Content', NULL, 'img.png'),
(9, 'Fourth', 'fourth tagline', 'slug', 'Content', NULL, 'img.png'),
(10, 'Fifth', 'tagline', 'first-post_Edited', 'Content', '2022-09-05 01:21:35', 'img.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`Serial`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`Serial`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `Serial` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `Serial` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
