-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : lun. 03 juin 2024 à 15:36
-- Version du serveur : 10.6.12-MariaDB-0ubuntu0.22.04.1
-- Version de PHP : 8.3.3-1+ubuntu22.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sae_23`
--

-- --------------------------------------------------------

--
-- Structure de la table `batiment`
--

CREATE TABLE `batiment` (
  `id_batiment` int(11) NOT NULL,
  `nom_batiment` varchar(300) NOT NULL,
  `adresse` varchar(300) NOT NULL,
  `ville` varchar(200) NOT NULL,
  `code_postale` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `batiment`
--

INSERT INTO `batiment` (`id_batiment`, `nom_batiment`, `adresse`, `ville`, `code_postale`) VALUES
(1, 'Centre culturel', '1Ter Rue du Moulin', 'Fontanil Cornillon', '38120'),
(2, 'Espace Claretière', '6 Rue du Cornillon', 'Fontanil Cornillon', '38120'),
(3, 'Maison de la culture', '4 rue Paul Claudel CS 92448', 'Grenoble', '38034'),
(4, 'LES CLOTS', '1 Rue des Tapis', 'Loriol-sur-Drôme', '26270'),
(5, 'Le Toit Rouge', '...', 'Montélimar', '26200'),
(6, 'Café de la Danse', '5 Pass. Louis-Philippe', 'Paris', '75011'),
(7, 'L_Olympia (music-hall)', '28 Bd des Capucines', 'Paris', '75009'),
(8, 'Zénith', '211 Av. Jean Jaurès', 'Paris', '75019'),
(9, 'Scène de musiques actuelles', '75 Av. Jules Maniez', 'Rennes', '35000'),
(10, 'Parc Expo Rennes-Aéroport', '......', 'Rennes', '35170'),
(11, 'Culturral', '213 Av. Albert Gruffat', 'Sallanches', '74700'),
(12, 'Conservatoire de Grenoble', '6 Chem. de Gordes', 'Grenoble', '38100'),
(13, 'Conservatoire de Valence Romans Agglo', '32 avenue Georges Clémenceau', 'Valence', '26000'),
(14, 'eglise saint germain des pres', '3 place st-germain_des_pres', 'Paris', '75006'),
(15, 'Salle Pleyel', '252 Rue du Faubourg Saint-Honoré', 'Paris', '75008'),
(16, 'Opéra Garnier', '8 Rue Scribe', 'Paris', '75009'),
(17, 'Theatre des Champs Elysées', '15 Avenue Montaigne', 'Paris', '75008'),
(18, 'Opéra Bastille', 'Place de la Bastille', 'Paris', '75012'),
(19, 'Salle Gaveau', '45-47 Rue La Boétie', 'Paris', '75008'),
(20, 'Philharmonie de Paris', '221 Avenue Jean Jaurès', 'Paris', '75019'),
(21, 'Théâtre de la Ville', '2 Place du Châtelet', 'Paris', '75004'),
(22, 'Konzerthaus de Vienne', 'Lothringerstraße 20', 'Vienne', '1030'),
(23, 'Konzerthaus de Berlin', 'Gendarmenmarkt', 'Berlin', '10117');

-- --------------------------------------------------------

--
-- Structure de la table `compositeur`
--

CREATE TABLE `compositeur` (
  `id_compositeur` int(11) NOT NULL,
  `nom_compositeur` varchar(300) NOT NULL,
  `date_naissance` date DEFAULT NULL,
  `date_mort` date DEFAULT NULL,
  `nb_morceau` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `compositeur`
--

INSERT INTO `compositeur` (`id_compositeur`, `nom_compositeur`, `date_naissance`, `date_mort`, `nb_morceau`) VALUES
(1, 'groupe little big', '2013-04-01', '0000-00-00', 93),
(2, 'Jean-Sébastien Bach', '1685-03-31', '1750-07-28', 1300),
(3, 'Ludwig van Beethoven', '1770-12-16', '1827-03-26', 500),
(4, 'Wolfgang Amadeus Mozart', '1756-01-27', '1791-12-05', NULL),
(5, 'Meganeko', NULL, NULL, 70),
(6, '钟离', '1969-12-31', NULL, 112),
(7, '魏无羡', '1998-10-31', NULL, 16),
(8, 'Adrien Nougaret (Zerator)', '1990-03-01', NULL, 13),
(9, 'Aron Michael Ekberg (AronChupa)', '1991-03-30', NULL, 17),
(10, 'Pyotr Ilyich Tchaikovsky', '1840-05-07', '1893-11-06', 104),
(11, 'Claude Debussy', '1862-08-22', '1918-03-25', 227),
(12, 'Franz Schubert', '1797-01-31', '1828-11-19', 600),
(13, 'Igor Stravinsky', '1882-06-17', '1971-04-06', 100),
(14, 'George Frideric Handel', '1685-02-23', '1759-04-14', 612),
(15, 'Antonio Vivaldi', '1678-03-04', '1741-07-28', 500),
(16, 'Sergei Rachmaninoff', '1873-04-01', '1943-03-28', 45),
(17, 'Frédéric Chopin', '1810-03-01', '1849-10-17', 230),
(18, 'Gustav Mahler', '1860-07-07', '1911-05-18', 40),
(19, 'Edvard Grieg', '1843-06-15', '1907-09-04', 74),
(20, 'Hans Zimmer', '1957-09-12', NULL, 200),
(21, 'John Williams', '1932-02-08', NULL, 150),
(22, 'Lindsey Stirling', '1986-09-21', NULL, 50),
(23, 'Alan Walker', '1997-08-24', NULL, 30),
(24, 'Dua Lipa', '1995-08-22', NULL, 40);

-- --------------------------------------------------------

--
-- Structure de la table `concert`
--

CREATE TABLE `concert` (
  `id_concert` int(11) NOT NULL,
  `id_salle` int(11) NOT NULL,
  `nom_concert` varchar(250) NOT NULL,
  `date_concert` date NOT NULL,
  `formation` enum('orchestre symphonique','orchestre à vent','orchestre à corde','duo','trio','quatuor','soliste','rock','traditionnelle','électro','spéciale') NOT NULL,
  `nb_place_restante` int(11) NOT NULL,
  `chef_d_orchestre` varchar(300) DEFAULT NULL,
  `soliste` varchar(300) DEFAULT NULL,
  `prix_place` float DEFAULT NULL,
  `visuel` tinyint(1) NOT NULL,
  `durée_concert` float NOT NULL COMMENT 'minute',
  `genre_concert` enum('symphonique','vent','corde','duo','trio','quatuor','soliste','rock','électro','traditionnelle','spéciale') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `concert`
--

INSERT INTO `concert` (`id_concert`, `id_salle`, `nom_concert`, `date_concert`, `formation`, `nb_place_restante`, `chef_d_orchestre`, `soliste`, `prix_place`, `visuel`, `durée_concert`, `genre_concert`) VALUES
(1, 12, '魔道祖师', '2024-06-12', 'traditionnelle', 500, NULL, NULL, 15, 1, 60, 'traditionnelle'),
(2, 8, '900K Live', '2024-03-25', 'électro', 2500, NULL, NULL, 20, 1, 90, 'électro'),
(3, 11, 'AronWorld', '2024-07-12', 'électro', 1197, NULL, NULL, 30, 1, 75, 'électro'),
(4, 16, 'Bach Que ma joie demeure', '2024-05-20', 'électro', 1350, NULL, NULL, NULL, 0, 30, 'symphonique'),
(5, 16, 'MOZART : REQUIEM', '2024-04-30', 'orchestre symphonique', 150, 'Jean-Charles Dunand', NULL, 22, 0, 150, 'symphonique'),
(6, 9, 'Little Big Concert', '2024-08-22', 'spéciale', 1046, NULL, NULL, 49, 1, 90, 'rock'),
(7, 17, 'Tchaikovsky Symphonie n°6', '2024-06-10', 'orchestre symphonique', 78, 'Klaus Mäkelä', 'Alexandre Kantorow', 75, 0, 120, 'symphonique'),
(9, 19, 'Schubert Symphonie n°8', '2024-09-20', 'orchestre symphonique', 300, 'Daniel Harding', NULL, 60, 0, 90, 'symphonique'),
(10, 20, 'Stravinsky Le Sacre du Printemps', '2024-11-25', 'orchestre symphonique', 50, 'Valery Gergiev', NULL, 100, 0, 105, 'symphonique'),
(11, 21, 'Haendel Le Messie', '2024-12-10', 'orchestre symphonique', 100, 'William Christie', NULL, 55, 0, 160, 'symphonique'),
(12, 22, 'Vivaldi Les Quatre Saisons', '2024-10-05', 'orchestre à corde', 500, 'Fabio Biondi', NULL, 45, 1, 65, 'symphonique'),
(13, 22, 'Rachmaninoff Concerto n°2', '2024-11-15', 'orchestre symphonique', 350, 'Vladimir Ashkenazy', 'Daniil Trifonov', 95, 0, 100, 'symphonique'),
(14, 23, 'Chopin Nocturnes', '2024-12-05', 'soliste', 400, NULL, 'Evgeny Kissin', 70, 0, 60, 'symphonique'),
(15, 24, 'Mahler Symphonie n°5', '2024-09-30', 'orchestre symphonique', 600, 'Riccardo Chailly', NULL, 85, 1, 75, 'symphonique'),
(16, 25, 'Grieg Concerto en la mineur', '2024-10-15', 'orchestre symphonique', 200, 'Mariss Jansons', 'Leif Ove Andsnes', 75, 0, 70, 'symphonique'),
(17, 22, 'Hans Zimmer Live', '2024-05-25', 'orchestre symphonique', 500, 'Hans Zimmer', NULL, 80, 1, 90, 'spéciale'),
(18, 22, 'John Williams en concert', '2024-06-10', 'orchestre symphonique', 450, 'John Williams', NULL, 100, 1, 95, 'spéciale'),
(19, 22, 'Lindsey Stirling Live', '2024-07-20', 'soliste', 400, NULL, 'Lindsey Stirling', 60, 1, 75, 'électro'),
(20, 9, 'Alan Walker en concert', '2024-08-15', 'soliste', 600, NULL, 'Alan Walker', 50, 1, 70, 'électro'),
(21, 8, 'Dua Lipa Live', '2024-09-10', 'soliste', 800, NULL, 'Dua Lipa', 65, 1, 85, 'rock');

-- --------------------------------------------------------

--
-- Structure de la table `jouer`
--

CREATE TABLE `jouer` (
  `id_concert` int(11) NOT NULL,
  `id_morceau` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `jouer`
--

INSERT INTO `jouer` (`id_concert`, `id_morceau`) VALUES
(6, 1),
(6, 2),
(6, 3),
(6, 4),
(6, 5),
(6, 6),
(6, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(2, 15),
(2, 16),
(2, 17),
(2, 18),
(2, 19),
(2, 20),
(2, 21),
(3, 22),
(3, 23),
(3, 24),
(3, 25),
(3, 26),
(4, 27),
(4, 28),
(4, 29),
(4, 30),
(4, 31),
(4, 32),
(4, 33),
(7, 62),
(7, 63),
(7, 64),
(9, 69),
(9, 70),
(9, 71),
(9, 72),
(10, 73),
(10, 74),
(10, 75),
(10, 76),
(11, 77),
(11, 78),
(11, 79),
(11, 80),
(12, 81),
(12, 82),
(12, 83),
(12, 84),
(13, 85),
(13, 86),
(13, 87),
(13, 88),
(14, 89),
(14, 90),
(14, 91),
(14, 92),
(14, 93),
(15, 94),
(15, 95),
(15, 96),
(15, 62),
(16, 98),
(16, 99),
(16, 100),
(17, 101),
(17, 102),
(17, 103),
(18, 105),
(18, 106),
(18, 107),
(19, 108),
(19, 109),
(19, 110),
(20, 111),
(20, 112),
(20, 113),
(21, 114),
(21, 115),
(21, 116);

-- --------------------------------------------------------

--
-- Structure de la table `morceau`
--

CREATE TABLE `morceau` (
  `id_morceau` int(11) NOT NULL,
  `id_compositeur` int(11) NOT NULL,
  `nom_morceau` varchar(400) NOT NULL,
  `date_composition` varchar(4) DEFAULT NULL COMMENT 'année',
  `durée_morceau` float NOT NULL COMMENT 'minutes',
  `genre` enum('concerto','composition','symphonie','duo','trio','sonate','quatuor','soliste','rock','électro','traditionnelle','spéciale') NOT NULL,
  `lieu_compo` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `morceau`
--

INSERT INTO `morceau` (`id_morceau`, `id_compositeur`, `nom_morceau`, `date_composition`, `durée_morceau`, `genre`, `lieu_compo`) VALUES
(1, 1, 'Rock-Papers-Scissors', '2019', 3.3, 'électro', 'Russie'),
(2, 1, 'Faradenza', '2018', 3.6, 'électro', 'Russie'),
(3, 1, 'Lolly Bomb', '2017', 5.25, 'spéciale', 'Russie'),
(4, 1, 'Hypnodancer', '2020', 4.6, 'spéciale', 'Russie'),
(5, 1, 'Sex Machine', '2021', 3.2, 'spéciale', 'Russie'),
(6, 1, 'Everyday I m drinking', '2013', 2.9, 'spéciale', 'Russie'),
(7, 1, 'Слэмятся пацаны', '2018', 4.1, 'spéciale', 'Russie'),
(8, 7, '【古琴】《何以歌》魔道祖师_广播剧主题曲_忘机本琴弹琴给你听（超燃）高能预警', '2019', 4.5, 'traditionnelle', 'Chine'),
(9, 7, '陈情令_The_Untamed', '2019', 2.5, 'traditionnelle', 'Chine'),
(10, 7, '魔道祖師前塵篇', '2019', 4, 'traditionnelle', 'Chine'),
(11, 7, '天官賜福', '2019', 4, 'traditionnelle', 'Chine'),
(12, 7, '【箜篌】演奏魔道祖師廣播劇第二季·主題曲《忘羨》', '2019', 4.4, 'traditionnelle', 'Chine'),
(13, 7, '【古琴】《若花怜蝶》为你战死是我至高无上的荣耀 ', '2019', 4, 'traditionnelle', 'Chine'),
(14, 7, '【古筝】魔道祖师《东风志》翻奏', '2019', 5, 'traditionnelle', 'Chine'),
(15, 8, 'COPYRIGHT : MOI', '2023', 2.5, 'électro', 'France'),
(16, 8, 'ANONYME', '2023', 3, 'électro', 'France'),
(17, 8, 'IMAGINE', '2023', 2, 'électro', 'France'),
(18, 8, 'OUI', '2023', 4.9, 'électro', 'France'),
(19, 8, 'KATOUM', '2023', 2.2, 'électro', 'France'),
(20, 8, 'RALENTIS', '2023', 2.5, 'électro', 'France'),
(21, 8, 'THE VOID', '2023', 2.5, 'électro', 'France'),
(22, 9, 'I_m an Albatraoz', '2015', 2.5, 'électro', 'Suéde'),
(23, 9, 'Trombone', '2021', 3.3, 'électro', 'Suède'),
(24, 9, 'Llama in my living room', '2018', 3.9, 'électro', 'Suède'),
(25, 9, 'She wants me dead', '2017', 2.9, 'électro', 'Suède'),
(26, 9, 'Little swing', '2016', 3.9, 'électro', 'Suède'),
(27, 2, 'Concerto 1 fa majeur', '1721', 17.9, 'concerto', 'Allemagne'),
(28, 2, 'concerto 2 fa majeur', '1721', 11.5, 'concerto', 'Allemagne'),
(29, 2, 'concerto 3 sol majeur', '1721', 19, 'concerto', 'Allemagne'),
(30, 2, 'concerto 4 sol majeur', '1721', 16.2, 'concerto', 'Allemagne'),
(31, 2, 'concerto 5 ré majeur', '1721', 17.5, 'concerto', 'Allemagne'),
(32, 2, 'concerto 6 sib majeur', '1721', 11.5, 'concerto', 'Allemagne'),
(33, 2, 'Toccata et fugue en ré mineur', '1707', 9.2, 'composition', 'Allemagne'),
(34, 4, 'Requiem', '1791', 150, 'symphonie', 'Vienne'),
(35, 7, '【古琴】《何以歌》魔道祖师_广播剧主题曲_忘机本琴弹琴给你听 (超燃) 高能预警', '2019', 4.5, 'traditionnelle', 'Chine'),
(36, 7, '陈情令_The_Untamed', '2019', 2.5, 'traditionnelle', 'Chine'),
(37, 7, '魔道祖師前塵篇', '2019', 4, 'traditionnelle', 'Chine'),
(38, 7, '天官賜福', '2019', 4, 'traditionnelle', 'Chine'),
(39, 7, '【箜篌】演奏魔道祖師廣播劇第二季·主題曲《忘羨》', '2019', 4.4, 'traditionnelle', 'Chine'),
(40, 7, '【古琴】《若花怜蝶》为你战死是我至高无上的荣耀 ', '2019', 4, 'traditionnelle', 'Chine'),
(41, 7, '【古筝】魔道祖师《东风志》翻奏', '2019', 5, 'traditionnelle', 'Chine'),
(42, 8, 'COPYRIGHT: MOI', '2023', 2.5, 'électro', 'France'),
(43, 8, 'ANONYME', '2023', 3, 'électro', 'France'),
(44, 8, 'IMAGINE', '2023', 2, 'électro', 'France'),
(45, 8, 'OUI', '2023', 4.9, 'électro', 'France'),
(46, 8, 'KATOUM', '2023', 2.2, 'électro', 'France'),
(47, 8, 'RALENTIS', '2023', 2.5, 'électro', 'France'),
(48, 8, 'THE VOID', '2023', 2.5, 'électro', 'France'),
(49, 9, 'I m an Albatraoz', '2015', 2.5, 'électro', 'Suède'),
(50, 9, 'Trombone', '2021', 3.3, 'électro', 'Suède'),
(51, 9, 'Llama in my living room', '2018', 3.9, 'électro', 'Suède'),
(52, 9, 'She wants me dead', '2017', 2.9, 'électro', 'Suède'),
(53, 9, 'Little swing', '2016', 3.9, 'électro', 'Suède'),
(54, 2, 'Concerto 1 fa majeur', '1721', 17.9, 'concerto', 'Allemagne'),
(55, 2, 'Concerto 2 fa majeur', '1721', 11.5, 'concerto', 'Allemagne'),
(56, 2, 'Concerto 3 sol majeur', '1721', 19, 'concerto', 'Allemagne'),
(57, 2, 'Concerto 4 sol majeur', '1721', 16.2, 'concerto', 'Allemagne'),
(58, 2, 'Concerto 5 ré majeur', '1721', 17.5, 'concerto', 'Allemagne'),
(59, 2, 'Concerto 6 sib majeur', '1721', 11.5, 'concerto', 'Allemagne'),
(60, 2, 'Toccata et fugue en ré mineur', '1707', 9.2, 'composition', 'Allemagne'),
(61, 4, 'Requiem', '1791', 150, 'symphonie', 'Vienne'),
(62, 10, 'symphonie n°5', '1888', 50, 'symphonie', 'Russie'),
(63, 10, 'Concerto pour piano n°1', '1875', 35, 'symphonie', 'Russie'),
(64, 10, 'Casse-Noisette', '1892', 20, 'symphonie', 'Russie'),
(65, 11, 'Prélude à l après-midi d un faune', '1894', 10, 'symphonie', 'France'),
(66, 11, 'La Mer', '1905', 23, 'composition', 'France'),
(67, 11, 'Suite Bergamasque', '1890', 19, 'symphonie', 'France'),
(68, 11, 'Clair de Lune', '1905', 5, 'composition', 'France'),
(69, 12, 'symphonie n°9 \"La Grande\"', '1828', 55, 'symphonie', 'Autriche'),
(70, 12, 'Quintette \"La Truite\"', '1819', 35, 'symphonie', 'Autriche'),
(71, 12, 'Ave Maria', '1825', 7, 'symphonie', 'Autriche'),
(72, 12, 'symphonie n°8 \"Inachevée\"', '1822', 25, 'symphonie', 'Autriche'),
(73, 13, 'L Oiseau de feu', '1910', 45, 'symphonie', 'Russie'),
(74, 13, 'Pulcinella', '1920', 35, 'symphonie', 'Russie'),
(75, 13, 'Pétrouchka', '1911', 35, 'symphonie', 'Russie'),
(76, 13, 'Le Sacre du Printemps', '1913', 35, 'symphonie', 'Russie'),
(77, 14, 'Water Music', '1717', 45, 'symphonie', 'Angleterre'),
(78, 14, 'Music for the Royal Fireworks', '1749', 20, 'symphonie', 'Angleterre'),
(79, 14, 'Rinaldo', '1711', 30, 'symphonie', 'Angleterre'),
(80, 14, 'Messiah', '1741', 60, 'symphonie', 'Angleterre'),
(81, 15, 'Gloria', '1715', 30, 'symphonie', 'Italie'),
(82, 15, 'Stabat Mater', '1712', 20, 'symphonie', 'Italie'),
(83, 15, 'Concerto pour mandoline', '1725', 15, 'symphonie', 'Italie'),
(84, 15, 'Les Quatre Saisons', '1723', 42, 'symphonie', 'Italie'),
(85, 16, 'Rhapsodie sur un thème de Paganini', '1934', 23, 'symphonie', 'Russie'),
(86, 16, 'symphonie n°2', '1908', 60, 'symphonie', 'Russie'),
(87, 16, 'Prélude en do# mineur', '1892', 4.5, 'symphonie', 'Russie'),
(88, 16, 'Concerto pour piano n°3', '1909', 38, 'symphonie', 'Russie'),
(89, 17, 'Ballade n°1', '1835', 10, 'symphonie', 'France'),
(90, 17, 'Etudes Op.10', '1833', 30, 'symphonie', 'France'),
(91, 17, 'Polonaise héroïque', '1842', 8, 'symphonie', 'France'),
(92, 17, 'Nocturne Op.9 n°2', '1832', 4, 'symphonie', 'France'),
(93, 17, 'Fantaisie-Impromptu', '1835', 5, 'symphonie', 'France'),
(94, 18, 'symphonie n°1', '1888', 50, 'symphonie', 'Autriche'),
(95, 18, 'Das Lied von der Erde', '1909', 60, 'symphonie', 'Autriche'),
(96, 18, 'Adagietto de la 5ème symphonie', '1902', 11, 'symphonie', 'Autriche'),
(97, 18, 'symphonie n°5', '1902', 75, 'symphonie', 'Autriche'),
(98, 19, 'Peer Gynt Suite n°1', '1875', 15, 'symphonie', 'Norvège'),
(99, 19, 'Peer Gynt Suite n°2', '1875', 17, 'symphonie', 'Norvège'),
(100, 19, 'Concerto pour piano en la mineur', '1868', 30, 'symphonie', 'Norvège'),
(101, 20, 'Time', '2010', 4.5, 'spéciale', 'USA'),
(102, 20, 'Cornfield Chase', '2014', 2.6, 'spéciale', 'USA'),
(103, 20, 'S.T.A.Y.', '2014', 6, 'spéciale', 'USA'),
(104, 20, 'Dream is Collapsing', '2010', 2.3, 'spéciale', 'USA'),
(105, 21, 'Theme from Jurassic Park', '1993', 6.3, 'spéciale', 'USA'),
(106, 21, 'Hedwig s Theme', '2001', 5.5, 'spéciale', 'USA'),
(107, 21, 'The Imperial March', '1980', 3, 'spéciale', 'USA'),
(108, 22, 'Crystallize', '2012', 4.3, 'électro', 'USA'),
(109, 22, 'Roundtable Rival', '2014', 3.4, 'électro', 'USA'),
(110, 22, 'Shatter Me', '2014', 4.4, 'électro', 'USA'),
(111, 23, 'Faded', '2015', 3.3, 'électro', 'Norvège'),
(112, 23, 'Alone', '2016', 2.4, 'électro', 'Norvège'),
(113, 23, 'The Spectre', '2017', 3.2, 'électro', 'Norvège'),
(114, 24, 'Don t Start Now', '2019', 3.3, 'rock', 'UK'),
(115, 24, 'Levitating', '2020', 3.2, 'rock', 'UK'),
(116, 24, 'Physical', '2020', 3.1, 'rock', 'UK');

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

CREATE TABLE `reservation` (
  `id_reservation` int(11) NOT NULL,
  `id_concert` int(11) NOT NULL,
  `nom_reservation` varchar(150) NOT NULL,
  `prenom_reservation` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `salle`
--

CREATE TABLE `salle` (
  `id_salle` int(11) NOT NULL,
  `id_batiment` int(11) NOT NULL,
  `nom_salle` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `salle`
--

INSERT INTO `salle` (`id_salle`, `id_batiment`, `nom_salle`) VALUES
(1, 1, 'Atrium'),
(2, 2, 'Salle Polyvalente'),
(3, 3, 'Grande salle'),
(4, 3, 'Auditorium'),
(5, 4, 'SALLE JEAN CLÉMENT'),
(6, 5, 'Le Toit Rouge'),
(7, 6, 'Café de la Danse'),
(8, 7, 'L_Olympia'),
(9, 8, 'Zénith'),
(10, 9, 'L_Antipode MJC'),
(11, 10, 'Le MuzikHall'),
(12, 11, 'Salle Léon Curral'),
(13, 12, 'Stekel'),
(14, 12, 'Parc'),
(15, 13, 'Auditorium'),
(16, 14, 'eglise saint germain des pres'),
(17, 15, 'Salle Pleyel'),
(18, 16, 'Opéra Garnier'),
(19, 17, 'Theatre des Champs Elysées'),
(20, 18, 'Opéra Bastille'),
(21, 19, 'Salle Gaveau'),
(22, 20, 'Philharmonie de Paris'),
(23, 21, 'Théâtre de la Ville'),
(24, 22, 'Konzerthaus de Vienne'),
(25, 23, 'Konzerthaus de Berlin');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `batiment`
--
ALTER TABLE `batiment`
  ADD PRIMARY KEY (`id_batiment`);

--
-- Index pour la table `compositeur`
--
ALTER TABLE `compositeur`
  ADD PRIMARY KEY (`id_compositeur`);

--
-- Index pour la table `concert`
--
ALTER TABLE `concert`
  ADD PRIMARY KEY (`id_concert`),
  ADD KEY `id_salle` (`id_salle`);

--
-- Index pour la table `jouer`
--
ALTER TABLE `jouer`
  ADD KEY `id_concert` (`id_concert`),
  ADD KEY `id_morceau` (`id_morceau`);

--
-- Index pour la table `morceau`
--
ALTER TABLE `morceau`
  ADD PRIMARY KEY (`id_morceau`),
  ADD KEY `id_compositeur` (`id_compositeur`);

--
-- Index pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`id_reservation`),
  ADD KEY `id_concert` (`id_concert`);

--
-- Index pour la table `salle`
--
ALTER TABLE `salle`
  ADD PRIMARY KEY (`id_salle`),
  ADD KEY `id_batiment` (`id_batiment`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `batiment`
--
ALTER TABLE `batiment`
  MODIFY `id_batiment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT pour la table `compositeur`
--
ALTER TABLE `compositeur`
  MODIFY `id_compositeur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT pour la table `concert`
--
ALTER TABLE `concert`
  MODIFY `id_concert` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT pour la table `morceau`
--
ALTER TABLE `morceau`
  MODIFY `id_morceau` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- AUTO_INCREMENT pour la table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `id_reservation` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `salle`
--
ALTER TABLE `salle`
  MODIFY `id_salle` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `concert`
--
ALTER TABLE `concert`
  ADD CONSTRAINT `FK_id_salle` FOREIGN KEY (`id_salle`) REFERENCES `salle` (`id_salle`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `jouer`
--
ALTER TABLE `jouer`
  ADD CONSTRAINT `FK_id_concert` FOREIGN KEY (`id_concert`) REFERENCES `concert` (`id_concert`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_id_morceau` FOREIGN KEY (`id_morceau`) REFERENCES `morceau` (`id_morceau`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `morceau`
--
ALTER TABLE `morceau`
  ADD CONSTRAINT `FK_id_compositeur` FOREIGN KEY (`id_compositeur`) REFERENCES `compositeur` (`id_compositeur`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `FK_id_concert_deux` FOREIGN KEY (`id_concert`) REFERENCES `concert` (`id_concert`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `salle`
--
ALTER TABLE `salle`
  ADD CONSTRAINT `FK_id_batiment` FOREIGN KEY (`id_batiment`) REFERENCES `batiment` (`id_batiment`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
