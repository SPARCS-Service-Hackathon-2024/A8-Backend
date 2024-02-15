import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root", # 사용자 이름
    password="password", # 비밀번호
    database="2024SparcsHackathon" # 데이터베이스 이름
)

ddl = """
-- DDL for Stations Table
CREATE TABLE `Stations` (
    `station_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `latitude` DOUBLE,
    `longitude` DOUBLE
);

-- DDL for Routes Table
CREATE TABLE `Routes` (
    `route_id` INT PRIMARY KEY,
    `name` TEXT
);
-- DDL for Chats Table
-- DDL for Activities Table
-- DDL for Users Table
CREATE TABLE `Users` (
    `user_id` INT PRIMARY KEY,
    `email` VARCHAR(40),
    `nickname` VARCHAR(20),
    `gender` INT, -- Assuming gender is stored as an integer, adjust if it's an ENUM.
    `want_gender` INT, -- Same assumption as gender.
    `address` VARCHAR(100) -- This is partially visible, assuming it's VARCHAR.
);

CREATE TABLE `Activities` (
    `activity_id` INT PRIMARY KEY,
    `user_id` INT,
    `title` VARCHAR(20),
    `intro` VARCHAR(30),
    `time` DATETIME,
    `duration` INT,
    `station_id` INT,
    `address` VARCHAR(100),
    `latitude` DOUBLE,
    `longitude` DOUBLE,
    FOREIGN KEY (`user_id`) REFERENCES `Users`(`user_id`)
);

-- DDL for Chatrooms Table
CREATE TABLE `Chatrooms` (
    `chatroom_id` INT PRIMARY KEY,
    `host_id` INT,
    `guest_id` INT,
    `activity_id` INT,
    `lock` BOOLEAN,
    FOREIGN KEY (`host_id`) REFERENCES `Users`(`user_id`),
    FOREIGN KEY (`guest_id`) REFERENCES `Users`(`user_id`),
    FOREIGN KEY (`activity_id`) REFERENCES `Activities`(`activity_id`)
);

CREATE TABLE `Chats` (
    `chat_id` INT PRIMARY KEY,
    `sen_id` INT,
    `rec_id` INT,
    `chat_time` DATETIME,
    `text` VARCHAR(255), -- Assuming the text length, adjust if needed.
    `love` BOOLEAN,
    `chatroom_id` INT,
    FOREIGN KEY (`chatroom_id`) REFERENCES `Chatrooms`(`chatroom_id`)
);

-- DDL for Relation_Routes_Stations Table
CREATE TABLE `Relation_Routes_Stations` (
    `route_id` INT,
    `station_id` INT,
    `number` INT,
    PRIMARY KEY (`route_id`, `station_id`),
    FOREIGN KEY (`route_id`) REFERENCES `Routes`(`route_id`),
    FOREIGN KEY (`station_id`) REFERENCES `Stations`(`station_id`)
);
"""

cursor = conn.cursor()

cursor.execute(ddl)

# 변경 사항 커밋
conn.commit()

# 연결 종료
conn.close()