import pandas as pd
from sqlalchemy import create_engine

# Google Drive file ID

url = f'https://drive.google.com/file/d/1asq7yzvFpkmDUMZQtK7AJ16_XZbQCZmc/view'


# Download the file and save it as 5k_borrowers_data.csv
output = '5k_borrowers_data.csv'
gdown.download(url, output, quiet=False)

# Load the CSV file into a DataFrame
5k_borrowers_data = pd.read_csv(output)
# Load the cleaned CSV file into a DataFrame
file_path = 'cleaned_5k_borrowers_data.csv'
borrowers_data = pd.read_csv(file_path)

# Database connection details
db_user = 'username'
db_password = 'password'
db_host = 'localhost'
db_name = 'borrowers_db'
# Replace the username and password with your username and password for MySQL Connection

# Connecting to MySQL
connection = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'

# Create a database editor
engine = create_engine(connection_string)

# Define the table schema in SQL
create_table_query = """
CREATE TABLE IF NOT EXISTS borrowers (
    name VARCHAR(255),
    date_of_birth DATE,
    gender VARCHAR(50),
    marital_status VARCHAR(50),
    phone_number VARCHAR(50),
    email_address VARCHAR(255),
    mailing_address TEXT,
    language_preference VARCHAR(50),
    geographical_location VARCHAR(255),
    credit_score INT,
    loan_amount FLOAT,
    loan_term INT,
    interest_rate FLOAT,
    loan_purpose VARCHAR(255),
    emi FLOAT,
    ip_address VARCHAR(50),
    geolocation VARCHAR(255),
    repayment_history TEXT,
    days_left_to_pay_current_emi INT,
    delayed_payment VARCHAR(50)
);
"""

# Execute the table creation query
with engine.connect() as connection:
    connection.execute(create_table_query)

# Load the DataFrame into the MySQL table
borrowers_data.to_sql('borrowers', con=engine, if_exists='replace', index=False)

print("Data loaded successfully into the 'borrowers' table.")
