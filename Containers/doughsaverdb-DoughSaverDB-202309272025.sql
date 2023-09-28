-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: DoughSaverDB
-- ------------------------------------------------------
-- Server version	11.1.2-MariaDB-1:11.1.2+maria~ubu2204

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
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `UserId` int(11) NOT NULL AUTO_INCREMENT,
  `Password` char(60) NOT NULL,
  `Name` char(25) NOT NULL,
  `Email` char(50) NOT NULL,
  `PrimaryLocation` int(5) NOT NULL,
  `Address` char(75) DEFAULT NULL,
  `CreationDate` datetime NOT NULL,
  `LastLogin` datetime NOT NULL,
  PRIMARY KEY (`UserId`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (1,'password','Test User','testuser@odu.edu',23529,'5115 Hampton Blvd, Norfolk, VA','2023-09-19 21:09:29','2023-09-19 21:09:29'),(2,'notmyrealpassword','Jesse Farkas','jfark001@odu.edu',23529,'5115 Hampton Blvd','2023-09-27 19:56:23','2023-09-27 19:56:23');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GroceryStore`
--

DROP TABLE IF EXISTS `GroceryStore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GroceryStore` (
  `StoreId` int(7) NOT NULL AUTO_INCREMENT,
  `StoreName` char(25) NOT NULL,
  `Address` char(75) NOT NULL,
  PRIMARY KEY (`StoreId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GroceryStore`
--

LOCK TABLES `GroceryStore` WRITE;
/*!40000 ALTER TABLE `GroceryStore` DISABLE KEYS */;
INSERT INTO `GroceryStore` VALUES (3,'Walmart','550 Fake Avenue');
/*!40000 ALTER TABLE `GroceryStore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ingredient`
--

DROP TABLE IF EXISTS `Ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ingredient` (
  `IngredientID` int(7) NOT NULL AUTO_INCREMENT,
  `IngredientName` varchar(150) DEFAULT NULL,
  `Brand` varchar(25) DEFAULT NULL,
  `Quantity` float(6,2) NOT NULL,
  `Unit` varchar(25) NOT NULL,
  `IsPrivate` tinyint(1) NOT NULL,
  `PrivateUID` int(7) DEFAULT NULL,
  PRIMARY KEY (`IngredientID`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ingredient`
--

LOCK TABLES `Ingredient` WRITE;
/*!40000 ALTER TABLE `Ingredient` DISABLE KEYS */;
INSERT INTO `Ingredient` VALUES (1,'Large Eggs','Great Value',60.00,'Count',0,NULL),(2,'Blackberries','',6.00,'Oz',0,NULL),(3,'Green Bell Pepper','',1.00,'Count',0,NULL),(4,'Hickory Smoked Bacon','Great Value',24.00,'Oz',0,NULL),(5,'Orange Juice','Great Value',128.00,'Oz',0,NULL),(6,'Shredded Fiesta Blend Cheese','Great Value',80.00,'Oz',0,NULL),(7,'Unsalted Butter 4 Sticks','Land O Lakes',1.00,'Lb',0,NULL),(8,'Multigrain Bread Thick Sliced','Natures Own',22.00,'Oz',0,NULL),(9,'Dr Pepper 12 Oz 12 Pack','',12.00,'Count',0,NULL),(10,'2 Percent Milk','Great Value',128.00,'Fl Oz',0,NULL),(11,'Great Value Frozen Waffle Cut French Fries 24 Oz','Great Value',24.00,'Oz',0,NULL),(12,'Scoops Tortilla Chips','Tostitos',14.50,'Oz',0,NULL),(13,'Balsamic Vinegar','Pompeian',16.00,'Fl Oz',0,NULL),(14,'Smooth Extra Virgin Olive Oil','Pompeian',16.00,'Fl Oz',0,NULL),(15,'Grill Mates Montreal Steak Seasoning','McCormick',3.40,'Oz',0,NULL),(16,'Russet Potatoes','',5.00,'Lb',0,NULL),(17,'Freshly Grated Parmesan Cheese','BelGioioso',5.00,'Oz',0,NULL),(18,'Raw Honey Inverted Plastic Bottle','Great Value',16.00,'Oz',0,NULL),(19,'Less Sodium Soy Sauce','Great Value',15.00,'Fl Oz',0,NULL),(20,'80/20 Ground Chuck','',1.00,'Lb',0,NULL),(21,'Street Taco Corn Tortillas','Mission',24.00,'Count',0,NULL),(22,'Gluten Free Red Curry Paste','Thai Kitchen',4.00,'Oz',0,NULL),(23,'Medium Restaurant Style Salsa','Fresh Cravings',16.00,'Oz',0,NULL),(24,'Heavy Whipping Cream','Great Value',16.00,'Oz',0,NULL),(25,'Fresh Cilantro','',1.00,'Bunch',0,NULL),(26,'Non-Fat Greek Yogurt, Plain','Chobani',32.00,'Oz',0,NULL),(27,'Gourmet Creamy Havarti Cheese','Castello',8.00,'Oz',0,NULL),(28,'Farm Fresh Large, White, Grade A Eggs','Egglands Best',18.00,'Count',0,NULL),(29,'Liquid Egg Whites','Bob Evans',32.00,'Oz',0,NULL),(30,'Heavy Whipping Cream','Land O Lakes',16.00,'Fl Oz',0,NULL),(31,'Potato Chips Sour Cream & Onion','Ruffles',8.00,'Oz',0,NULL),(32,'Classic Potato Chips','Lays',8.00,'Oz',0,NULL),(33,'Mild Italian Sausage, 5 Links','Johnsonville',19.00,'Oz',0,NULL),(34,'Pork Chorizo Sausage','Cacique',9.00,'Oz',0,NULL),(35,'Premium Pork Regular Sausage Roll','Jimmy Dean',16.00,'Oz',0,NULL),(36,'Frozen Raw Super Colossal Shell-on Tail-on Easy Peel Shrimp(13-15 Count per lb)','Great Value',16.00,'Oz',0,NULL),(37,'Boneless Beef Ribeye Steak','Stampede',1.88,'Lb',0,NULL),(38,'Oven Roasters Red Potatoes & Onions, Frozen','Birds Eye',14.00,'Oz',0,NULL),(39,'Frozen Crispy Breaded Chicken Strips','Perdue',26.00,'Oz',0,NULL),(40,'Plain Original Pre-Sliced Bagels','Thomas',6.00,'Count',0,NULL),(41,'Homemade All Natural Tomato Pizza Sauce','Raos',13.00,'Oz',0,NULL),(42,'Frozen Sliced Peaches','Great Value',16.00,'Oz',0,NULL),(43,'Cream Cheese','Philadelphia',8.00,'Oz',0,NULL),(44,'Almonds, Lightly Salted','Blue Diamond',14.00,'Oz',0,NULL),(45,'Milk Chocolate Candy, Gluten Free, 1.55 oz bar','Hersheys',6.00,'Count',0,NULL),(46,'Frozen Cooked Snow Crab Legs','Sams Choice',1.50,'Lb',0,NULL),(47,'Pike Place Roast, Ground Coffee, Medium Roast','Starbucks',28.00,'Oz',0,NULL),(48,'Sticky Sweet Barbecue Sauce','Stubbs',18.00,'Oz',0,NULL);
/*!40000 ALTER TABLE `Ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `IngredientCollection`
--

DROP TABLE IF EXISTS `IngredientCollection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `IngredientCollection` (
  `UserID` int(11) NOT NULL,
  `IngredientID` int(7) NOT NULL,
  PRIMARY KEY (`UserID`,`IngredientID`),
  UNIQUE KEY `IngredientID` (`IngredientID`),
  CONSTRAINT `IngredientCollection_IngredientID_Ingredient_IngredientID` FOREIGN KEY (`IngredientID`) REFERENCES `Ingredient` (`IngredientID`),
  CONSTRAINT `IngredientCollection_UserID_Customer_UserId` FOREIGN KEY (`UserID`) REFERENCES `Customer` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `IngredientCollection`
--

LOCK TABLES `IngredientCollection` WRITE;
/*!40000 ALTER TABLE `IngredientCollection` DISABLE KEYS */;
/*!40000 ALTER TABLE `IngredientCollection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PriceData`
--

DROP TABLE IF EXISTS `PriceData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PriceData` (
  `StoreID` int(7) NOT NULL,
  `IngredientID` int(7) NOT NULL,
  `Link` varchar(150) NOT NULL,
  `RegularPrice` float(6,2) DEFAULT NULL,
  `CurrentPrice` float(6,2) NOT NULL,
  `UpdateTimestamp` datetime NOT NULL,
  `IsPaused` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`StoreID`,`IngredientID`),
  KEY `PriceData_IngredientID_Ingredient_IngredientID` (`IngredientID`),
  CONSTRAINT `PriceData_IngredientID_Ingredient_IngredientID` FOREIGN KEY (`IngredientID`) REFERENCES `Ingredient` (`IngredientID`),
  CONSTRAINT `PriceData_StoreID_GroceryStore_StoreId` FOREIGN KEY (`StoreID`) REFERENCES `GroceryStore` (`StoreId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PriceData`
--

LOCK TABLES `PriceData` WRITE;
/*!40000 ALTER TABLE `PriceData` DISABLE KEYS */;
INSERT INTO `PriceData` VALUES (3,1,'https://www.walmart.com/ip/Great-Value-Large-White-Eggs-60-Count/193637719',NULL,8.24,'2023-05-08 12:07:18',1),(3,2,'https://www.walmart.com/ip/Fresh-Blackberries-6-oz/47314798',NULL,2.87,'2023-09-27 20:01:36',NULL),(3,3,'https://www.walmart.com/ip/Fresh-Green-Bell-Pepper-Each/44390945',NULL,0.86,'2023-09-27 20:01:40',NULL),(3,4,'https://www.walmart.com/ip/Great-Value-Hickory-Smoked-Bacon-Mega-Pack-24-oz/346866251',NULL,8.87,'2023-09-27 20:01:58',NULL),(3,5,'https://www.walmart.com/ip/Great-Value-100-Orange-Juice-Original-128-fl-oz/721723248',NULL,6.98,'2023-09-27 20:02:16',NULL),(3,6,'https://www.walmart.com/ip/Great-Value-Finely-Shredded-Fiesta-Blend-Cheese-80-oz/41972647',NULL,17.68,'2023-09-27 22:00:14',NULL),(3,7,'https://www.walmart.com/ip/Land-O-Lakes-Unsalted-Butter-4-Butter-Sticks-1-lb-Pack/10291059',NULL,5.27,'2023-09-27 22:00:27',NULL),(3,8,'https://www.walmart.com/ip/Nature-s-Own-Perfectly-Crafted-Multigrain-Bread-Thick-Sliced-Loaf-22-oz/916953541',NULL,3.54,'2023-09-27 22:00:47',NULL),(3,9,'https://www.walmart.com/ip/Dr-Pepper-Soda-12-fl-oz-cans-12-pack/10452492',NULL,6.48,'2023-09-27 22:02:35',NULL),(3,10,'https://www.walmart.com/ip/Great-Value-2-Reduced-Fat-Milk-128-Fl-Oz/10450115',NULL,2.82,'2023-09-27 22:01:05',NULL),(3,11,'https://www.walmart.com/ip/Great-Value-Waffle-Cut-French-Fried-Potatoes-24-oz-Frozen/10534286',NULL,3.42,'2023-09-27 22:01:10',NULL),(3,12,'https://www.walmart.com/ip/Tostitos-Scoops-Tortilla-Chips-Party-Size-14-5-oz-Bag/11027423',NULL,5.48,'2023-09-27 22:01:20',NULL),(3,13,'https://www.walmart.com/ip/Pompeian-Balsamic-Vinegar-16-fl-oz/10320860',NULL,3.84,'2023-09-28 00:00:12',NULL),(3,14,'https://www.walmart.com/ip/Pompeian-Smooth-Extra-Virgin-Olive-Oil-16-fl-oz/176946682',NULL,6.48,'2023-09-27 22:01:29',NULL),(3,15,'https://www.walmart.com/ip/McCormick-Grill-Mates-Montreal-Steak-Seasoning-3-4-oz/10308051',NULL,2.33,'2023-09-28 00:00:30',NULL),(3,16,'https://www.walmart.com/ip/Russet-Potatoes-5-lb-Bag/10447837',NULL,4.27,'2023-09-27 22:01:49',NULL),(3,17,'https://www.walmart.com/ip/BelGioioso-Freshly-Grated-Parmesan-Cheese-5-oz-Cup/187292653',NULL,3.44,'2023-09-28 00:01:30',NULL),(3,18,'https://www.walmart.com/ip/Great-Value-Raw-Honey-16-oz-Inverted-Plastic-Bottle/433628197',NULL,6.34,'2023-09-27 22:01:56',NULL),(3,19,'https://www.walmart.com/ip/Great-Value-Less-Sodium-Soy-Sauce-15-fl-oz/15056122',NULL,1.58,'2023-09-27 22:02:06',NULL),(3,20,'https://www.walmart.com/ip/All-Natural-80-Lean-20-Fat-Ground-Beef-Chuck-Roll-1-lb/15136791',NULL,5.22,'2023-09-28 00:00:46',NULL),(3,21,'https://www.walmart.com/ip/Mission-Street-Taco-Corn-Tortillas-24-Count/47585143',NULL,2.44,'2023-09-27 22:02:20',NULL),(3,22,'https://www.walmart.com/ip/Thai-Kitchen-Gluten-Free-Red-Curry-Paste-4-oz/10801530',NULL,3.98,'2023-09-21 10:00:38',1),(3,23,'https://www.walmart.com/ip/Fresh-Cravings-Medium-Restaurant-Style-Salsa-16-oz/45980581',NULL,3.43,'2023-09-28 00:01:04',NULL),(3,24,'https://www.walmart.com/ip/Great-Value-Heavy-Whipping-Cream-16-Oz/10450339',NULL,2.78,'2023-09-27 20:01:27',NULL),(3,25,'https://www.walmart.com/ip/Fresh-Cilantro-Bunch/160597260',NULL,0.48,'2023-09-28 00:01:40',NULL),(3,26,'https://www.walmart.com/ip/Chobani-Non-Fat-Greek-Yogurt-Plain-32-oz/21291511',NULL,5.58,'2023-09-27 18:00:52',NULL),(3,27,'https://www.walmart.com/ip/Castello-Gourmet-Creamy-Havarti-Cheese-8oz/42393930',NULL,4.47,'2023-09-28 00:01:53',NULL),(3,28,'https://www.walmart.com/ip/Eggland-s-Best-Farm-Fresh-Large-White-Grade-A-Eggs-18-Count/51259531',NULL,4.12,'2023-09-28 00:02:07',NULL),(3,29,'https://www.walmart.com/ip/Bob-Evans-100-Liquid-Egg-Whites-32-oz-Pack-of-1/821371418',NULL,5.27,'2023-09-28 00:02:26',NULL),(3,30,'https://www.walmart.com/ip/Land-O-Lakes-Heavy-Whipping-Cream-16-fl-oz/15556068',NULL,3.56,'2023-09-28 00:01:14',NULL),(3,31,'https://www.walmart.com/ip/Ruffles-Potato-Chips-Sour-Cream-Onion-8-0-Ounce/735598557',NULL,3.88,'2023-09-28 00:02:38',NULL),(3,32,'https://www.walmart.com/ip/Lay-s-Classic-Potato-Chips-8-oz-Bag/33282303',NULL,3.68,'2023-09-28 00:02:44',NULL),(3,33,'https://www.walmart.com/ip/Johnsonville-Mild-Italian-Sausage-5-Links-1-lb-3-oz-Fresh/10316095',NULL,5.44,'2023-09-27 18:00:22',NULL),(3,34,'https://www.walmart.com/ip/Cacique-Pork-Chorizo-Sausage-9-oz-Roll/11027816',NULL,1.64,'2023-09-27 18:00:59',NULL),(3,35,'https://www.walmart.com/ip/Jimmy-Dean-Premium-Pork-Regular-Sausage-Roll-16-oz/10533854',NULL,4.62,'2023-09-27 18:00:28',NULL),(3,36,'https://www.walmart.com/ip/Great-Value-Frozen-Raw-Super-Colossal-Shell-on-Tail-on-Easy-Peel-Shrimp-16-oz-13-15-Count-per-lb/55490173',NULL,7.92,'2023-09-27 18:00:33',NULL),(3,37,'https://www.walmart.com/ip/Stampede-Boneless-Beef-Ribeye-Steak-1-875-lbs/51259034',NULL,13.98,'2023-09-27 18:00:46',NULL),(3,38,'https://www.walmart.com/ip/Birds-Eye-Oven-Roasters-Red-Potatoes-Onions-Frozen-14-oz-Frozen/909404576',NULL,2.97,'2023-09-27 18:01:16',NULL),(3,39,'https://www.walmart.com/ip/Perdue-Frozen-Crispy-Breaded-Chicken-Strips-26-oz/25875852',NULL,8.98,'2023-09-27 18:01:27',NULL),(3,40,'https://www.walmart.com/ip/Thomas-Plain-Original-Pre-Sliced-Bagels-6-Count/10535153',NULL,4.18,'2023-09-27 18:01:34',NULL),(3,41,'https://www.walmart.com/ip/Rao-s-Homemade-All-Natural-Tomatoe-Pizza-Sauce-13-oz-Jar/34266491',NULL,4.78,'2023-09-27 18:01:41',NULL),(3,42,'https://www.walmart.com/ip/Great-Value-Frozen-Sliced-Peaches-16-oz/10543667',NULL,2.68,'2023-09-27 20:00:14',NULL),(3,43,'https://www.walmart.com/ip/Philadelphia-Original-Cream-Cheese-8-oz-Brick/10295545',NULL,2.98,'2023-09-27 20:00:27',NULL),(3,44,'https://www.walmart.com/ip/Blue-Diamond-Almonds-Lightly-Salted-14-oz/45996554',NULL,6.98,'2023-09-27 20:00:37',NULL),(3,45,'https://www.walmart.com/ip/Hershey-s-Milk-Chocolate-Candy-Individually-Wrapped-Gluten-Free-1-55-oz-Bars-6-Ct/10452239',NULL,6.48,'2023-09-27 20:00:44',NULL),(3,46,'https://www.walmart.com/ip/Sam-s-Choice-Frozen-Cooked-Snow-Crab-Legs-1-5-lb/10811111',NULL,19.96,'2023-09-27 20:00:56',NULL),(3,47,'https://www.walmart.com/ip/Starbucks-Pike-Place-Roast-Ground-Coffee-Medium-Roast-28-oz/476466165',NULL,18.98,'2023-09-27 20:01:07',NULL),(3,48,'https://www.walmart.com/ip/Stubb-s-Sticky-Sweet-Barbecue-Sauce-18-oz/38452318',NULL,3.84,'2023-09-27 20:01:21',NULL);
/*!40000 ALTER TABLE `PriceData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PriceHistory`
--

DROP TABLE IF EXISTS `PriceHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PriceHistory` (
  `StoreID` int(7) NOT NULL,
  `IngredientID` int(7) NOT NULL,
  `UpdateTimestamp` datetime NOT NULL,
  `HistoricalPrice` float(6,2) NOT NULL,
  PRIMARY KEY (`StoreID`,`IngredientID`,`UpdateTimestamp`),
  KEY `PriceHistory_IngredientID_Ingredient_IngredientID` (`IngredientID`),
  CONSTRAINT `PriceHistory_IngredientID_Ingredient_IngredientID` FOREIGN KEY (`IngredientID`) REFERENCES `Ingredient` (`IngredientID`),
  CONSTRAINT `PriceHistory_StoreID_GroceryStore_StoreId` FOREIGN KEY (`StoreID`) REFERENCES `GroceryStore` (`StoreId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PriceHistory`
--

LOCK TABLES `PriceHistory` WRITE;
/*!40000 ALTER TABLE `PriceHistory` DISABLE KEYS */;
INSERT INTO `PriceHistory` VALUES (3,1,'2023-05-03 07:50:16',16.10),(3,1,'2023-05-18 07:50:09',8.24),(3,1,'2023-06-01 11:50:06',6.02),(3,1,'2023-06-13 09:50:07',7.66),(3,1,'2023-06-22 07:50:15',8.34),(3,1,'2023-06-22 09:50:09',5.92),(3,1,'2023-06-29 13:50:19',8.34),(3,1,'2023-07-13 07:50:19',8.54),(3,1,'2023-07-19 09:50:20',8.63),(3,1,'2023-08-07 15:50:06',7.47),(3,1,'2023-08-21 09:50:16',7.27),(3,1,'2023-09-04 13:50:18',7.47),(3,1,'2023-09-14 09:50:17',8.38),(3,2,'2023-05-08 12:07:26',2.67),(3,2,'2023-05-23 07:52:25',2.67),(3,2,'2023-07-05 11:51:54',2.17),(3,2,'2023-08-01 13:51:49',2.77),(3,2,'2023-09-20 11:52:05',2.37),(3,2,'2023-09-20 14:01:30',2.37),(3,3,'2023-05-08 13:05:05',0.86),(3,4,'2023-05-08 13:05:20',5.97),(3,4,'2023-08-17 09:50:26',5.97),(3,4,'2023-08-31 05:50:29',7.74),(3,5,'2023-05-08 13:05:37',5.78),(3,5,'2023-06-20 11:50:55',5.78),(3,5,'2023-08-09 13:50:41',6.12),(3,6,'2023-05-08 13:05:54',17.68),(3,7,'2023-05-08 13:06:04',4.98),(3,7,'2023-08-29 07:51:01',4.98),(3,8,'2023-05-07 23:50:50',3.24),(3,8,'2023-05-08 13:06:14',3.24),(3,9,'2023-04-26 10:29:58',6.48),(3,9,'2023-05-08 13:06:26',4.98),(3,9,'2023-09-14 13:51:08',4.98),(3,10,'2023-04-27 11:29:28',3.12),(3,10,'2023-05-03 07:51:53',3.22),(3,10,'2023-05-08 13:06:40',2.81),(3,10,'2023-05-18 07:52:02',2.81),(3,10,'2023-06-01 11:51:59',3.07),(3,10,'2023-06-09 09:51:38',2.66),(3,10,'2023-06-13 09:51:46',3.07),(3,10,'2023-06-29 13:51:54',2.82),(3,10,'2023-07-03 09:51:57',2.76),(3,10,'2023-07-13 07:52:03',2.59),(3,10,'2023-07-20 09:51:19',2.77),(3,10,'2023-08-01 11:51:33',2.72),(3,10,'2023-08-07 15:51:40',2.53),(3,10,'2023-08-14 11:51:59',2.72),(3,10,'2023-08-29 07:51:41',2.66),(3,10,'2023-09-01 11:52:02',2.78),(3,10,'2023-09-04 13:52:08',2.73),(3,11,'2023-05-08 13:06:58',2.82),(3,11,'2023-08-14 11:52:32',2.82),(3,12,'2023-05-08 13:07:15',5.38),(3,12,'2023-08-21 09:52:30',5.38),(3,12,'2023-09-20 16:01:09',5.48),(3,12,'2023-09-21 00:00:51',11.25),(3,13,'2023-05-08 13:07:32',3.84),(3,14,'2023-05-08 13:07:50',6.48),(3,15,'2023-05-08 14:05:14',2.33),(3,15,'2023-05-18 10:50:44',2.33),(3,15,'2023-07-13 06:50:45',1.98),(3,15,'2023-07-13 10:50:22',7.49),(3,15,'2023-07-13 20:50:40',1.98),(3,15,'2023-07-14 20:50:38',7.49),(3,15,'2023-08-16 10:50:56',1.98),(3,16,'2023-05-01 10:51:01',3.77),(3,16,'2023-05-08 14:05:21',4.67),(3,16,'2023-06-01 10:51:13',4.67),(3,16,'2023-09-12 10:50:47',4.97),(3,17,'2023-05-08 10:07:08',3.44),(3,19,'2023-05-08 10:05:42',1.58),(3,20,'2023-05-03 06:51:47',4.98),(3,20,'2023-05-08 10:06:03',5.17),(3,20,'2023-05-16 10:51:39',5.17),(3,20,'2023-06-19 10:51:45',5.34),(3,20,'2023-08-14 12:51:38',5.47),(3,20,'2023-09-12 10:51:26',5.22),(3,20,'2023-09-21 10:00:29',4.97),(3,20,'2023-09-21 10:51:50',4.97),(3,21,'2023-05-08 10:06:17',2.44),(3,22,'2023-05-08 10:06:36',3.98),(3,23,'2023-05-08 10:06:49',3.43),(3,24,'2023-05-08 12:07:08',2.78),(3,25,'2023-05-08 10:07:20',0.48),(3,26,'2023-05-08 10:07:32',5.58),(3,27,'2023-05-08 11:05:08',4.47),(3,28,'2023-05-08 11:05:27',4.93),(3,29,'2023-05-08 11:05:32',5.27),(3,30,'2023-05-08 10:06:56',3.56),(3,31,'2023-05-08 11:05:42',4.38),(3,32,'2023-05-08 11:06:00',2.76),(3,33,'2023-05-08 11:06:19',5.34),(3,34,'2023-05-08 11:06:28',1.64),(3,35,'2023-05-08 11:06:34',4.62),(3,36,'2023-05-08 11:06:48',7.92),(3,37,'2023-05-08 11:07:03',13.98),(3,38,'2023-05-08 11:07:18',2.97),(3,39,'2023-05-08 11:07:24',8.98),(3,40,'2023-05-08 12:05:08',4.18),(3,41,'2023-05-08 12:05:28',4.78),(3,42,'2023-05-08 12:05:35',2.68),(3,43,'2023-05-08 12:05:40',2.98),(3,44,'2023-05-08 12:05:57',6.28),(3,45,'2023-05-08 12:06:12',4.88),(3,46,'2023-05-08 12:06:31',19.96),(3,47,'2023-05-08 12:06:42',18.98),(3,48,'2023-05-08 12:07:00',3.84);
/*!40000 ALTER TABLE `PriceHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recipe`
--

DROP TABLE IF EXISTS `Recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Recipe` (
  `RecipeID` int(7) NOT NULL AUTO_INCREMENT,
  `RecipeName` varchar(50) NOT NULL,
  `IsPrivate` tinyint(1) NOT NULL,
  `PrivateUID` int(7) DEFAULT NULL,
  `IngredientID` int(7) NOT NULL,
  `Quantity` decimal(10,0) NOT NULL,
  `Unit` varchar(25) NOT NULL,
  PRIMARY KEY (`RecipeID`),
  KEY `Recipe_IngredientID_Ingredient_IngredientID` (`IngredientID`),
  CONSTRAINT `Recipe_IngredientID_Ingredient_IngredientID` FOREIGN KEY (`IngredientID`) REFERENCES `Ingredient` (`IngredientID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recipe`
--

LOCK TABLES `Recipe` WRITE;
/*!40000 ALTER TABLE `Recipe` DISABLE KEYS */;
/*!40000 ALTER TABLE `Recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RecipeCollection`
--

DROP TABLE IF EXISTS `RecipeCollection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RecipeCollection` (
  `UserID` int(11) NOT NULL,
  `RecipeID` int(7) NOT NULL,
  PRIMARY KEY (`UserID`,`RecipeID`),
  KEY `RecipeCollection_RecipeID_Recipe_RecipeID` (`RecipeID`),
  CONSTRAINT `RecipeCollection_RecipeID_Recipe_RecipeID` FOREIGN KEY (`RecipeID`) REFERENCES `Recipe` (`RecipeID`),
  CONSTRAINT `RecipeCollection_UserID_Customer_UserId` FOREIGN KEY (`UserID`) REFERENCES `Customer` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RecipeCollection`
--

LOCK TABLES `RecipeCollection` WRITE;
/*!40000 ALTER TABLE `RecipeCollection` DISABLE KEYS */;
/*!40000 ALTER TABLE `RecipeCollection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShoppingList`
--

DROP TABLE IF EXISTS `ShoppingList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ShoppingList` (
  `ListID` int(7) NOT NULL AUTO_INCREMENT,
  `ListName` varchar(25) NOT NULL,
  `IngredientID` int(7) NOT NULL,
  `StoreID` int(7) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Budget` int(4) DEFAULT NULL,
  PRIMARY KEY (`ListID`),
  KEY `ShoppingList_IngredientID_Ingredient_IngredientID` (`IngredientID`),
  KEY `ShoppingList_StoreID_GroceryStore_StoreId` (`StoreID`),
  CONSTRAINT `ShoppingList_IngredientID_Ingredient_IngredientID` FOREIGN KEY (`IngredientID`) REFERENCES `Ingredient` (`IngredientID`),
  CONSTRAINT `ShoppingList_StoreID_GroceryStore_StoreId` FOREIGN KEY (`StoreID`) REFERENCES `GroceryStore` (`StoreId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShoppingList`
--

LOCK TABLES `ShoppingList` WRITE;
/*!40000 ALTER TABLE `ShoppingList` DISABLE KEYS */;
/*!40000 ALTER TABLE `ShoppingList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShoppingListCollection`
--

DROP TABLE IF EXISTS `ShoppingListCollection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ShoppingListCollection` (
  `UserID` int(11) NOT NULL,
  `ListID` int(7) NOT NULL,
  PRIMARY KEY (`UserID`,`ListID`),
  KEY `ShoppingListCollection_ListID_ShoppingList_ListID` (`ListID`),
  CONSTRAINT `ShoppingListCollection_ListID_ShoppingList_ListID` FOREIGN KEY (`ListID`) REFERENCES `ShoppingList` (`ListID`),
  CONSTRAINT `ShoppingListCollection_UserID_Customer_UserId` FOREIGN KEY (`UserID`) REFERENCES `Customer` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShoppingListCollection`
--

LOCK TABLES `ShoppingListCollection` WRITE;
/*!40000 ALTER TABLE `ShoppingListCollection` DISABLE KEYS */;
/*!40000 ALTER TABLE `ShoppingListCollection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StoreCollection`
--

DROP TABLE IF EXISTS `StoreCollection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `StoreCollection` (
  `UserID` int(11) NOT NULL,
  `StoreID` int(7) NOT NULL,
  PRIMARY KEY (`UserID`,`StoreID`),
  UNIQUE KEY `StoreID` (`StoreID`),
  CONSTRAINT `StoreCollection_StoreID_GroceryStore_StoreId` FOREIGN KEY (`StoreID`) REFERENCES `GroceryStore` (`StoreId`),
  CONSTRAINT `StoreCollection_UserID_Customer_UserId` FOREIGN KEY (`UserID`) REFERENCES `Customer` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StoreCollection`
--

LOCK TABLES `StoreCollection` WRITE;
/*!40000 ALTER TABLE `StoreCollection` DISABLE KEYS */;
/*!40000 ALTER TABLE `StoreCollection` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-28  0:25:01
