import os
import logging
from extract import extract_data
from transform import transform_data
from load import load_data

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("="*50)
    logger.info("🚀 Starting Data Engineering ETL Pipeline")
    logger.info("="*50)
    
    # Define data path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "employees.csv")
    
    # Step 1: Extract
    logger.info(">>> STEP 1: EXTRACT")
    raw_df = extract_data(data_path)
    
    # Step 2: Transform
    logger.info(">>> STEP 2: TRANSFORM")
    clean_df = transform_data(raw_df)
    
    # Step 3: Load
    logger.info(">>> STEP 3: LOAD")
    load_data(clean_df)
    
    logger.info("="*50)
    logger.info("✅ ETL Pipeline Completed Successfully!")
    logger.info("="*50)

if __name__ == "__main__":
    run_pipeline()
