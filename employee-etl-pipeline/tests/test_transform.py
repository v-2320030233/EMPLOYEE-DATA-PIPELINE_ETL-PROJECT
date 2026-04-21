import pandas as pd
import pytest
import sys
import os

# Add scripts directory to path to import transform
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
from transform import transform_data

def test_transform_data_drops_duplicates():
    data = {
        'Employee ID': [1, 1],
        'Name': ['Alice', 'Alice'],
        'Department': ['IT', 'IT'],
        'Salary': ['50000', '50000'],
        'Join Date': ['2020-01-01', '2020-01-01'],
        'Email': ['alice@test.com', 'alice@test.com'],
        'Age': [30, 30]
    }
    df = pd.DataFrame(data)
    clean_df = transform_data(df)
    assert len(clean_df) == 1

def test_transform_data_handles_negative_salary():
    data = {
        'Employee ID': [1, 2],
        'Name': ['Alice', 'Bob'],
        'Department': ['IT', 'HR'],
        'Salary': ['50000', '-60000'],
        'Join Date': ['2020-01-01', '2020-01-02'],
        'Email': ['alice@test.com', 'bob@test.com'],
        'Age': [30, 40]
    }
    df = pd.DataFrame(data)
    clean_df = transform_data(df)
    assert len(clean_df) == 1
    assert clean_df.iloc[0]['name'] == 'Alice'

def test_transform_data_standardizes_columns():
    data = {
        'Employee ID': [1],
        'Name': ['Alice'],
        'Department': ['IT'],
        'Salary': ['50000'],
        'Join Date': ['2020-01-01'],
        'Email': ['alice@test.com'],
        'Age': [30]
    }
    df = pd.DataFrame(data)
    clean_df = transform_data(df)
    expected_cols = ['employee_id', 'name', 'department', 'salary', 'join_date', 'email', 'age']
    assert list(clean_df.columns) == expected_cols
