CREATE PROCEDURE sp_truncate_load_customers
AS BEGIN
    BEGIN TRY
        BEGIN TRANSACTION
        TRUNCATE TABLE dbo.dimcustomers

        INSERT INTO dbo.dimcustomers
        SELECT * FROM stage.customers

        COMMIT
    END TRY
    BEGIN CATCH
        ROLLBACK;
        PRINT ERROR_MESSAGE();
    END CATCH
END;