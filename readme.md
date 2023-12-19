# ETL Project: GitHub Data Extraction and Loading to Azure Synapse Analytics Dedicated SQL Pool

## Overview

This ETL (Extract, Transform, Load) project is implemented in a Jupyter Notebook (`ETL.ipynb`). It extracts data from a GitHub repository in CSV and JSON formats, applies necessary transformations based on business logic, stores the transformed data into an Azure Blob Storage file (CSV format), and then uses a 'COPY INTO' SQL statement to load the file into a stage table. Finally, a stored procedure is executed to load the data from the stage table to a table in a schema accessible to end users. The database used for this project is Azure Synapse Analytics Dedicated SQL Pool

## Workflow

1. **Data Extraction:**
    - Data is extracted from a GitHub repository in CSV and JSON formats.

2. **Transformation:**
    - The extracted data undergoes transformations according to predefined business logic.

3. **Azure Blob Storage:**
    - The transformed data is stored in an Azure Blob Storage file in CSV format.

4. **SQL Loading:**
    - The 'COPY INTO' SQL statement is used to load the CSV file into a stage table in ASA Dedicated SQL Pool.

5. **Stored Procedure Execution:**
    - stored procedures were executed to load the data to & from the stage table to a table in a schema accessible to end users.

## Prerequisites

Before running the Jupyter Notebook, ensure you have the following:

- An Azure Synapse Analytics Workspace with contributor access and db_write priviledges.
- Azure Blob Storage account credentials.
- Python environment with necessary libraries installed (check requirements.txt).

## Project Structure

```plaintext
ETL-Project/
|-- ETL.ipynb
|-- queries/
|   |-- create_tables.sql
|   |-- sp_truncate_load_customers.sql
|-- functions/
|   |-- azure_blob_uploader.py
|   |-- error_messages.py
|   |-- github_connector.py
|   |-- mail_sender.py
|   |-- sql_connector.py
|-- README.md
|-- requirements.txt
```

# Usage
## Clone the repository:
```bash
    git clone https://github.com/DamilolaAdeniji/GITHUB-SYNAPSE-ETL-PROJECT.git
    cd ETL-Project
```

## Install the required Python libraries:
``` python
    pip install -r requirements.txt
```