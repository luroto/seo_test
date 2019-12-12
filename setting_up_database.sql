-- Script for creating users, password and database 
CREATE USER 'bunny_test_user'@'localhost' IDENTIFIED BY 'bunny_test_pwd';
CREATE DATABASE IF NOT EXISTS bunny_test;
GRANT ALL PRIVILEGES ON bunny_test.* TO 'bunny_test_user'@'localhost';
