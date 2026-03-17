-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema baseball
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema baseball
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `baseball` DEFAULT CHARACTER SET utf8mb3 ;
USE `baseball` ;

-- -----------------------------------------------------
-- Table `baseball`.`ballpark`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`ballpark` (
  `ballparkID` INT NOT NULL AUTO_INCREMENT,
  `ballparkName` VARCHAR(45) NULL DEFAULT NULL,
  `city` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`ballparkID`))
ENGINE = InnoDB
AUTO_INCREMENT = 31
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`season`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`season` (
  `seasonID` INT NOT NULL AUTO_INCREMENT,
  `startDate` DATETIME NULL DEFAULT NULL,
  `endDate` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`seasonID`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`team` (
  `teamID` INT NOT NULL AUTO_INCREMENT,
  `teamName` VARCHAR(45) NULL DEFAULT NULL,
  `city` VARCHAR(45) NULL DEFAULT NULL,
  `ballparkID` INT NULL DEFAULT NULL,
  `seasonID` INT NULL DEFAULT NULL,
  PRIMARY KEY (`teamID`),
  INDEX `fk_team_ballpark_idx` (`ballparkID` ASC) VISIBLE,
  INDEX `fk_team_season_idx` (`seasonID` ASC) VISIBLE,
  CONSTRAINT `fk_team_ballpark`
    FOREIGN KEY (`ballparkID`)
    REFERENCES `baseball`.`ballpark` (`ballparkID`),
  CONSTRAINT `fk_team_season`
    FOREIGN KEY (`seasonID`)
    REFERENCES `baseball`.`season` (`seasonID`))
ENGINE = InnoDB
AUTO_INCREMENT = 61
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`coach`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`coach` (
  `coachID` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(45) NULL DEFAULT NULL,
  `lastName` VARCHAR(45) NULL DEFAULT NULL,
  `teamID` INT NULL DEFAULT NULL,
  PRIMARY KEY (`coachID`),
  INDEX `fk_coach_team_idx` (`teamID` ASC) VISIBLE,
  CONSTRAINT `fk_coach_team`
    FOREIGN KEY (`teamID`)
    REFERENCES `baseball`.`team` (`teamID`))
ENGINE = InnoDB
AUTO_INCREMENT = 31
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`game`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`game` (
  `gameID` INT NOT NULL AUTO_INCREMENT,
  `gameDate` DATETIME NULL DEFAULT NULL,
  `homeTeamID` INT NULL DEFAULT NULL,
  `awayTeamID` INT NULL DEFAULT NULL,
  `homeTeamScore` INT NULL DEFAULT NULL,
  `awayTeamScore` INT NULL DEFAULT NULL,
  `ballparkID` INT NULL DEFAULT NULL,
  `seasonID` INT NULL DEFAULT NULL,
  PRIMARY KEY (`gameID`),
  INDEX `fk_game_homeTeam_idx` (`homeTeamID` ASC) VISIBLE,
  INDEX `fk_game_awayTeam_idx` (`awayTeamID` ASC) VISIBLE,
  INDEX `fk_game_ballpark_idx` (`ballparkID` ASC) VISIBLE,
  INDEX `fk_game_season_idx` (`seasonID` ASC) VISIBLE,
  CONSTRAINT `fk_game_awayTeam`
    FOREIGN KEY (`awayTeamID`)
    REFERENCES `baseball`.`team` (`teamID`),
  CONSTRAINT `fk_game_ballpark`
    FOREIGN KEY (`ballparkID`)
    REFERENCES `baseball`.`ballpark` (`ballparkID`),
  CONSTRAINT `fk_game_homeTeam`
    FOREIGN KEY (`homeTeamID`)
    REFERENCES `baseball`.`team` (`teamID`),
  CONSTRAINT `fk_game_season`
    FOREIGN KEY (`seasonID`)
    REFERENCES `baseball`.`season` (`seasonID`))
ENGINE = InnoDB
AUTO_INCREMENT = 101
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`concessionSale`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`concessionSale` (
  `concessionSaleID` INT NOT NULL AUTO_INCREMENT,
  `gameID` INT NULL DEFAULT NULL,
  `itemName` VARCHAR(100) NULL DEFAULT NULL,
  `quantitySold` INT NULL DEFAULT NULL,
  `pricePerItem` DECIMAL(6,2) NULL DEFAULT NULL,
  PRIMARY KEY (`concessionSaleID`),
  INDEX `idx_concessionSale_game` (`gameID` ASC) VISIBLE,
  CONSTRAINT `fk_concessionSale_game`
    FOREIGN KEY (`gameID`)
    REFERENCES `baseball`.`game` (`gameID`))
ENGINE = InnoDB
AUTO_INCREMENT = 39
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `baseball`.`umpire`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`umpire` (
  `umpireID` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(45) NULL DEFAULT NULL,
  `lastName` VARCHAR(45) NULL DEFAULT NULL,
  `yearsExperience` INT NULL DEFAULT NULL,
  PRIMARY KEY (`umpireID`))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`gameUmpire`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`gameUmpire` (
  `gameUmpireID` INT NOT NULL AUTO_INCREMENT,
  `gameID` INT NULL DEFAULT NULL,
  `umpireID` INT NULL DEFAULT NULL,
  `role` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`gameUmpireID`),
  INDEX `fk_gameUmpire_game_idx` (`gameID` ASC) VISIBLE,
  INDEX `fk_gameUmpire_umpire_idx` (`umpireID` ASC) VISIBLE,
  CONSTRAINT `fk_gameUmpire_game`
    FOREIGN KEY (`gameID`)
    REFERENCES `baseball`.`game` (`gameID`),
  CONSTRAINT `fk_gameUmpire_umpire`
    FOREIGN KEY (`umpireID`)
    REFERENCES `baseball`.`umpire` (`umpireID`))
ENGINE = InnoDB
AUTO_INCREMENT = 301
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`player` (
  `playerID` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(45) NULL DEFAULT NULL,
  `lastName` VARCHAR(45) NULL DEFAULT NULL,
  `position` VARCHAR(45) NULL DEFAULT NULL,
  `teamID` INT NULL DEFAULT NULL,
  PRIMARY KEY (`playerID`),
  INDEX `fk_player_team_idx` (`teamID` ASC) VISIBLE,
  CONSTRAINT `fk_player_team`
    FOREIGN KEY (`teamID`)
    REFERENCES `baseball`.`team` (`teamID`))
ENGINE = InnoDB
AUTO_INCREMENT = 201
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`injury`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`injury` (
  `injuryID` INT NOT NULL AUTO_INCREMENT,
  `playerID` INT NULL DEFAULT NULL,
  `injuryDescription` VARCHAR(100) NULL DEFAULT NULL,
  `startDate` DATE NULL DEFAULT NULL,
  `endDate` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`injuryID`),
  INDEX `idx_injury_player` (`playerID` ASC) VISIBLE,
  CONSTRAINT `fk_injury_player`
    FOREIGN KEY (`playerID`)
    REFERENCES `baseball`.`player` (`playerID`))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `baseball`.`playerGameStats`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`playerGameStats` (
  `statID` INT NOT NULL AUTO_INCREMENT,
  `gameID` INT NULL DEFAULT NULL,
  `playerID` INT NULL DEFAULT NULL,
  `atBats` INT NULL DEFAULT NULL,
  `hits` INT NULL DEFAULT NULL,
  `homeRuns` INT NULL DEFAULT NULL,
  `rbis` INT NULL DEFAULT NULL,
  PRIMARY KEY (`statID`),
  INDEX `idx_playerGameStats_game` (`gameID` ASC) VISIBLE,
  INDEX `idx_playerGameStats_player` (`playerID` ASC) VISIBLE,
  CONSTRAINT `fk_playerGameStats_game`
    FOREIGN KEY (`gameID`)
    REFERENCES `baseball`.`game` (`gameID`),
  CONSTRAINT `fk_playerGameStats_player`
    FOREIGN KEY (`playerID`)
    REFERENCES `baseball`.`player` (`playerID`))
ENGINE = InnoDB
AUTO_INCREMENT = 256
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `baseball`.`sponsor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`sponsor` (
  `sponsorID` INT NOT NULL AUTO_INCREMENT,
  `sponsorName` VARCHAR(50) NULL DEFAULT NULL,
  `industry` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`sponsorID`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`teamSponsor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`teamSponsor` (
  `teamSponsorID` INT NOT NULL AUTO_INCREMENT,
  `teamID` INT NULL DEFAULT NULL,
  `sponsorID` INT NULL DEFAULT NULL,
  `sponsorshipAmount` DECIMAL(10,2) NULL DEFAULT NULL,
  PRIMARY KEY (`teamSponsorID`),
  INDEX `fk_teamSponsor_team_idx` (`teamID` ASC) VISIBLE,
  INDEX `fk_teamSponsor_sponsor_idx` (`sponsorID` ASC) VISIBLE,
  CONSTRAINT `fk_teamSponsor_sponsor`
    FOREIGN KEY (`sponsorID`)
    REFERENCES `baseball`.`sponsor` (`sponsorID`),
  CONSTRAINT `fk_teamSponsor_team`
    FOREIGN KEY (`teamID`)
    REFERENCES `baseball`.`team` (`teamID`))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `baseball`.`ticketSale`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `baseball`.`ticketSale` (
  `ticketSaleID` INT NOT NULL AUTO_INCREMENT,
  `gameID` INT NULL DEFAULT NULL,
  `ticketType` VARCHAR(45) NULL DEFAULT NULL,
  `ticketsSold` INT NULL DEFAULT NULL,
  `pricePerTicket` DECIMAL(6,2) NULL DEFAULT NULL,
  PRIMARY KEY (`ticketSaleID`),
  INDEX `idx_ticketSale_game` (`gameID` ASC) VISIBLE,
  CONSTRAINT `fk_ticketSale_game`
    FOREIGN KEY (`gameID`)
    REFERENCES `baseball`.`game` (`gameID`))
ENGINE = InnoDB
AUTO_INCREMENT = 39
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
