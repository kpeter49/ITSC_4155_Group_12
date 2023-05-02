-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: recipeapp
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$FCMpxXgGwlnypLmM3xKnzu$2ElTBNMRJGyHfZQpBHIwGOF+d7oy9Xn8O6vyIWJe8jM=','2023-04-04 08:01:47.382955',1,'kpeter49','','','',1,1,'2023-02-26 22:26:10.627864'),(2,'pbkdf2_sha256$390000$EX1mUhTBuUrZEtXxYb4NCx$0OaCT01UM13B7vj43o9AXJBDUVIBPvsMdGRD5tUoC5k=','2023-02-26 23:40:23.872853',0,'karl','Karl','Peterson','karl.r.peterson4@gmail.com',0,1,'2023-02-26 22:40:11.000000'),(3,'pbkdf2_sha256$390000$5CeY7rDFb6dBrtdqaURDyS$DziYlEt8oYbyFtBasW3nYwT7Ku6RCV4Ny66cu6bBvgY=','2023-05-02 01:29:01.878345',0,'test1','','','',0,1,'2023-04-04 00:03:13.182702'),(4,'pbkdf2_sha256$390000$kRDsmAHK0VKPKSF0rvdCsJ$yONolh9fAqy1NlAaoB2b38MonU4iKpvDZM89xT1a7Zw=','2023-04-04 05:36:44.381407',0,'test2','','','',0,1,'2023-04-04 05:36:25.213432'),(5,'pbkdf2_sha256$390000$Jw0YCbzdEpmyGFxcCwStpu$oeDsOOmcov6tvMWRqDdo0iuI2Vdy+pwWxyHN9gB9SSs=','2023-04-04 13:36:58.102536',0,'test3','','','',0,1,'2023-04-04 05:41:17.604239'),(6,'pbkdf2_sha256$390000$Ov6Gc3lZFtO104Sx1Rquzj$lZTvMxmPugF5xKVRcvIWChc8v18WErY3Yunl3+gzad0=','2023-04-04 05:50:03.904559',0,'test5','','','',0,1,'2023-04-04 05:48:38.045314'),(7,'pbkdf2_sha256$390000$9AuEtromqUMLUF3DN9lx8J$6LqM9J4JVWY5itSUhI1mKClYUXzHtDiQNOTpP7jFkTw=','2023-04-04 08:07:25.582348',0,'test7','','','',0,1,'2023-04-04 08:06:01.422242');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-01 23:12:57
