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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-02-26 22:29:58.020813','0','test',1,'[{\"added\": {}}]',7,1),(2,'2023-02-26 22:39:38.856611','0','test',1,'[{\"added\": {}}]',7,1),(3,'2023-02-26 22:40:12.161526','2','karl',1,'[{\"added\": {}}]',4,1),(4,'2023-02-26 22:40:42.236379','2','karl',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]',4,1),(5,'2023-02-26 22:41:28.514770','0','chicken',1,'[{\"added\": {}}]',7,1),(6,'2023-02-27 02:01:27.452435','0','Spaghetti',1,'[{\"added\": {}}]',7,1),(7,'2023-02-27 02:02:10.422867','0','Linguine',1,'[{\"added\": {}}]',7,1),(8,'2023-02-27 02:02:31.972783','0','Fettucine',1,'[{\"added\": {}}]',7,1),(9,'2023-02-27 02:04:04.543585','0','Chicken and Rice',1,'[{\"added\": {}}]',7,1),(10,'2023-04-04 03:25:01.535178','1','eggs',1,'[{\"added\": {}}]',8,1),(11,'2023-04-04 03:25:17.536579','2','salt',1,'[{\"added\": {}}]',8,1),(12,'2023-04-04 03:25:32.562045','3','pepper',1,'[{\"added\": {}}]',8,1),(13,'2023-04-04 03:25:43.312403','4','peanuts',1,'[{\"added\": {}}]',8,1),(14,'2023-04-04 05:45:53.542383','92887','92887',3,'',9,1),(15,'2023-04-04 05:45:58.765106','2BDCA','2BDCA',3,'',9,1),(16,'2023-04-04 07:52:38.293382','1','peanuts',1,'[{\"added\": {}}]',8,1),(17,'2023-04-04 07:52:50.440989','2','peanut butter',1,'[{\"added\": {}}]',8,1),(18,'2023-04-04 07:53:02.027718','3','chicken',1,'[{\"added\": {}}]',8,1),(19,'2023-04-04 07:53:09.659134','4','chocolate',1,'[{\"added\": {}}]',8,1),(20,'2023-04-04 07:53:35.133265','5','eggs',1,'[{\"added\": {}}]',8,1),(21,'2023-04-04 08:00:34.776745','1','eggs',1,'[{\"added\": {}}]',8,1),(22,'2023-04-04 08:00:41.797611','2','peanuts',1,'[{\"added\": {}}]',8,1),(23,'2023-04-04 08:00:52.072677','3','peanut butter',1,'[{\"added\": {}}]',8,1),(24,'2023-04-04 08:01:01.763305','4','onion',1,'[{\"added\": {}}]',8,1),(25,'2023-04-04 08:01:15.522550','5','milk',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-01 23:12:56
