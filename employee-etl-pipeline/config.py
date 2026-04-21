import os
from dotenv import load_dotenv

# Get the absolute path to the directory containing config.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Load environment variables explicitly from the .env file in the root directory
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Database configuration parameters
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "company_db")

# SQLAlchemy connection string
DB_URL = os.getenv("DB_URL", f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
