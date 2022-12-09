CREATE DATABASE `XXXChange`;

-- Table of tracking daily activiy
-- may be future modifications will be
-- taken to modify the attributes
CREATE TABLE `daily_tracking`
(
    `id` SERIAL COMMENT 'ID',
    `day` DATE COMMENT 'DATE',
    `wakeup_time` TIME COMMENT 'The time wake up',
    `sleepy_time` TIME COMMENT 'The time went to sleep',
    `created_at` DATETIME NOT NULL,
    `created_by` VARCHAR(45) DEFUALT 'system',
    `updated_at` DATETIME NOT NULL,
    `updated_by` VARCHAR(45) DEFUALT 'system',
    `deleated_at` DATETIME NOT NULL,
    deleated_by VARCHAR(45) DEFUALT 'system',
    PRIMARY KEY (`id`)
);
