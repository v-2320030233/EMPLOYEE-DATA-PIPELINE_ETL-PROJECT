# Employee ETL Pipeline

This is an end-to-end Data Engineering ETL (Extract, Transform, Load) pipeline in Python that processes employee data. It extracts raw data from a CSV, cleans it using Pandas, and loads it into a MySQL database.

## Project Structure
```text
employee-etl-pipeline/
├── data/
│   └── employees.csv           # Raw sample data with intentional issues
├── scripts/
│   ├── extract.py              # Loads CSV and displays info
│   ├── transform.py            # Cleans and transforms the data
│   ├── load.py                 # Loads cleaned data to MySQL
│   └── pipeline.py             # Master script running extract -> transform -> load
├── notebooks/
│   └── ETL_Pipeline.ipynb      # Step-by-step Jupyter Notebook walkthrough
├── sql/
│   └── queries.sql             # SQL queries for extracting business insights
├── config.py                   # Database connection credentials
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Prerequisites
- Python 3.7+
- MySQL Server running locally or remotely

## Setup Instructions

1. **Install Dependencies**
   Navigate to the project root and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Database**
   - Ensure your MySQL server is running.
   - Create a database in MySQL (e.g., `company_db`).
   - Edit the `config.py` file to set your database credentials (`DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`).

3. **Run the ETL Pipeline**
   You can run the entire pipeline at once using the master script:
   ```bash
   python scripts/pipeline.py
   ```
   Alternatively, you can run each step independently:
   ```bash
   python scripts/extract.py
   python scripts/transform.py
   python scripts/load.py
   ```

4. **Explore the Notebook**
   To see a step-by-step interactive walkthrough, launch Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/ETL_Pipeline.ipynb
   ```

5. **Run SQL Queries**
   After loading the data, you can connect to your MySQL database and run the queries found in `sql/queries.sql` to answer business questions.
