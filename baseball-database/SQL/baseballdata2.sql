-- MySQL dump 10.13  Distrib 8.0.44, for macos15 (arm64)
--
-- Host: localhost    Database: baseball
-- ------------------------------------------------------
-- Server version	9.5.0

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '19829fa8-bb5f-11f0-ac8c-8345cd35a188:1-303';

--
-- Table structure for table `ballpark`
--

DROP TABLE IF EXISTS `ballpark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ballpark` (
  `ballparkID` int NOT NULL AUTO_INCREMENT,
  `ballparkName` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ballparkID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ballpark`
--

LOCK TABLES `ballpark` WRITE;
/*!40000 ALTER TABLE `ballpark` DISABLE KEYS */;
INSERT INTO `ballpark` VALUES (1,'Truist Park','Atlanta'),(2,'Dodger Stadium','Los Angeles'),(3,'Yankee Stadium','New York'),(4,'Fenway Park','Boston'),(5,'T-Mobile Park','Seattle'),(6,'Minute Maid Park','Houston'),(7,'Wrigley Field','Chicago'),(8,'Citi Field','New York'),(9,'Petco Park','San Diego'),(10,'Oracle Park','San Francisco'),(11,'Busch Stadium','St. Louis'),(12,'Chase Field','Phoenix'),(13,'Coors Field','Denver'),(14,'Progressive Field','Cleveland'),(15,'PNC Park','Pittsburgh');
/*!40000 ALTER TABLE `ballpark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coach`
--

DROP TABLE IF EXISTS `coach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coach` (
  `coachID` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `teamID` int DEFAULT NULL,
  PRIMARY KEY (`coachID`),
  KEY `fk_coach_team_idx` (`teamID`),
  CONSTRAINT `fk_coach_team` FOREIGN KEY (`teamID`) REFERENCES `team` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coach`
--

LOCK TABLES `coach` WRITE;
/*!40000 ALTER TABLE `coach` DISABLE KEYS */;
INSERT INTO `coach` VALUES (1,'Brian','Snitker',1),(2,'Walt','Weiss',1),(3,'Dave','Roberts',2),(4,'Clayton','McCullough',2),(5,'Aaron','Boone',3),(6,'Carlos','Mendoza',3),(7,'Alex','Cora',4),(8,'Ramón','Vázquez',4),(9,'Scott','Servais',5),(10,'Kristopher','Negron',5),(11,'Dusty','Baker',6),(12,'Joe','Espada',6),(13,'David','Ross',7),(14,'Andy','Green',7),(15,'Buck','Showalter',8),(16,'Eric','Chávez',8),(17,'Bob','Melvin',9),(18,'Ryan','Christenson',9),(19,'Gabe','Kapler',10),(20,'Ron','Wotus',10),(21,'Oliver','Marmol',11),(22,'Skip','Schumaker',11),(23,'Torey','Lovullo',12),(24,'Robbie','Hammock',12),(25,'Bud','Black',13),(26,'Mike','Redmond',13),(27,'Terry','Francona',14),(28,'DeMarlo','Hale',14),(29,'Derek','Shelton',15),(30,'Don','Kelly',15);
/*!40000 ALTER TABLE `coach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `concessionSale`
--

DROP TABLE IF EXISTS `concessionSale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `concessionSale` (
  `concessionSaleID` int NOT NULL AUTO_INCREMENT,
  `gameID` int DEFAULT NULL,
  `itemName` varchar(100) DEFAULT NULL,
  `quantitySold` int DEFAULT NULL,
  `pricePerItem` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`concessionSaleID`),
  KEY `idx_concessionSale_game` (`gameID`),
  CONSTRAINT `fk_concessionSale_game` FOREIGN KEY (`gameID`) REFERENCES `game` (`gameID`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concessionSale`
--

LOCK TABLES `concessionSale` WRITE;
/*!40000 ALTER TABLE `concessionSale` DISABLE KEYS */;
INSERT INTO `concessionSale` VALUES (1,1,'Hot Dog',1200,6.50),(2,1,'Soda',2000,5.00),(3,2,'Nachos',900,7.50),(4,2,'Beer',2500,9.00),(5,3,'Hot Dog',1100,6.50),(6,3,'Beer',2400,9.00),(7,4,'Nachos',850,7.25),(8,4,'Soda',1800,5.00),(9,5,'Pretzel',600,6.00),(10,5,'Beer',2600,9.50),(11,6,'Hot Dog',1000,6.50),(12,6,'Water',1500,4.00),(13,7,'Burger',700,8.50),(14,7,'Soda',1900,5.00),(15,8,'Popcorn',650,5.50),(16,8,'Beer',2200,9.25),(17,9,'Hot Dog',1300,6.75),(18,9,'Soda',2100,5.00),(19,10,'Nachos',900,7.50),(20,10,'Beer',2500,9.00),(21,20,'Water',1600,4.00),(22,20,'Hot Dog',1200,6.50),(23,30,'Pretzel',700,6.00),(24,30,'Beer',2300,9.25),(25,40,'Popcorn',720,5.50),(26,40,'Soda',2000,5.00),(27,50,'Burger',800,8.50),(28,50,'Beer',2600,9.50),(29,60,'Hot Dog',1400,6.75),(30,60,'Soda',2100,5.00),(31,70,'Nachos',1000,7.75),(32,70,'Beer',2400,9.25),(33,80,'Pretzel',650,6.00),(34,80,'Soda',1800,5.00),(35,90,'Hot Dog',1150,6.50),(36,90,'Beer',2150,9.00),(37,100,'Burger',900,8.75),(38,100,'Water',1700,4.00);
/*!40000 ALTER TABLE `concessionSale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `gameID` int NOT NULL AUTO_INCREMENT,
  `gameDate` datetime DEFAULT NULL,
  `homeTeamID` int DEFAULT NULL,
  `awayTeamID` int DEFAULT NULL,
  `homeTeamScore` int DEFAULT NULL,
  `awayTeamScore` int DEFAULT NULL,
  `ballparkID` int DEFAULT NULL,
  `seasonID` int DEFAULT NULL,
  PRIMARY KEY (`gameID`),
  KEY `fk_game_homeTeam_idx` (`homeTeamID`),
  KEY `fk_game_awayTeam_idx` (`awayTeamID`),
  KEY `fk_game_ballpark_idx` (`ballparkID`),
  KEY `fk_game_season_idx` (`seasonID`),
  CONSTRAINT `fk_game_awayTeam` FOREIGN KEY (`awayTeamID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `fk_game_ballpark` FOREIGN KEY (`ballparkID`) REFERENCES `ballpark` (`ballparkID`),
  CONSTRAINT `fk_game_homeTeam` FOREIGN KEY (`homeTeamID`) REFERENCES `team` (`teamID`),
  CONSTRAINT `fk_game_season` FOREIGN KEY (`seasonID`) REFERENCES `season` (`seasonID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
INSERT INTO `game` VALUES (1,'2023-04-01 00:00:00',1,2,5,3,1,1),(2,'2023-04-03 00:00:00',1,3,4,6,1,1),(3,'2023-04-05 00:00:00',2,1,7,4,2,1),(4,'2023-04-07 00:00:00',2,5,3,2,2,1),(5,'2023-04-08 00:00:00',3,4,6,1,3,1),(6,'2023-04-10 00:00:00',3,6,4,3,3,1),(7,'2023-04-12 00:00:00',4,3,2,5,4,1),(8,'2023-04-14 00:00:00',4,5,8,4,4,1),(9,'2023-04-15 00:00:00',5,6,3,7,5,1),(10,'2023-04-17 00:00:00',5,1,5,2,5,1),(11,'2023-04-19 00:00:00',6,7,6,3,6,1),(12,'2023-04-20 00:00:00',6,8,4,5,6,1),(13,'2023-04-22 00:00:00',7,2,2,1,7,1),(14,'2023-04-24 00:00:00',7,9,5,6,7,1),(15,'2023-04-25 00:00:00',8,10,7,3,8,1),(16,'2023-04-27 00:00:00',8,3,6,4,8,1),(17,'2023-04-28 00:00:00',9,11,3,2,9,1),(18,'2023-04-30 00:00:00',9,12,4,5,9,1),(19,'2023-05-01 00:00:00',10,13,2,3,10,1),(20,'2023-05-03 00:00:00',10,14,9,7,10,1),(21,'2023-05-04 00:00:00',11,15,5,4,11,1),(22,'2023-05-06 00:00:00',11,12,3,1,11,1),(23,'2023-05-08 00:00:00',12,7,4,3,12,1),(24,'2023-05-10 00:00:00',12,6,7,5,12,1),(25,'2023-05-11 00:00:00',13,10,8,6,13,1),(26,'2023-05-13 00:00:00',13,1,3,2,13,1),(27,'2023-05-14 00:00:00',14,4,6,4,14,1),(28,'2023-05-16 00:00:00',14,3,2,7,14,1),(29,'2023-05-17 00:00:00',15,5,5,3,15,1),(30,'2023-05-19 00:00:00',15,2,4,2,15,1),(31,'2023-05-20 00:00:00',1,7,7,6,1,1),(32,'2023-05-22 00:00:00',1,8,8,5,1,1),(33,'2023-05-23 00:00:00',2,9,3,4,2,1),(34,'2023-05-25 00:00:00',2,10,6,3,2,1),(35,'2023-05-27 00:00:00',3,11,5,7,3,1),(36,'2023-05-29 00:00:00',3,12,4,1,3,1),(37,'2023-05-30 00:00:00',4,13,9,5,4,1),(38,'2023-06-01 00:00:00',4,14,3,2,4,1),(39,'2023-06-02 00:00:00',5,15,6,7,5,1),(40,'2023-06-04 00:00:00',5,8,8,4,5,1),(41,'2023-06-05 00:00:00',6,3,2,1,6,1),(42,'2023-06-07 00:00:00',6,1,7,5,6,1),(43,'2023-06-08 00:00:00',7,12,3,6,7,1),(44,'2023-06-10 00:00:00',7,13,4,2,7,1),(45,'2023-06-11 00:00:00',8,5,5,3,8,1),(46,'2023-06-13 00:00:00',8,15,7,4,8,1),(47,'2023-06-14 00:00:00',9,3,6,2,9,1),(48,'2023-06-16 00:00:00',9,6,3,2,9,1),(49,'2023-06-17 00:00:00',10,2,8,6,10,1),(50,'2023-06-19 00:00:00',10,1,4,3,10,1),(51,'2024-04-01 00:00:00',1,4,6,3,1,2),(52,'2024-04-03 00:00:00',1,6,5,4,1,2),(53,'2024-04-05 00:00:00',2,3,3,2,2,2),(54,'2024-04-07 00:00:00',2,11,7,5,2,2),(55,'2024-04-09 00:00:00',3,7,4,6,3,2),(56,'2024-04-11 00:00:00',3,1,2,1,3,2),(57,'2024-04-12 00:00:00',4,2,5,3,4,2),(58,'2024-04-14 00:00:00',4,3,6,4,4,2),(59,'2024-04-15 00:00:00',5,9,8,7,5,2),(60,'2024-04-17 00:00:00',5,10,3,5,5,2),(61,'2024-04-18 00:00:00',6,4,4,2,6,2),(62,'2024-04-20 00:00:00',6,2,7,6,6,2),(63,'2024-04-22 00:00:00',7,1,6,5,7,2),(64,'2024-04-23 00:00:00',7,5,2,3,7,2),(65,'2024-04-25 00:00:00',8,6,4,1,8,2),(66,'2024-04-27 00:00:00',8,7,5,2,8,2),(67,'2024-04-28 00:00:00',9,14,3,4,9,2),(68,'2024-04-30 00:00:00',9,3,8,6,9,2),(69,'2024-05-01 00:00:00',10,11,6,3,10,2),(70,'2024-05-03 00:00:00',10,12,7,5,10,2),(71,'2024-05-04 00:00:00',11,9,5,3,11,2),(72,'2024-05-06 00:00:00',11,1,4,2,11,2),(73,'2024-05-07 00:00:00',12,3,6,4,12,2),(74,'2024-05-09 00:00:00',12,4,7,6,12,2),(75,'2024-05-10 00:00:00',13,7,2,1,13,2),(76,'2024-05-12 00:00:00',13,5,4,3,13,2),(77,'2024-05-13 00:00:00',14,8,6,5,14,2),(78,'2024-05-15 00:00:00',14,2,3,2,14,2),(79,'2024-05-17 00:00:00',15,6,7,4,15,2),(80,'2024-05-19 00:00:00',15,10,5,3,15,2),(81,'2024-05-20 00:00:00',1,12,8,6,1,2),(82,'2024-05-22 00:00:00',1,9,3,5,1,2),(83,'2024-05-23 00:00:00',2,14,7,2,2,2),(84,'2024-05-25 00:00:00',2,15,6,4,2,2),(85,'2024-05-27 00:00:00',3,5,2,1,3,2),(86,'2024-05-29 00:00:00',3,10,5,7,3,2),(87,'2024-05-30 00:00:00',4,6,4,3,4,2),(88,'2024-06-01 00:00:00',4,7,3,2,4,2),(89,'2024-06-02 00:00:00',5,11,7,6,5,2),(90,'2024-06-04 00:00:00',5,12,8,4,5,2),(91,'2024-06-05 00:00:00',6,9,6,2,6,2),(92,'2024-06-07 00:00:00',6,15,3,4,6,2),(93,'2024-06-08 00:00:00',7,11,5,3,7,2),(94,'2024-06-10 00:00:00',7,14,6,5,7,2),(95,'2024-06-11 00:00:00',8,10,4,2,8,2),(96,'2024-06-13 00:00:00',8,13,7,6,8,2),(97,'2024-06-14 00:00:00',9,1,8,5,9,2),(98,'2024-06-16 00:00:00',9,5,3,1,9,2),(99,'2024-06-17 00:00:00',10,4,4,2,10,2),(100,'2024-06-19 00:00:00',10,6,6,3,10,2);
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gameUmpire`
--

DROP TABLE IF EXISTS `gameUmpire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gameUmpire` (
  `gameUmpireID` int NOT NULL AUTO_INCREMENT,
  `gameID` int DEFAULT NULL,
  `umpireID` int DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`gameUmpireID`),
  KEY `fk_gameUmpire_game_idx` (`gameID`),
  KEY `fk_gameUmpire_umpire_idx` (`umpireID`),
  CONSTRAINT `fk_gameUmpire_game` FOREIGN KEY (`gameID`) REFERENCES `game` (`gameID`),
  CONSTRAINT `fk_gameUmpire_umpire` FOREIGN KEY (`umpireID`) REFERENCES `umpire` (`umpireID`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gameUmpire`
--

LOCK TABLES `gameUmpire` WRITE;
/*!40000 ALTER TABLE `gameUmpire` DISABLE KEYS */;
INSERT INTO `gameUmpire` VALUES (1,1,1,'Home'),(2,1,2,'1B'),(3,1,3,'2B'),(4,2,4,'Home'),(5,2,5,'1B'),(6,2,6,'2B'),(7,3,7,'Home'),(8,3,8,'1B'),(9,3,9,'2B'),(10,4,10,'Home'),(11,4,11,'1B'),(12,4,12,'2B'),(13,5,13,'Home'),(14,5,14,'1B'),(15,5,15,'2B'),(16,6,16,'Home'),(17,6,17,'1B'),(18,6,18,'2B'),(19,7,19,'Home'),(20,7,20,'1B'),(21,7,1,'2B'),(298,100,18,'Home'),(299,100,19,'1B'),(300,100,20,'2B');
/*!40000 ALTER TABLE `gameUmpire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `injury`
--

DROP TABLE IF EXISTS `injury`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `injury` (
  `injuryID` int NOT NULL AUTO_INCREMENT,
  `playerID` int DEFAULT NULL,
  `injuryDescription` varchar(100) DEFAULT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  PRIMARY KEY (`injuryID`),
  KEY `idx_injury_player` (`playerID`),
  CONSTRAINT `fk_injury_player` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `injury`
--

LOCK TABLES `injury` WRITE;
/*!40000 ALTER TABLE `injury` DISABLE KEYS */;
INSERT INTO `injury` VALUES (1,11,'Hamstring strain','2023-05-14','2023-05-23'),(2,27,'Wrist sprain','2023-06-02','2023-06-10'),(3,2,'Back tightness','2023-07-18','2023-07-22'),(4,6,'Knee soreness','2024-04-12','2024-04-18'),(5,21,'Shoulder fatigue','2024-05-30','2024-06-07'),(6,33,'Sprained ankle','2023-08-10','2023-08-17'),(7,17,'Oblique strain','2023-04-20','2023-05-02'),(8,4,'Hand contusion','2024-06-14','2024-06-21'),(9,12,'Calf strain','2024-07-03','2024-07-13'),(10,28,'Quad tightness','2024-06-25','2024-07-01'),(11,37,'Elbow inflammation','2023-09-03','2023-09-14'),(12,5,'Knee bruise','2023-06-10','2023-06-14'),(13,15,'Neck stiffness','2023-05-04','2023-05-06'),(14,22,'Groin tightness','2023-08-25','2023-09-03'),(15,29,'Shoulder strain','2024-05-11','2024-05-21'),(16,34,'Hamstring pull','2024-04-30','2024-05-08'),(17,30,'Hip irritation','2024-07-20','2024-07-25'),(18,23,'Toe fracture','2023-09-12','2023-09-30'),(19,25,'Wrist contusion','2023-06-14','2023-06-20'),(20,13,'Back tightness','2023-07-02','2023-07-07');
/*!40000 ALTER TABLE `injury` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `playerID` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `teamID` int DEFAULT NULL,
  PRIMARY KEY (`playerID`),
  KEY `fk_player_team_idx` (`teamID`),
  CONSTRAINT `fk_player_team` FOREIGN KEY (`teamID`) REFERENCES `team` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES (1,'Ronald','Acuña','RF',1),(2,'Matt','Olson','1B',1),(3,'Ozzie','Albies','2B',1),(4,'Austin','Riley','3B',1),(5,'Michael','Harris','CF',1),(6,'Mookie','Betts','RF',2),(7,'Freddie','Freeman','1B',2),(8,'Will','Smith','C',2),(9,'Max','Muncy','3B',2),(10,'J.D.','Martinez','DH',2),(11,'Aaron','Judge','RF',3),(12,'Giancarlo','Stanton','LF',3),(13,'Gleyber','Torres','2B',3),(14,'Anthony','Rizzo','1B',3),(15,'Harrison','Bader','CF',3),(16,'Rafael','Devers','3B',4),(17,'Masataka','Yoshida','LF',4),(18,'Justin','Turner','DH',4),(19,'Trevor','Story','SS',4),(20,'Alex','Verdugo','RF',4),(21,'Julio','Rodríguez','CF',5),(22,'Ty','France','1B',5),(23,'Eugenio','Suarez','3B',5),(24,'J.P.','Crawford','SS',5),(25,'Teoscar','Hernandez','RF',5),(26,'Jose','Altuve','2B',6),(27,'Yordan','Alvarez','LF',6),(28,'Kyle','Tucker','RF',6),(29,'Alex','Bregman','3B',6),(30,'Jeremy','Pena','SS',6),(31,'Nico','Hoerner','2B',7),(32,'Ian','Happ','LF',7),(33,'Seiya','Suzuki','RF',7),(34,'Dansby','Swanson','SS',7),(35,'Cody','Bellinger','CF',7),(36,'Pete','Alonso','1B',8),(37,'Francisco','Lindor','SS',8),(38,'Jeff','McNeil','2B',8),(39,'Brandon','Nimmo','CF',8),(40,'Starling','Marte','RF',8),(41,'Xander','Bogaerts','SS',9),(42,'Juan','Soto','LF',9),(43,'Manny','Machado','3B',9),(44,'Fernando','Tatis','RF',9),(45,'Jake','Cronenworth','2B',9),(46,'Logan','Webb','P',10),(47,'LaMonte','Wade','1B',10),(48,'Mike','Yastrzemski','RF',10),(49,'Thairo','Estrada','2B',10),(50,'Joc','Pederson','DH',10),(51,'Paul','Goldschmidt','1B',11),(52,'Nolan','Arenado','3B',11),(53,'Tommy','Edman','SS',11),(54,'Lars','Nootbaar','RF',11),(55,'Willson','Contreras','C',11),(56,'Corbin','Carroll','CF',12),(57,'Ketel','Marte','2B',12),(58,'Christian','Walker','1B',12),(59,'Alek','Thomas','CF',12),(60,'Gabriel','Moreno','C',12),(61,'Kris','Bryant','RF',13),(62,'Ryan','McMahon','3B',13),(63,'Elias','Diaz','C',13),(64,'Charlie','Blackmon','DH',13),(65,'Brenton','Doyle','CF',13),(66,'Jose','Ramirez','3B',14),(67,'Steven','Kwan','LF',14),(68,'Andres','Gimenez','2B',14),(69,'Josh','Naylor','1B',14),(70,'Bo','Naylor','C',14),(71,'Bryan','Reynolds','LF',15),(72,'KeBryan','Hayes','3B',15),(73,'Jack','Suwinski','RF',15),(74,'Henry','Davis','C',15),(75,'Connor','Joe','1B',15),(76,'Eddie','Rosario','LF',1),(77,'Sean','Murphy','C',1),(78,'Sam','Hilliard','CF',1),(79,'Orlando','Arcia','SS',1),(80,'Marcell','Ozuna','DH',1),(81,'Chris','Taylor','LF',2),(82,'Jason','Heyward','RF',2),(83,'Gavin','Lux','SS',2),(84,'Miguel','Vargas','2B',2),(85,'David','Peralta','LF',2),(86,'DJ','LeMahieu','2B',3),(87,'Jose','Trevino','C',3),(88,'Oswald','Peraza','SS',3),(89,'Oswaldo','Cabrera','LF',3),(90,'Anthony','Volpe','SS',3),(91,'Adam','Duvall','RF',4),(92,'Reese','McGuire','C',4),(93,'Enmanuel','Valdez','2B',4),(94,'Kike','Hernandez','SS',4),(95,'Jarren','Duran','CF',4),(96,'Cal','Raleigh','C',5),(97,'Jarred','Kelenic','LF',5),(98,'A.J.','Pollock','LF',5),(99,'Dylan','Moore','SS',5),(100,'Kolten','Wong','2B',5),(101,'Martin','Maldonado','C',6),(102,'Chas','McCormick','CF',6),(103,'Jose','Abreu','1B',6),(104,'Mauricio','Dubon','2B',6),(105,'Corey','Julks','LF',6),(106,'Christopher','Morel','DH',7),(107,'Patrick','Wisdom','3B',7),(108,'Nick','Madrigal','2B',7),(109,'Mike','Tauchman','CF',7),(110,'Yan','Gomes','C',7),(111,'Mark','Canha','LF',8),(112,'Daniel','Vogelbach','DH',8),(113,'Luis','Guillorme','SS',8),(114,'Omar','Narvaez','C',8),(115,'Tommy','Pham','LF',8),(116,'Trent','Grisham','CF',9),(117,'Ha-Seong','Kim','SS',9),(118,'Matt','Batton','2B',9),(119,'Gary','Sanchez','C',9),(120,'Luis','Campusano','C',9),(121,'Blake','Sabol','C',10),(122,'David','Villar','3B',10),(123,'Michael','Conforto','RF',10),(124,'Mitch','Haniger','RF',10),(125,'Austin','Slater','LF',10),(126,'Jordan','Walker','RF',11),(127,'Dylan','Carlson','CF',11),(128,'Nolan','Gorman','2B',11),(129,'Andrew','Knizner','C',11),(130,'Brendan','Donovan','LF',11),(131,'Evan','Longoria','3B',12),(132,'Dominic','Cancone','LF',12),(133,'Jake','McCarthy','RF',12),(134,'Pavin','Smith','1B',12),(135,'Blaze','Alexander','SS',12),(136,'Harold','Castro','2B',13),(137,'Ezequiel','Tovar','SS',13),(138,'Jurickson','Profar','LF',13),(139,'Alan','Trejo','2B',13),(140,'Yonathan','Daza','CF',13),(141,'Myles','Straw','CF',14),(142,'Gabriel','Arias','SS',14),(143,'Will','Brennan','RF',14),(144,'Tyler','Freeman','2B',14),(145,'Cam','Gallagher','C',14),(146,'Ji-Man','Choi','1B',15),(147,'Austin','Hedges','C',15),(148,'Liover','Peguero','SS',15),(149,'Rodolfo','Castro','2B',15),(150,'Mark','Mathias','3B',15),(151,'Shogo','Akiyama','CF',7),(152,'Jonathan','India','2B',7),(153,'Bryce','Elder','P',1),(154,'Spencer','Strider','P',1),(155,'Kyle','Wright','P',1),(156,'Walker','Buehler','P',2),(157,'Julio','Urias','P',2),(158,'Tony','Gonsolin','P',2),(159,'Clayton','Kershaw','P',2),(160,'Dustin','May','P',2),(161,'Gerrit','Cole','P',3),(162,'Nestor','Cortes','P',3),(163,'Luis','Severino','P',3),(164,'Carlos','Rodon','P',3),(165,'Clarke','Schmidt','P',3),(166,'Robbie','Ray','P',5),(167,'Luis','Castillo','P',5),(168,'Logan','Gilbert','P',5),(169,'George','Kirby','P',5),(170,'Marco','Gonzales','P',5),(171,'Framber','Valdez','P',6),(172,'Cristian','Javier','P',6),(173,'Hunter','Brown','P',6),(174,'Jose','Urquidy','P',6),(175,'Lance','McCullers','P',6),(176,'Jordan','Montgomery','P',11),(177,'Miles','Mikolas','P',11),(178,'Jake','Woodford','P',11),(179,'Steven','Matz','P',11),(180,'Matthew','Liberatore','P',11),(181,'Merrill','Kelly','P',12),(182,'Zac','Gallen','P',12),(183,'Tommy','Henry','P',12),(184,'Ryne','Nelson','P',12),(185,'Brandon','Pfaadt','P',12),(186,'Kyle','Freeland','P',13),(187,'German','Marquez','P',13),(188,'Austin','Gomber','P',13),(189,'Ryan','Feltner','P',13),(190,'Connor','Seabold','P',13),(191,'Shane','Bieber','P',14),(192,'Tanner','Bibee','P',14),(193,'Aaron','Civale','P',14),(194,'Logan','Allen','P',14),(195,'Cal','Quantrill','P',14),(196,'Mitch','Keller','P',15),(197,'Roansy','Contreras','P',15),(198,'Luis','Ortiz','P',15),(199,'Johan','Oviedo','P',15),(200,'Rich','Hill','P',15);
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `player_vw`
--

DROP TABLE IF EXISTS `player_vw`;
/*!50001 DROP VIEW IF EXISTS `player_vw`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `player_vw` AS SELECT 
 1 AS `player_id`,
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `position`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `playerGameStats`
--

DROP TABLE IF EXISTS `playerGameStats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playerGameStats` (
  `statID` int NOT NULL AUTO_INCREMENT,
  `gameID` int DEFAULT NULL,
  `playerID` int DEFAULT NULL,
  `atBats` int DEFAULT NULL,
  `hits` int DEFAULT NULL,
  `homeRuns` int DEFAULT NULL,
  `rbis` int DEFAULT NULL,
  PRIMARY KEY (`statID`),
  KEY `idx_playerGameStats_game` (`gameID`),
  KEY `idx_playerGameStats_player` (`playerID`),
  CONSTRAINT `fk_playerGameStats_game` FOREIGN KEY (`gameID`) REFERENCES `game` (`gameID`),
  CONSTRAINT `fk_playerGameStats_player` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playerGameStats`
--

LOCK TABLES `playerGameStats` WRITE;
/*!40000 ALTER TABLE `playerGameStats` DISABLE KEYS */;
INSERT INTO `playerGameStats` VALUES (1,1,1,4,2,1,2),(2,1,2,4,1,0,1),(3,1,6,4,2,0,1),(4,1,7,4,3,1,3),(5,2,3,4,1,0,0),(6,2,4,4,2,1,2),(7,2,11,4,1,0,1),(8,2,12,4,0,0,0),(9,3,6,4,2,0,1),(10,3,7,4,1,0,0),(11,3,1,4,1,0,0),(12,3,5,4,2,1,3),(13,4,6,4,2,1,2),(14,4,9,4,1,0,1),(15,4,21,4,2,0,1),(16,4,23,4,1,0,0),(17,5,11,4,2,1,2),(18,5,14,4,1,0,0),(19,5,16,4,1,0,1),(20,5,18,4,2,0,1),(21,6,11,4,1,0,0),(22,6,12,4,2,1,3),(23,6,26,4,2,0,1),(24,6,27,4,1,0,0),(25,7,16,4,1,0,0),(26,7,17,4,2,0,1),(27,7,11,4,1,0,0),(28,7,14,4,1,0,0),(29,8,16,4,0,0,0),(30,8,17,4,2,1,3),(31,8,21,4,2,0,1),(32,8,25,4,1,0,0),(33,9,21,4,3,1,3),(34,9,22,4,2,0,1),(35,9,27,4,1,0,0),(36,9,28,4,2,1,2),(37,10,21,4,2,0,0),(38,10,5,4,1,0,0),(39,10,31,4,1,0,0),(40,10,33,4,2,1,3),(41,11,26,4,1,0,1),(42,11,28,4,2,1,3),(43,11,31,4,1,0,0),(44,11,32,4,2,0,1),(45,12,26,4,2,1,2),(46,12,30,4,1,0,0),(47,12,36,4,2,0,1),(48,12,39,4,1,0,0),(49,13,31,4,2,1,2),(50,13,32,4,1,0,0),(51,13,6,4,2,1,3),(52,13,7,4,1,0,0),(53,14,31,4,2,0,1),(54,14,33,4,1,0,0),(55,14,43,4,2,1,2),(56,14,44,4,3,1,4),(57,15,36,4,1,0,0),(58,15,37,4,2,1,2),(59,15,46,4,1,0,1),(60,15,47,4,1,0,0),(61,16,8,4,2,1,2),(62,16,9,4,1,0,1),(63,16,21,4,1,0,1),(64,16,23,4,2,1,3),(65,17,42,4,1,0,0),(66,17,43,4,2,1,2),(67,17,9,4,1,0,0),(68,17,14,4,2,0,1),(69,18,56,4,2,0,1),(70,18,58,4,1,0,0),(71,18,22,4,1,0,1),(72,18,24,4,2,1,3),(73,19,10,4,2,0,1),(74,19,11,4,1,0,0),(75,19,12,4,2,1,2),(76,19,13,4,1,0,0),(77,20,14,4,1,0,1),(78,20,16,4,2,0,1),(79,20,17,4,2,1,3),(80,20,18,4,1,0,0),(81,21,51,4,2,1,2),(82,21,52,4,1,0,1),(83,21,53,4,2,0,1),(84,21,54,4,1,0,0),(85,22,55,4,2,0,1),(86,22,56,4,1,0,0),(87,22,57,4,1,0,1),(88,22,58,4,2,1,3),(89,23,61,4,1,0,0),(90,23,62,4,2,0,1),(91,23,63,4,3,0,1),(92,23,64,4,1,0,0),(93,24,65,4,2,1,2),(94,24,66,4,1,0,0),(95,24,67,4,1,0,1),(96,24,68,4,1,0,0),(200,50,12,4,1,0,0),(201,50,21,4,2,1,3),(202,50,31,4,1,0,1),(203,50,46,4,2,0,1),(204,51,1,4,2,1,3),(205,51,2,4,1,0,0),(206,51,3,4,2,0,1),(207,51,4,4,1,0,0),(248,60,21,4,1,0,1),(249,60,22,4,2,1,3),(250,60,23,4,1,0,0),(251,60,24,4,1,0,0),(252,100,10,4,1,0,1),(253,100,11,4,2,1,3),(254,100,12,4,1,0,0),(255,100,13,4,2,0,1);
/*!40000 ALTER TABLE `playerGameStats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `season`
--

DROP TABLE IF EXISTS `season`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `season` (
  `seasonID` int NOT NULL AUTO_INCREMENT,
  `startDate` datetime DEFAULT NULL,
  `endDate` datetime DEFAULT NULL,
  PRIMARY KEY (`seasonID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `season`
--

LOCK TABLES `season` WRITE;
/*!40000 ALTER TABLE `season` DISABLE KEYS */;
INSERT INTO `season` VALUES (1,'2023-03-30 00:00:00','2023-10-01 00:00:00'),(2,'2024-03-28 00:00:00','2024-09-29 00:00:00');
/*!40000 ALTER TABLE `season` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sponsor`
--

DROP TABLE IF EXISTS `sponsor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sponsor` (
  `sponsorID` int NOT NULL AUTO_INCREMENT,
  `sponsorName` varchar(50) DEFAULT NULL,
  `industry` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sponsorID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sponsor`
--

LOCK TABLES `sponsor` WRITE;
/*!40000 ALTER TABLE `sponsor` DISABLE KEYS */;
INSERT INTO `sponsor` VALUES (1,'Nike','Sportswear'),(2,'Gatorade','Beverage'),(3,'Bank of America','Finance'),(4,'State Farm','Insurance'),(5,'Coca-Cola','Beverage'),(6,'Toyota','Automotive'),(7,'Pepsi','Beverage'),(8,'Under Armour','Sportswear'),(9,'Geico','Insurance'),(10,'T-Mobile','Telecom');
/*!40000 ALTER TABLE `sponsor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `teamID` int NOT NULL AUTO_INCREMENT,
  `teamName` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `ballparkID` int DEFAULT NULL,
  `seasonID` int DEFAULT NULL,
  PRIMARY KEY (`teamID`),
  KEY `fk_team_ballpark_idx` (`ballparkID`),
  KEY `fk_team_season_idx` (`seasonID`),
  CONSTRAINT `fk_team_ballpark` FOREIGN KEY (`ballparkID`) REFERENCES `ballpark` (`ballparkID`),
  CONSTRAINT `fk_team_season` FOREIGN KEY (`seasonID`) REFERENCES `season` (`seasonID`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (1,'Atlanta Braves','Atlanta',1,1),(2,'Los Angeles Dodgers','Los Angeles',2,1),(3,'New York Yankees','New York',3,1),(4,'Boston Red Sox','Boston',4,1),(5,'Seattle Mariners','Seattle',5,1),(6,'Houston Astros','Houston',6,1),(7,'Chicago Cubs','Chicago',7,1),(8,'New York Mets','New York',8,1),(9,'San Diego Padres','San Diego',9,1),(10,'San Francisco Giants','San Francisco',10,1),(11,'St. Louis Cardinals','St. Louis',11,1),(12,'Arizona Diamondbacks','Phoenix',12,1),(13,'Colorado Rockies','Denver',13,1),(14,'Cleveland Guardians','Cleveland',14,1),(15,'Pittsburgh Pirates','Pittsburgh',15,1);
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teamSponsor`
--

DROP TABLE IF EXISTS `teamSponsor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teamSponsor` (
  `teamSponsorID` int NOT NULL AUTO_INCREMENT,
  `teamID` int DEFAULT NULL,
  `sponsorID` int DEFAULT NULL,
  `sponsorshipAmount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`teamSponsorID`),
  KEY `fk_teamSponsor_team_idx` (`teamID`),
  KEY `fk_teamSponsor_sponsor_idx` (`sponsorID`),
  CONSTRAINT `fk_teamSponsor_sponsor` FOREIGN KEY (`sponsorID`) REFERENCES `sponsor` (`sponsorID`),
  CONSTRAINT `fk_teamSponsor_team` FOREIGN KEY (`teamID`) REFERENCES `team` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teamSponsor`
--

LOCK TABLES `teamSponsor` WRITE;
/*!40000 ALTER TABLE `teamSponsor` DISABLE KEYS */;
INSERT INTO `teamSponsor` VALUES (1,1,1,500000.00),(2,1,2,250000.00),(3,2,5,600000.00),(4,2,1,300000.00),(5,3,3,450000.00),(6,3,7,200000.00),(7,4,8,350000.00),(8,4,2,150000.00),(9,5,10,300000.00),(10,5,4,120000.00),(11,6,5,520000.00),(12,6,2,200000.00),(13,7,9,280000.00),(14,7,8,150000.00),(15,8,1,500000.00),(16,8,6,180000.00),(17,9,4,250000.00),(18,9,10,190000.00),(19,10,2,210000.00),(20,10,3,130000.00);
/*!40000 ALTER TABLE `teamSponsor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticketSale`
--

DROP TABLE IF EXISTS `ticketSale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticketSale` (
  `ticketSaleID` int NOT NULL AUTO_INCREMENT,
  `gameID` int DEFAULT NULL,
  `ticketType` varchar(45) DEFAULT NULL,
  `ticketsSold` int DEFAULT NULL,
  `pricePerTicket` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`ticketSaleID`),
  KEY `idx_ticketSale_game` (`gameID`),
  CONSTRAINT `fk_ticketSale_game` FOREIGN KEY (`gameID`) REFERENCES `game` (`gameID`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketSale`
--

LOCK TABLES `ticketSale` WRITE;
/*!40000 ALTER TABLE `ticketSale` DISABLE KEYS */;
INSERT INTO `ticketSale` VALUES (1,1,'General',32000,45.00),(2,1,'Premium',4000,120.00),(3,2,'General',28000,40.00),(4,2,'Premium',3500,110.00),(5,3,'General',30000,42.00),(6,3,'Premium',3500,115.00),(7,4,'General',28000,40.00),(8,4,'Premium',3600,118.00),(9,5,'General',31000,48.00),(10,5,'Premium',3900,122.00),(11,6,'General',29500,39.00),(12,6,'Premium',4100,120.00),(13,7,'General',27000,38.00),(14,7,'Premium',3000,105.00),(15,8,'General',25000,35.00),(16,8,'Premium',2800,102.00),(17,9,'General',33000,52.00),(18,9,'Premium',4200,128.00),(19,10,'General',31000,47.00),(20,10,'Premium',4000,125.00),(21,20,'General',29000,44.00),(22,20,'Premium',3800,120.00),(23,30,'General',30500,45.00),(24,30,'Premium',3600,118.00),(25,40,'General',31500,46.00),(26,40,'Premium',3500,117.00),(27,50,'General',29800,41.00),(28,50,'Premium',3100,110.00),(29,60,'General',32000,49.00),(30,60,'Premium',3900,121.00),(31,70,'General',31500,48.00),(32,70,'Premium',3600,118.00),(33,80,'General',30500,45.00),(34,80,'Premium',3300,112.00),(35,90,'General',29900,42.00),(36,90,'Premium',3000,108.00),(37,100,'General',32500,50.00),(38,100,'Premium',4100,130.00);
/*!40000 ALTER TABLE `ticketSale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `umpire`
--

DROP TABLE IF EXISTS `umpire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `umpire` (
  `umpireID` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `yearsExperience` int DEFAULT NULL,
  PRIMARY KEY (`umpireID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `umpire`
--

LOCK TABLES `umpire` WRITE;
/*!40000 ALTER TABLE `umpire` DISABLE KEYS */;
INSERT INTO `umpire` VALUES (1,'Mark','Carlson',15),(2,'Jim','Reynolds',18),(3,'Will','Little',10),(4,'Dan','Iassogna',22),(5,'Chris','Conroy',11),(6,'Jordan','Baker',9),(7,'Alan','Porter',12),(8,'Quinn','Wolcott',8),(9,'Pat','Hoberg',9),(10,'Jeremie','Rehak',6),(11,'Gerry','Davis',24),(12,'Tom','Hallion',28),(13,'Lance','Barksdale',21),(14,'Ed','Hickey',4),(15,'John','Libka',7),(16,'Vic','Carapazza',13),(17,'Ramon','DeJesus',5),(18,'Rob','Drake',20),(19,'Jerry','Layne',30),(20,'Manny','Gonzalez',11);
/*!40000 ALTER TABLE `umpire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `player_vw`
--

/*!50001 DROP VIEW IF EXISTS `player_vw`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `player_vw` (`player_id`,`first_name`,`last_name`,`position`) AS select `player`.`playerID` AS `playerID`,`player`.`firstName` AS `firstName`,`player`.`lastName` AS `lastName`,`player`.`position` AS `position` from `player` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-02  9:45:13
