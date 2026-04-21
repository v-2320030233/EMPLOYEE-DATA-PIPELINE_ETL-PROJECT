import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

def extract_data(file_path):
    """
    Reads the CSV file using Pandas and displays basic info.
    """
    logger.info(f"Extracting data from {file_path}")
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    df = pd.read_csv(file_path)
    
    logger.info(f"Data Shape (Rows, Columns): {df.shape}")
    logger.info(f"Null Counts per Column:\n{df.isnull().sum()}")
    
    return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "employees.csv")
    extracted_df = extract_data(data_path)
