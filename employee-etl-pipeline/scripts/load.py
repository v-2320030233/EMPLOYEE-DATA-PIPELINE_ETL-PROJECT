import pandas as pd
from sqlalchemy import create_engine
import os
import sys
import logging

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

logger = logging.getLogger(__name__)

def load_data(df, table_name="employees"):
    """
    Connects to MySQL using SQLAlchemy and loads the cleaned DataFrame.
    """
    logger.info(f"Loading data into MySQL table '{table_name}'")
    
    try:
        # Create SQLAlchemy engine
        engine = create_engine(config.DB_URL)
        
        # Load data to SQL, replace table if it already exists
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        
        logger.info(f"[SUCCESS] Successfully loaded {df.shape[0]} rows into '{table_name}' table.")
        
    except Exception as e:
        logger.error(f"Failed to load data to database: {e}")
        logger.info("Ensure your MySQL server is running and credentials in config.py or .env are correct.")

if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data
    logging.basicConfig(level=logging.INFO)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "employees.csv")
    
    raw_df = extract_data(data_path)
    clean_df = transform_data(raw_df)
    load_data(clean_df)
