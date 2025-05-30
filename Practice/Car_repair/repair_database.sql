-- MySQL dump 10.13  Distrib 8.4.5, for Win64 (x86_64)
--
-- Host: localhost    Database: repairdb
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
-- Table structure for table `repair_category`
--

DROP TABLE IF EXISTS `repair_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_type` varchar(10) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_category`
--

LOCK TABLES `repair_category` WRITE;
/*!40000 ALTER TABLE `repair_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `repair_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair_detail`
--

DROP TABLE IF EXISTS `repair_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_detail` (
  `detail_id` bigint NOT NULL AUTO_INCREMENT,
  `history_id` bigint NOT NULL,
  `category_id` int NOT NULL,
  `repair_item_id` bigint DEFAULT NULL,
  `item_quantity` int DEFAULT NULL,
  `item_cost` bigint DEFAULT NULL,
  `total_cost` bigint DEFAULT NULL,
  `detail_meno` longtext,
  PRIMARY KEY (`detail_id`),
  KEY `fk_rd_rh_history_id` (`history_id`),
  KEY `fk_rd_rc_category_id` (`category_id`),
  KEY `fk_rd_vi_repair_item_id` (`repair_item_id`),
  CONSTRAINT `fk_rd_rc_category_id` FOREIGN KEY (`category_id`) REFERENCES `repair_category` (`category_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_rd_rh_history_id` FOREIGN KEY (`history_id`) REFERENCES `repair_history` (`history_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_rd_vi_repair_item_id` FOREIGN KEY (`repair_item_id`) REFERENCES `vehicle_item` (`repair_item_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_detail`
--

LOCK TABLES `repair_detail` WRITE;
/*!40000 ALTER TABLE `repair_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `repair_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair_history`
--

DROP TABLE IF EXISTS `repair_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_history` (
  `history_id` bigint NOT NULL AUTO_INCREMENT,
  `repair_date` datetime DEFAULT NULL,
  `vehicle_number` varchar(10) NOT NULL,
  `repair_mileage` int NOT NULL,
  `brand_id` int NOT NULL,
  `shop_id` bigint NOT NULL,
  `repair_memo` text,
  PRIMARY KEY (`history_id`),
  KEY `fk_rh_vhc_vehicle_number` (`vehicle_number`),
  KEY `fk_rh_rsh_shop_id` (`shop_id`),
  KEY `fk_reh_sb_brand_id` (`brand_id`),
  CONSTRAINT `fk_reh_sb_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `shop_brand` (`brand_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_rh_rsh_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `repair_shop` (`shop_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_rh_vhc_vehicle_number` FOREIGN KEY (`vehicle_number`) REFERENCES `vehicle` (`vehicle_number`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_history`
--

LOCK TABLES `repair_history` WRITE;
/*!40000 ALTER TABLE `repair_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `repair_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair_shop`
--

DROP TABLE IF EXISTS `repair_shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repair_shop` (
  `shop_id` bigint NOT NULL AUTO_INCREMENT,
  `brand_id` int NOT NULL,
  `shop_name` varchar(30) NOT NULL,
  `shop_phone` varchar(15) DEFAULT NULL,
  `boss_name` varchar(10) DEFAULT NULL,
  `type_id` int NOT NULL,
  `grade_id` int NOT NULL,
  `state_id` int NOT NULL,
  PRIMARY KEY (`shop_id`),
  KEY `fk_rh_sb_brand_id` (`brand_id`),
  KEY `fk_rs_st_shop_type_id` (`type_id`),
  KEY `fk_rs_sg_grade_id` (`grade_id`),
  KEY `fk_rs_ss_state_id` (`state_id`),
  CONSTRAINT `fk_rh_sb_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `shop_brand` (`brand_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_rs_sg_grade_id` FOREIGN KEY (`grade_id`) REFERENCES `shop_grade` (`grade_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_rs_ss_state_id` FOREIGN KEY (`state_id`) REFERENCES `shop_state` (`state_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_rs_st_shop_type_id` FOREIGN KEY (`type_id`) REFERENCES `shop_types` (`shop_type_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair_shop`
--

LOCK TABLES `repair_shop` WRITE;
/*!40000 ALTER TABLE `repair_shop` DISABLE KEYS */;
/*!40000 ALTER TABLE `repair_shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_brand`
--

DROP TABLE IF EXISTS `shop_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_brand` (
  `brand_id` int NOT NULL AUTO_INCREMENT,
  `brand_name` varchar(20) NOT NULL,
  `brand_phone` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`brand_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_brand`
--

LOCK TABLES `shop_brand` WRITE;
/*!40000 ALTER TABLE `shop_brand` DISABLE KEYS */;
/*!40000 ALTER TABLE `shop_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_grade`
--

DROP TABLE IF EXISTS `shop_grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_grade` (
  `grade_id` int NOT NULL AUTO_INCREMENT,
  `grade_type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`grade_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_grade`
--

LOCK TABLES `shop_grade` WRITE;
/*!40000 ALTER TABLE `shop_grade` DISABLE KEYS */;
/*!40000 ALTER TABLE `shop_grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_state`
--

DROP TABLE IF EXISTS `shop_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_state` (
  `state_id` int NOT NULL AUTO_INCREMENT,
  `state_type` varchar(20) NOT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_state`
--

LOCK TABLES `shop_state` WRITE;
/*!40000 ALTER TABLE `shop_state` DISABLE KEYS */;
/*!40000 ALTER TABLE `shop_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop_types`
--

DROP TABLE IF EXISTS `shop_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop_types` (
  `shop_type_id` int NOT NULL AUTO_INCREMENT,
  `shop_type` varchar(10) NOT NULL,
  PRIMARY KEY (`shop_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop_types`
--

LOCK TABLES `shop_types` WRITE;
/*!40000 ALTER TABLE `shop_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `shop_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `vehicle_number` varchar(10) NOT NULL,
  `vehicle_mileage` int DEFAULT NULL,
  PRIMARY KEY (`vehicle_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle_item`
--

DROP TABLE IF EXISTS `vehicle_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle_item` (
  `repair_item_id` bigint NOT NULL AUTO_INCREMENT,
  `item_name` varchar(100) NOT NULL,
  `standard_cost` bigint DEFAULT NULL,
  PRIMARY KEY (`repair_item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle_item`
--

LOCK TABLES `vehicle_item` WRITE;
/*!40000 ALTER TABLE `vehicle_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehicle_item` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-30 17:23:50
