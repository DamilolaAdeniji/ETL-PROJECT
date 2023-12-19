DECLARE @file_url NVARCHAR(255);
SET @file_url = 'https://{insert_account_name}.blob.core.windows.net/{insert_container_name}/all_customers.csv';


CREATE PROCEDURE sp_trunc_load_stage
AS BEGIN
    BEGIN TRY
    
        BEGIN TRANSACTION
        TRUNCATE TABLE stage.customers
        COPY INTO stage.customers
        FROM @file_url
        WITH (FILE_TYPE = 'CSV',
        MAXERRORS = 0,
        FIRSTROW = 2,
        PARSER_VERSION = '2.0');

        COMMIT
    END TRY
    BEGIN CATCH
        ROLLBACK;
        PRINT ERROR_MESSAGE();
    END CATCH
END;