import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_data(df):
    """
    Cleans and transforms the raw employee DataFrame.
    """
    logger.info("Starting Data Transformation")
    
    # 1. Standardize column names to lowercase with underscores
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    logger.info(f"Standardized column names: {df.columns.tolist()}")
    
    # 2. Drop duplicate rows
    initial_shape = df.shape
    df = df.drop_duplicates()
    logger.info(f"Dropped duplicates. Rows went from {initial_shape[0]} to {df.shape[0]}.")
    
    # 3. Handle null values
    df['department'] = df.apply(lambda row: 'Unknown' if pd.isna(row['department']) else row['department'], axis=1)
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    median_age = df['age'].median()
    df['age'] = df['age'].fillna(median_age).astype(int)
    logger.info("Handled null values for department and age.")
    
    # 4. Ensure salary is numeric and filter invalid records
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df = df.dropna(subset=['salary'])
    df = df[df['salary'] > 0]
    df['salary'] = df['salary'].astype(int)
    logger.info(f"Cleaned salary column. Valid rows remaining: {df.shape[0]}.")
    
    # 5. Convert join_date to proper datetime format
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
    df = df.dropna(subset=['join_date'])
    logger.info("Converted join_date to datetime.")
    
    logger.info(f"Final Transformed Data Shape: {df.shape}")
    
    return df

if __name__ == "__main__":
    from extract import extract_data
    import os
    logging.basicConfig(level=logging.INFO)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "employees.csv")
    raw_df = extract_data(data_path)
    clean_df = transform_data(raw_df)
