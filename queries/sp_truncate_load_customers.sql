CREATE PROCEDURE sp_truncate_load_customers
AS BEGIN
    BEGIN TRY
        BEGIN TRANSACTION
        DROP TABLE dbo.dimcustomers

        CREATE TABLE dbo.dimcustomers (
        id varchar(25),
        first_name varchar(255),
        last_name varchar(255),
        email varchar(255),
        gender varchar(25),
        phone varchar(255),
        dateloaded datetime)
        WITH
        (
            HEAP,  
            DISTRIBUTION = REPLICATE  
        )
        INSERT INTO dbo.dimcustomers
        SELECT * FROM stage.customers
-- GRANT SELECT ON dbo.dimcustomers TO dammy
        COMMIT
    END TRY
    BEGIN CATCH
        ROLLBACK;
        PRINT ERROR_MESSAGE();
    END CATCH
END;