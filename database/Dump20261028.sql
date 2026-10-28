-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: base
-- ------------------------------------------------------
-- Server version	26.7.0

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

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '28dccac1-a55a-11f1-8f78-d8bbc1211f9f:1-375';

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_admin_idx` (`id_usuario`),
  CONSTRAINT `id_usuario_admin` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciudades`
--

DROP TABLE IF EXISTS `ciudades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `ciudad` varchar(45) DEFAULT NULL,
  `id_provincia` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_prov_idx` (`id_provincia`),
  CONSTRAINT `id_prov` FOREIGN KEY (`id_provincia`) REFERENCES `provincias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=227 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudades`
--

LOCK TABLES `ciudades` WRITE;
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` VALUES (1,1,'La Plata',1),(2,1,'Mar del Plata',1),(3,1,'Bahia Blanca',1),(4,1,'Tandil',1),(5,1,'San Nicolas de los Arroyos',1),(6,1,'San Fernando del Valle de Catamarca',2),(7,1,'Andalgala',2),(8,1,'Tinogasta',2),(9,1,'Resistencia',3),(10,1,'Presidencia Roque Saenz Pena',3),(11,1,'Villa Angela',3),(12,1,'Rawson',4),(13,1,'Comodoro Rivadavia',4),(14,1,'Puerto Madryn',4),(15,1,'Trelew',4),(16,1,'Cordoba',5),(17,1,'Villa Carlos Paz',5),(18,1,'Rio Cuarto',5),(19,1,'Villa Maria',5),(20,1,'Corrientes',6),(21,1,'Goya',6),(22,1,'Paso de los Libres',6),(23,1,'Parana',7),(24,1,'Concordia',7),(25,1,'Gualeguaychu',7),(26,1,'Formosa',8),(27,1,'Clorinda',8),(28,1,'Pirané',8),(29,1,'San Salvador de Jujuy',9),(30,1,'Palpala',9),(31,1,'Humahuaca',9),(32,1,'Santa Rosa',10),(33,1,'General Pico',10),(34,1,'Toay',10),(35,1,'La Rioja',11),(36,1,'Chilecito',11),(37,1,'Aimogasta',11),(38,1,'Mendoza',12),(39,1,'San Rafael',12),(40,1,'Godoy Cruz',12),(41,1,'Lujan de Cuyo',12),(42,1,'Posadas',13),(43,1,'Obera',13),(44,1,'Eldorado',13),(45,1,'Puerto Iguazu',13),(46,1,'Neuquen',14),(47,1,'San Martin de los Andes',14),(48,1,'Villa La Angostura',14),(49,1,'Viedma',15),(50,1,'San Carlos de Bariloche',15),(51,1,'General Roca',15),(52,1,'Cipolletti',15),(53,1,'Salta',16),(54,1,'San Ramon de la Nueva Oran',16),(55,1,'Tartagal',16),(56,1,'San Juan',17),(57,1,'Caucete',17),(58,1,'Jachal',17),(59,1,'San Luis',18),(60,1,'Villa Mercedes',18),(61,1,'Merlo',18),(62,1,'Rio Gallegos',19),(63,1,'Caleta Olivia',19),(64,1,'El Calafate',19),(65,1,'Santa Fe',20),(66,1,'Rosario',20),(67,1,'Rafaela',20),(68,1,'Venado Tuerto',20),(69,1,'Santiago del Estero',21),(70,1,'La Banda',21),(71,1,'Termas de Rio Hondo',21),(72,1,'Ushuaia',22),(73,1,'Rio Grande',22),(74,1,'Tolhuin',22),(75,1,'San Miguel de Tucuman',23),(76,1,'Tafi Viejo',23),(77,1,'Concepcion',23),(78,1,'Sao Paulo',24),(79,1,'Campinas',24),(80,1,'Santos',24),(81,1,'Ribeirao Preto',24),(82,1,'Rio de Janeiro',25),(83,1,'Niteroi',25),(84,1,'Petropolis',25),(85,1,'Belo Horizonte',26),(86,1,'Uberlandia',26),(87,1,'Juiz de Fora',26),(88,1,'Salvador',27),(89,1,'Feira de Santana',27),(90,1,'Ilheus',27),(91,1,'Curitiba',28),(92,1,'Londrina',28),(93,1,'Maringa',28),(94,1,'Porto Alegre',29),(95,1,'Caxias do Sul',29),(96,1,'Pelotas',29),(97,1,'Santiago',30),(98,1,'Puente Alto',30),(99,1,'Maipu',30),(100,1,'Valparaiso',31),(101,1,'Vina del Mar',31),(102,1,'Quilpue',31),(103,1,'Concepcion',32),(104,1,'Los Angeles',32),(105,1,'Talcahuano',32),(106,1,'Temuco',33),(107,1,'Villarrica',33),(108,1,'Angol',33),(109,1,'Puerto Montt',34),(110,1,'Osorno',34),(111,1,'Castro',34),(112,1,'Montevideo',35),(113,1,'Ciudad de la Costa',36),(114,1,'Las Piedras',36),(115,1,'Pando',36),(116,1,'Maldonado',37),(117,1,'Punta del Este',37),(118,1,'San Carlos',37),(119,1,'Colonia del Sacramento',38),(120,1,'Carmelo',38),(121,1,'Nueva Palmira',38),(122,1,'Salto',39),(123,1,'Constitucion',39),(124,1,'Belen',39),(125,1,'Aregua',40),(126,1,'San Lorenzo',40),(127,1,'Luque',40),(128,1,'Ciudad del Este',41),(129,1,'Hernandarias',41),(130,1,'Presidente Franco',41),(131,1,'Encarnacion',42),(132,1,'Colonias Unidas',42),(133,1,'Hohenau',42),(134,1,'Coronel Oviedo',43),(135,1,'Caaguazu',43),(136,1,'Doctor Juan Eulogio Estigarribia',43),(137,1,'Caacupe',44),(138,1,'Eusebio Ayala',44),(139,1,'Piribebuy',44),(140,1,'Los Angeles',45),(141,1,'San Francisco',45),(142,1,'San Diego',45),(143,1,'Sacramento',45),(144,1,'Houston',46),(145,1,'Dallas',46),(146,1,'Austin',46),(147,1,'San Antonio',46),(148,1,'Miami',47),(149,1,'Orlando',47),(150,1,'Tampa',47),(151,1,'Tallahassee',47),(152,1,'New York City',48),(153,1,'Buffalo',48),(154,1,'Albany',48),(155,1,'Rochester',48),(156,1,'Anchorage',49),(157,1,'Fairbanks',49),(158,1,'Juneau',49),(159,1,'Honolulu',50),(160,1,'Hilo',50),(161,1,'Kailua',50),(162,1,'Guadalajara',51),(163,1,'Puerto Vallarta',51),(164,1,'Zapopan',51),(165,1,'Merida',52),(166,1,'Valladolid',52),(167,1,'Progreso',52),(168,1,'Oaxaca de Juarez',53),(169,1,'Salina Cruz',53),(170,1,'Juchitan de Zaragoza',53),(171,1,'Puebla',54),(172,1,'Tehuacan',54),(173,1,'San Martin Texmelucan',54),(174,1,'Chihuahua',55),(175,1,'Ciudad Juarez',55),(176,1,'Delicias',55),(177,1,'Sevilla',56),(178,1,'Malaga',56),(179,1,'Granada',56),(180,1,'Cordoba',56),(181,1,'Barcelona',57),(182,1,'Girona',57),(183,1,'Tarragona',57),(184,1,'Lleida',57),(185,1,'Santiago de Compostela',58),(186,1,'Vigo',58),(187,1,'A Coruna',58),(188,1,'Ourense',58),(189,1,'Zaragoza',59),(190,1,'Huesca',59),(191,1,'Teruel',59),(192,1,'Madrid',60),(193,1,'Alcala de Henares',60),(194,1,'Getafe',60),(195,1,'Mostoles',60),(196,1,'Milan',61),(197,1,'Bergamo',61),(198,1,'Brescia',61),(199,1,'Roma',62),(200,1,'Latina',62),(201,1,'Viterbo',62),(202,1,'Florencia',63),(203,1,'Pisa',63),(204,1,'Siena',63),(205,1,'Palermo',64),(206,1,'Catania',64),(207,1,'Siracusa',64),(208,1,'Venecia',65),(209,1,'Verona',65),(210,1,'Padua',65),(211,1,'Sapporo',66),(212,1,'Hakodate',66),(213,1,'Asahikawa',66),(214,1,'Tokyo',67),(215,1,'Hachioji',67),(216,1,'Tachikawa',67),(217,1,'Osaka',68),(218,1,'Sakai',68),(219,1,'Higashiosaka',68),(220,1,'Kyoto',69),(221,1,'Uji',69),(222,1,'Kameoka',69),(223,1,'Naha',70),(224,1,'Okinawa',70),(225,1,'Uruma',70),(226,1,'CABA',71);
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `razon_social` varchar(45) DEFAULT NULL,
  `cuit` varchar(45) DEFAULT NULL,
  `pagina_web` varchar(45) DEFAULT NULL,
  `compras` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_cliente_idx` (`id_usuario`),
  CONSTRAINT `id_usuario_cliente` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_factura` int DEFAULT NULL,
  `id_proveedor` int DEFAULT NULL,
  `id_gerente` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_factura_compra_idx` (`id_factura`),
  KEY `id_proveedor_idx` (`id_proveedor`),
  KEY `id_gerente_idx` (`id_gerente`),
  CONSTRAINT `id_factura_compra` FOREIGN KEY (`id_factura`) REFERENCES `facturas` (`id`),
  CONSTRAINT `id_gerente` FOREIGN KEY (`id_gerente`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `id_proveedor` FOREIGN KEY (`id_proveedor`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamentos`
--

DROP TABLE IF EXISTS `departamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `departamento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='departamentos dentro de esta empresa, cómo venta, marketing, logistica, it, etc';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamentos`
--

LOCK TABLES `departamentos` WRITE;
/*!40000 ALTER TABLE `departamentos` DISABLE KEYS */;
INSERT INTO `departamentos` VALUES (1,1,'Administracion'),(2,1,'Ventas'),(3,1,'Marketing'),(4,1,'Compras'),(5,1,'Logistica'),(6,1,'Deposito'),(7,1,'Atencion al cliente'),(8,1,'Recursos Humanos'),(9,1,'Contabilidad'),(10,1,'Finanzas'),(11,1,'Sistemas e IT'),(12,1,'Mantenimiento'),(13,1,'Seguridad e Higiene'),(14,1,'Direccion'),(15,1,'Produccion');
/*!40000 ALTER TABLE `departamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalles`
--

DROP TABLE IF EXISTS `detalles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_factura` int DEFAULT NULL,
  `id_producto` int DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `valor_unitario` float DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_factura_detalle_idx` (`id_factura`),
  KEY `id_producto_idx` (`id_producto`),
  CONSTRAINT `id_factura_detalle` FOREIGN KEY (`id_factura`) REFERENCES `facturas` (`id`),
  CONSTRAINT `id_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles`
--

LOCK TABLES `detalles` WRITE;
/*!40000 ALTER TABLE `detalles` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `dni` varchar(45) DEFAULT NULL,
  `edad` int DEFAULT NULL,
  `sueldo` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_empelado_idx` (`id_usuario`),
  CONSTRAINT `id_usuario_empelado` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estados`
--

DROP TABLE IF EXISTS `estados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `estado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='estados de productos, como agotado, nuevo, casi agotado, en descuento!,con stock, etc';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados`
--

LOCK TABLES `estados` WRITE;
/*!40000 ALTER TABLE `estados` DISABLE KEYS */;
INSERT INTO `estados` VALUES (1,1,'Nuevo'),(2,1,'Con stock'),(3,1,'Stock bajo'),(4,1,'Casi agotado'),(5,1,'Agotado'),(6,1,'En descuento'),(7,1,'Fuera de temporada'),(8,1,'Vencido'),(9,1,'Dañado'),(10,1,'Descontinuado');
/*!40000 ALTER TABLE `estados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas`
--

DROP TABLE IF EXISTS `facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `descuento` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `id_tipo_factura` int DEFAULT NULL,
  `id_mp` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_tipo_factura_idx` (`id_tipo_factura`),
  KEY `id_mp_idx` (`id_mp`),
  CONSTRAINT `id_mp` FOREIGN KEY (`id_mp`) REFERENCES `mdp` (`id`),
  CONSTRAINT `id_tipo_factura` FOREIGN KEY (`id_tipo_factura`) REFERENCES `tipos_facturas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas`
--

LOCK TABLES `facturas` WRITE;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gerentes`
--

DROP TABLE IF EXISTS `gerentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gerentes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `dni` varchar(45) DEFAULT NULL,
  `edad` int DEFAULT NULL,
  `sueldo` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_gerente_idx` (`id_usuario`),
  CONSTRAINT `id_usuario_gerente` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gerentes`
--

LOCK TABLES `gerentes` WRITE;
/*!40000 ALTER TABLE `gerentes` DISABLE KEYS */;
/*!40000 ALTER TABLE `gerentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logins`
--

DROP TABLE IF EXISTS `logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_login_idx` (`id_usuario`),
  CONSTRAINT `id_usuario_login` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logins`
--

LOCK TABLES `logins` WRITE;
/*!40000 ALTER TABLE `logins` DISABLE KEYS */;
/*!40000 ALTER TABLE `logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mails`
--

DROP TABLE IF EXISTS `mails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mails` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `mail` varchar(320) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mails`
--

LOCK TABLES `mails` WRITE;
/*!40000 ALTER TABLE `mails` DISABLE KEYS */;
/*!40000 ALTER TABLE `mails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mdp`
--

DROP TABLE IF EXISTS `mdp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mdp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `mdp` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mdp`
--

LOCK TABLES `mdp` WRITE;
/*!40000 ALTER TABLE `mdp` DISABLE KEYS */;
/*!40000 ALTER TABLE `mdp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paises`
--

DROP TABLE IF EXISTS `paises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paises` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `pais` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paises`
--

LOCK TABLES `paises` WRITE;
/*!40000 ALTER TABLE `paises` DISABLE KEYS */;
INSERT INTO `paises` VALUES (1,1,'Argentina'),(2,1,'Brasil'),(3,1,'Chile'),(4,1,'Uruguay'),(5,1,'Paraguay'),(6,1,'Estados Unidos'),(7,1,'Mexico'),(8,1,'España'),(9,1,'Italia'),(10,1,'Japon');
/*!40000 ALTER TABLE `paises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_estado` int DEFAULT NULL,
  `id_tipo_producto` int DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `producto` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_estado_idx` (`id_estado`),
  KEY `id_tipo_producto_idx` (`id_tipo_producto`),
  CONSTRAINT `id_estado` FOREIGN KEY (`id_estado`) REFERENCES `estados` (`id`),
  CONSTRAINT `id_tipo_producto` FOREIGN KEY (`id_tipo_producto`) REFERENCES `tipos_productos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `razon_social` varchar(45) DEFAULT NULL,
  `cuit` varchar(45) DEFAULT NULL,
  `pagina_web` varchar(45) DEFAULT NULL,
  `ventas` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_proveedor_idx` (`id_usuario`),
  CONSTRAINT `id_usuario_proveedor` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provincias`
--

DROP TABLE IF EXISTS `provincias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provincias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `provincia` varchar(45) DEFAULT NULL,
  `id_pais` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_pai_idx` (`id_pais`),
  CONSTRAINT `id_pai` FOREIGN KEY (`id_pais`) REFERENCES `paises` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='provincias/estados/prefecturas';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provincias`
--

LOCK TABLES `provincias` WRITE;
/*!40000 ALTER TABLE `provincias` DISABLE KEYS */;
INSERT INTO `provincias` VALUES (1,1,'Buenos Aires',1),(2,1,'Catamarca',1),(3,1,'Chaco',1),(4,1,'Chubut',1),(5,1,'Cordoba',1),(6,1,'Corrientes',1),(7,1,'Entre Rios',1),(8,1,'Formosa',1),(9,1,'Jujuy',1),(10,1,'La Pampa',1),(11,1,'La Rioja',1),(12,1,'Mendoza',1),(13,1,'Misiones',1),(14,1,'Neuquen',1),(15,1,'Rio Negro',1),(16,1,'Salta',1),(17,1,'San Juan',1),(18,1,'San Luis',1),(19,1,'Santa Cruz',1),(20,1,'Santa Fe',1),(21,1,'Santiago del Estero',1),(22,1,'Tierra del Fuego',1),(23,1,'Tucuman',1),(24,1,'Sao Paulo',2),(25,1,'Rio de Janeiro',2),(26,1,'Minas Gerais',2),(27,1,'Bahia',2),(28,1,'Parana',2),(29,1,'Rio Grande do Sul',2),(30,1,'Santiago',3),(31,1,'Valparaiso',3),(32,1,'Biobio',3),(33,1,'Araucania',3),(34,1,'Los Lagos',3),(35,1,'Montevideo',4),(36,1,'Canelones',4),(37,1,'Maldonado',4),(38,1,'Colonia',4),(39,1,'Salto',4),(40,1,'Central',5),(41,1,'Alto Parana',5),(42,1,'Itapua',5),(43,1,'Caaguazu',5),(44,1,'Cordillera',5),(45,1,'California',6),(46,1,'Texas',6),(47,1,'Florida',6),(48,1,'New York',6),(49,1,'Alaska',6),(50,1,'Hawaii',6),(51,1,'Jalisco',7),(52,1,'Yucatan',7),(53,1,'Oaxaca',7),(54,1,'Puebla',7),(55,1,'Chihuahua',7),(56,1,'Andalucia',8),(57,1,'Cataluna',8),(58,1,'Galicia',8),(59,1,'Aragon',8),(60,1,'Comunidad de Madrid',8),(61,1,'Lombardia',9),(62,1,'Lazio',9),(63,1,'Toscana',9),(64,1,'Sicilia',9),(65,1,'Veneto',9),(66,1,'Hokkaido',10),(67,1,'Tokyo',10),(68,1,'Osaka',10),(69,1,'Kyoto',10),(70,1,'Okinawa',10),(71,1,'CABA',1);
/*!40000 ALTER TABLE `provincias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `redes`
--

DROP TABLE IF EXISTS `redes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `redes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `handle` varchar(45) DEFAULT NULL,
  `id_tipo_rs` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_tipo_rs_idx` (`id_tipo_rs`),
  CONSTRAINT `id_tipo_rs` FOREIGN KEY (`id_tipo_rs`) REFERENCES `tipos_rs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `redes`
--

LOCK TABLES `redes` WRITE;
/*!40000 ALTER TABLE `redes` DISABLE KEYS */;
/*!40000 ALTER TABLE `redes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `rol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,1,'empleado'),(2,1,'gerente'),(3,1,'admin'),(4,1,'cliente'),(5,1,'proveedor');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telefonos`
--

DROP TABLE IF EXISTS `telefonos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `telefonos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `telefono` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telefonos`
--

LOCK TABLES `telefonos` WRITE;
/*!40000 ALTER TABLE `telefonos` DISABLE KEYS */;
/*!40000 ALTER TABLE `telefonos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_facturas`
--

DROP TABLE IF EXISTS `tipos_facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_facturas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `tipo_factura` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_facturas`
--

LOCK TABLES `tipos_facturas` WRITE;
/*!40000 ALTER TABLE `tipos_facturas` DISABLE KEYS */;
INSERT INTO `tipos_facturas` VALUES (1,1,'venta'),(2,1,'compra');
/*!40000 ALTER TABLE `tipos_facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_productos`
--

DROP TABLE IF EXISTS `tipos_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `tipo_producto` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tipos de productos, ej: lacteo, carne, verdura, jugete,herramienta, mascota, otro, etc\n(sería como un almacen/supermercado/etc';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_productos`
--

LOCK TABLES `tipos_productos` WRITE;
/*!40000 ALTER TABLE `tipos_productos` DISABLE KEYS */;
INSERT INTO `tipos_productos` VALUES (1,1,'Alimentos'),(2,1,'Bebidas'),(3,1,'Limpieza'),(4,1,'Higiene personal'),(5,1,'Lacteos'),(6,1,'Carnes'),(7,1,'Golosinas'),(8,1,'Frutas y verduras'),(9,1,'Herramientas'),(10,1,'Juguetes'),(11,1,'Accesorios para mascotas'),(12,1,'Electrodomesticos'),(13,1,'Libreria'),(14,1,'Indumentaria'),(15,1,'Perfumería'),(16,1,'Decoración'),(17,1,'Ferreteria'),(18,1,'Libros'),(19,1,'Otros');
/*!40000 ALTER TABLE `tipos_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_rs`
--

DROP TABLE IF EXISTS `tipos_rs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_rs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `red_social` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='tipos de redes sociales, ej: facebook, instagram, otro, etc.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_rs`
--

LOCK TABLES `tipos_rs` WRITE;
/*!40000 ALTER TABLE `tipos_rs` DISABLE KEYS */;
INSERT INTO `tipos_rs` VALUES (1,1,'Facebook'),(2,1,'Instagram'),(3,1,'LinkedIn'),(4,1,'TikTok'),(5,1,'Twitter'),(6,1,'YouTube'),(7,1,'WhatsApp'),(8,1,'Telegram'),(9,1,'Pinterest'),(10,1,'Reddit'),(11,1,'Otra');
/*!40000 ALTER TABLE `tipos_rs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `usuario` varchar(45) NOT NULL,
  `contrasenia` varchar(45) NOT NULL,
  `id_rol` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_UNIQUE` (`usuario`),
  KEY `id_rol_idx` (`id_rol`),
  CONSTRAINT `id_rol` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,1,'emp','prueba',1),(2,1,'ger','prueba',2),(3,1,'adm','prueba',3),(4,1,'cli','prueba',4),(5,1,'pro','prueba',5);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_departamentos`
--

DROP TABLE IF EXISTS `usuarios_departamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_departamentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `id_departamento` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_departamento_idx` (`id_usuario`),
  KEY `id_departamento_idx` (`id_departamento`),
  CONSTRAINT `id_departamento` FOREIGN KEY (`id_departamento`) REFERENCES `departamentos` (`id`),
  CONSTRAINT `id_usuario_departamento` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_departamentos`
--

LOCK TABLES `usuarios_departamentos` WRITE;
/*!40000 ALTER TABLE `usuarios_departamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_departamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_mails`
--

DROP TABLE IF EXISTS `usuarios_mails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_mails` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `id_mail` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_mail_idx` (`id_usuario`),
  KEY `id_mail_idx` (`id_mail`),
  CONSTRAINT `id_mail` FOREIGN KEY (`id_mail`) REFERENCES `mails` (`id`),
  CONSTRAINT `id_usuario_mail` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_mails`
--

LOCK TABLES `usuarios_mails` WRITE;
/*!40000 ALTER TABLE `usuarios_mails` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_mails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_redes`
--

DROP TABLE IF EXISTS `usuarios_redes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_redes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `id_red` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_red_idx` (`id_usuario`),
  KEY `id_red_idx` (`id_red`),
  CONSTRAINT `id_red` FOREIGN KEY (`id_red`) REFERENCES `redes` (`id`),
  CONSTRAINT `id_usuario_red` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_redes`
--

LOCK TABLES `usuarios_redes` WRITE;
/*!40000 ALTER TABLE `usuarios_redes` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_redes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_telefonos`
--

DROP TABLE IF EXISTS `usuarios_telefonos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_telefonos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `id_telefono` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_telefono_idx` (`id_usuario`),
  KEY `id_telefono_idx` (`id_telefono`),
  CONSTRAINT `id_telefono` FOREIGN KEY (`id_telefono`) REFERENCES `telefonos` (`id`),
  CONSTRAINT `id_usuario_telefono` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_telefonos`
--

LOCK TABLES `usuarios_telefonos` WRITE;
/*!40000 ALTER TABLE `usuarios_telefonos` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_telefonos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_ubicaciones`
--

DROP TABLE IF EXISTS `usuarios_ubicaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_ubicaciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_usuario` int DEFAULT NULL,
  `id_pais` int DEFAULT NULL,
  `id_provincia` int DEFAULT NULL,
  `id_ciudad` int DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `codigo_postal` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario_ubicacion_idx` (`id_usuario`),
  KEY `id_pais_idx` (`id_pais`),
  KEY `id_provincia_idx` (`id_provincia`),
  KEY `id_ciudad_idx` (`id_ciudad`),
  CONSTRAINT `id_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudades` (`id`),
  CONSTRAINT `id_pais` FOREIGN KEY (`id_pais`) REFERENCES `paises` (`id`),
  CONSTRAINT `id_provincia` FOREIGN KEY (`id_provincia`) REFERENCES `provincias` (`id`),
  CONSTRAINT `id_usuario_ubicacion` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_ubicaciones`
--

LOCK TABLES `usuarios_ubicaciones` WRITE;
/*!40000 ALTER TABLE `usuarios_ubicaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_ubicaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `habilitado` int DEFAULT '1',
  `id_factura` int DEFAULT NULL,
  `id_empleado` int DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_factura_venta_idx` (`id_factura`),
  KEY `id_empleado_idx` (`id_empleado`),
  KEY `id_cliente_idx` (`id_cliente`),
  CONSTRAINT `id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `id_empleado` FOREIGN KEY (`id_empleado`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `id_factura_venta` FOREIGN KEY (`id_factura`) REFERENCES `facturas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-28 19:23:00
