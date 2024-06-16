/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ALUNO` (
  `ID` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `matricula` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `endereco` varchar(50) NOT NULL,
  `telefone` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
