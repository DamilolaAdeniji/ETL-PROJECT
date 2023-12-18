CREATE SCHEMA stage;
GO

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'stage.customers')
BEGIN
CREATE TABLE stage.customers (
    id varchar(25),
    first_name varchar(255),
    last_name varchar(255),
    email varchar(255),
    gender varchar(25),
    phone varchar(255),
    dateloaded datetime -- to enable us know how updated the data is
);
END;
GO

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'dbo.dimcustomers')
BEGIN
CREATE TABLE dbo.dimcustomers (
    id varchar(25),
    first_name varchar(255),
    last_name varchar(255),
    email varchar(255),
    gender varchar(25),
    phone varchar(255),
    dateloaded datetime -- to enable us know how updated the data is
);
END;

GO