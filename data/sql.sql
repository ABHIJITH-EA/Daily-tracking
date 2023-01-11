CREATE DATABASE `XXXChange`;

USE `XXXChange`;

-- Table to track daily activiy
-- may be future modifications will be
-- taken to modify the attributes
CREATE TABLE `daily_tracking`
(
    `id` SERIAL COMMENT 'ID',
    `day` DATE NOT NULL UNIQUE COMMENT 'Date',
    `wakeup_time` TIME NOT NULL COMMENT 'The time got up in the morning',
    `sleepy_time` DATETIME NOT NULL COMMENT 'The time went to sleep',
    `created_at` DATETIME NOT NULL,
    `created_by` VARCHAR(45) DEFAULT 'system',
    `updated_at` DATETIME NOT NULL,
    `updated_by` VARCHAR(45) DEFAULT 'system',
    `deleated_at` DATETIME,
    `deleated_by` VARCHAR(45),
    PRIMARY KEY (`id`)
);

-- Table for buggeting
CREATE TABLE `budget_tracking`
(
    `id` SERIAL COMMENT 'ID',
    `day` DATE NOT NULL COMMENT 'Date',
    `created_at` DATETIME NOT NULL,
    `created_by` VARCHAR(45) DEFAULT 'system',
    `updated_at` DATETIME NOT NULL,
    `updated_by` VARCHAR(45) DEFAULT 'system',
    `deleated_at` DATETIME,
    `deleated_by` VARCHAR(45),
    PRIMARY KEY (`id`)
);

CREATE TABLE `spent`
(
    `id` SERIAL COMMENT 'ID of each spent occured',
    `budgeting_id` BIGINT UNSIGNED,
    `amount` INT NOT NULL DEFAULT 0,
    `remarks` VARCHAR(255),
    `created_at` DATETIME NOT NULL,
    `created_by` VARCHAR(45) DEFAULT 'system',
    `updated_at` DATETIME NOT NULL,
    `updated_by` VARCHAR(45) DEFAULT 'system',
    `deleated_at` DATETIME,
    `deleated_by` VARCHAR(45),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`budgeting_id`) REFERENCES `budget_tracking`(`id`)
);

CREATE TABLE `income`
(
    `id` SERIAL COMMENT 'ID of income',
    `budgeting_id` BIGINT UNSIGNED,
    `amount` INT NOT NULL DEFAULT 0,
    `remarks` VARCHAR(255),
    `created_at` DATETIME NOT NULL,
    `created_by` VARCHAR(45) DEFAULT 'system',
    `updated_at` DATETIME NOT NULL,
    `updated_by` VARCHAR(45) DEFAULT 'system',
    `deleated_at` DATETIME,
    `deleated_by` VARCHAR(45),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`budgeting_id`) REFERENCES `budget_tracking`(`id`)
);

-- Planner table's
-- There will be week planner table and
-- month planner table

-- Table for month planning
CREATE TABLE `month_plan`
(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE COMMENT 'primary key',
    `start_date` DATE NOT NULL COMMENT 'Start date of the month planned actions',
    `end_date` DATE NOT NULL COMMENT 'End date of the month planned actions',
    `goal` VARCHAR(512) NOT NULL COMMENT 'Goals of the month',
    `status` ENUM('INPROGRESS', 'SUCCESS', 'FAILED') NOT NULL,
    `created_at` DATETIME NOT NULL,
    `created_by` VARCHAR(45) DEFAULT 'system',
    `updated_at` DATETIME NOT NULL,
    `updated_by` VARCHAR(45) DEFAULT 'system',
    `deleated_at` DATETIME,
    `deleated_by` VARCHAR(45),
    PRIMARY KEY (`id`)
);

-- Table for week planning
CREATE TABLE `week_plan`
(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE COMMENT 'primary key',
    `month_id` INT UNSIGNED,
    `start_date` DATE NOT NULL COMMENT 'Start date of the week planned actions',
    `end_date` DATE NOT NULL COMMENT 'End date of the week planned actions',
    `goal` VARCHAR(512) NOT NULL COMMENT 'Goals of the week',
    `status` ENUM('INPROGRESS', 'SUCCESS', 'FAILED') NOT NULL COMMENT 'Status of goal achieving',
    `created_at` DATETIME NOT NULL,
    `created_by` VARCHAR(45) DEFAULT 'system',
    `updated_at` DATETIME NOT NULL,
    `updated_by` VARCHAR(45) DEFAULT 'system',
    `deleated_at` DATETIME,
    `deleated_by` VARCHAR(45),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`month_id`) REFERENCES `month_plan`(`id`)
);