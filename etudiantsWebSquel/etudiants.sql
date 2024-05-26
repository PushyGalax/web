-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  sam. 25 mars 2023 à 18:09
-- Version du serveur :  5.7.17
-- Version de PHP :  5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  etudiants
--
CREATE DATABASE IF NOT EXISTS etudiants DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE etudiants;

-- --------------------------------------------------------

--
-- Structure de la table etudiant
--

CREATE TABLE etudiant (
  numEtudiant int(11) NOT NULL,
  prenom varchar(25) NOT NULL,
  nom varchar(25) NOT NULL,
  dateNaissance date NOT NULL DEFAULT '2000-01-01'
) ENGINE=MyISAM DEFAULT CHARSET=UTF_8;

--
-- Déchargement des données de la table etudiant
--

INSERT INTO etudiant (numEtudiant, prenom, nom, dateNaissance) VALUES
(1, 'Christian', 'DUCCINI', '1900-01-01'),
(11, 'Sdgh', 'RH', '2023-03-25'),
(3, 'Paul', 'ISSON', '1982-09-09'),
(4, 'Mic', 'ROSOFT', '1980-05-05'),
(5, 'Mat', 'HEMATIC', '1979-12-10'),
(6, 'Vincent', 'MILANES', '1980-03-13'),
(7, 'Paula', 'RITE', '1981-09-15'),
(8, 'Nin', 'DEJARDIN', '1981-05-04'),
(9, 'Jonathan', 'LETRAIN', '1981-06-23'),
(10, 'Floriane', 'DUCCINI', '2002-08-10');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table etudiant
--
ALTER TABLE etudiant
  ADD PRIMARY KEY (numEtudiant);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table etudiant
--
ALTER TABLE etudiant
  MODIFY numEtudiant int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
