CREATE DATABASE `XXXChange`;

USE `XXXChange`;

-- Table to track daily activiy
-- may be future modifications will be
-- taken to modify the attributes
CREATE TABLE `daily_tracking`
(
    `id` SERIAL COMMENT 'ID',
    `day` DATE NOT NULL COMMENT 'Date',
    `wakeup_time` TIME NOT NULL COMMENT 'The time got up in the morning',
    `sleepy_time` TIME NOT NULL COMMENT 'The time went to sleep',
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