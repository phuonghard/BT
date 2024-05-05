CREATE DATABASE PHUONGHARD;
USE PHUONGHARD;
CREATE TABLE Department (
DepartmentID				INT AUTO_INCREMENT PRIMARY KEY,
DepartmentName				VARCHAR(50)
);
CREATE TABLE Position (
PositionID 					INT AUTO_INCREMENT PRIMARY KEY,
PositionNam					VARCHAR(50)
);	
CREATE TABLE Account (
AccountID					INT AUTO_INCREMENT PRIMARY KEY,
Email						VARCHAR(50),
Username					VARCHAR(100),
Fullname					VARCHAR(100),
DepartmentID				VARCHAR(50),
PositionID					VARCHAR(50),
CreateDate					DATE
);
CREATE TABLE Group1 (
GroupID						INT AUTO_INCREMENT PRIMARY KEY,
GroupName					VARCHAR(50),
CreatorID					VARCHAR(50),
CreateDate					DATE
);
CREATE TABLE GroupAccount (
GroupID						VARCHAR(50),
AccountID					VARCHAR(50),
JoinDate					VARCHAR(50)
);
CREATE	TABLE TypeQuestion (
TypeID					INT AUTO_INCREMENT PRIMARY KEY,
TypeName				VARCHAR(50)
);
CREATE	TABLE CategoryQuestion (
CategoryID					INT AUTO_INCREMENT PRIMARY KEY,
CategoryName				VARCHAR(50)
);
CREATE	TABLE Question (
QuestionID					INT AUTO_INCREMENT PRIMARY KEY,
Content						VARCHAR(50),
CategoryID					VARCHAR(50),
TypeID						VARCHAR(50),
CreatorID					VARCHAR(50),
CreateDate					Date
);
CREATE	TABLE Answer (
AnswerID					INT AUTO_INCREMENT PRIMARY KEY,
Content						VARCHAR(50),
QuestionID					VARCHAR(50),
isCorrect					BOOLEAN
);
CREATE	TABLE Exam (
ExamID					INT AUTO_INCREMENT PRIMARY KEY,
Code					VARCHAR(50),
Title					VARCHAR(50),
CategoryID				VARCHAR(50),
Duration				VARCHAR(50),
CreatorID				VARCHAR(50),
CreateDate				DATE
);
