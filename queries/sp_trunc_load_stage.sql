DECLARE @file_url NVARCHAR(255);
SET @file_url = 'https://{insert_account_name}.blob.core.windows.net/{insert_container_name}/all_customers.csv';


CREATE PROCEDURE sp_trunc_load_stage
AS BEGIN
    BEGIN TRY
    
        BEGIN TRANSACTION
        DROP TABLE stage.customers

        CREATE TABLE stage.customers (
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
            DISTRIBUTION = ROUND_ROBIN  
        )
        
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