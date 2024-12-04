CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS operations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number1 INT NOT NULL,
    number2 INT NOT NULL,
    result INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);