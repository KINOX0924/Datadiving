-- MySQL dump 10.13  Distrib 8.4.5, for Win64 (x86_64)
--
-- Host: localhost    Database: bank_database
-- ------------------------------------------------------
-- Server version	8.4.5

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cp_rank`
--

DROP TABLE IF EXISTS `cp_rank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cp_rank` (
  `rank_id` char(5) NOT NULL,
  `rank_title` varchar(6) NOT NULL,
  PRIMARY KEY (`rank_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cp_rank`
--

LOCK TABLES `cp_rank` WRITE;
/*!40000 ALTER TABLE `cp_rank` DISABLE KEYS */;
INSERT INTO `cp_rank` VALUES ('C01','아르바이트');
/*!40000 ALTER TABLE `cp_rank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `dept_number` int NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(10) NOT NULL,
  `region_number` int DEFAULT NULL,
  PRIMARY KEY (`dept_number`),
  KEY `fk_department_region_number` (`region_number`),
  CONSTRAINT `fk_department_region_number` FOREIGN KEY (`region_number`) REFERENCES `region` (`region_number`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_number` bigint NOT NULL AUTO_INCREMENT,
  `employee_id` varchar(20) NOT NULL,
  `employee_password` varchar(300) NOT NULL,
  `email_address` varchar(40) NOT NULL,
  `employee_name` varchar(10) NOT NULL,
  `resident_number` char(15) NOT NULL,
  `rank_id` char(5) NOT NULL,
  `role` varchar(20) DEFAULT NULL,
  `dept_number` int DEFAULT NULL,
  `region_number` int DEFAULT NULL,
  `salary` int NOT NULL,
  `phone_number` char(15) NOT NULL,
  `address` varchar(50) NOT NULL,
  `hire_date` datetime NOT NULL,
  PRIMARY KEY (`employee_number`),
  KEY `fk_employees_rank_id` (`rank_id`),
  KEY `fk_employees_dept_number` (`dept_number`),
  KEY `fk_employees_region_number` (`region_number`),
  CONSTRAINT `fk_employees_dept_number` FOREIGN KEY (`dept_number`) REFERENCES `department` (`dept_number`) ON UPDATE CASCADE,
  CONSTRAINT `fk_employees_rank_id` FOREIGN KEY (`rank_id`) REFERENCES `cp_rank` (`rank_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_employees_region_number` FOREIGN KEY (`region_number`) REFERENCES `region` (`region_number`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `region` (
  `region_number` int NOT NULL AUTO_INCREMENT,
  `region_name` varchar(20) NOT NULL,
  PRIMARY KEY (`region_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-28 21:54:45
