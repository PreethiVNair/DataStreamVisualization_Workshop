import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd


class Database:

    def __init__(self):
        # Load variables from .env
        load_dotenv()

        # Get the Neon database URL
        self.database_url = os.getenv("DATABASE_URL")

        # Connect to the database
        self.connection = psycopg2.connect(self.database_url)

        # Create a cursor
        self.cursor = self.connection.cursor()

        # Name of the database table
        self.table_name = "robot_data"

    def createTable(self, data_point):

        # Get the column names from the incoming data
        columns = data_point.columns

        # Build the SQL columns dynamically
        sql_columns = []

        for column in columns:

            # Convert column name into a safe database column name
            safe_column = column.lower().replace(" ", "_").replace("#", "")

            # Use TEXT for now
            sql_columns.append(f'"{safe_column}" TEXT')

        # Create the table
        query = f"""
            CREATE TABLE IF NOT EXISTS robot_data (
                id SERIAL PRIMARY KEY,
                {", ".join(sql_columns)}
            )
        """

        self.cursor.execute(query)

        # Save the changes
        self.connection.commit()

    def insertDataPoint(self, data_point):

        # Get the column names
        columns = data_point.columns

        # Convert column names to database column names
        safe_columns = []

        for column in columns:
            safe_column = column.lower().replace(" ", "_").replace("#", "")
            safe_columns.append(safe_column)

        # Get the values from the first row
        values = data_point.iloc[0].tolist()

        # Convert pandas/NumPy values to normal Python values
        converted_values = []

        for value in values:

            # Convert NaN to None
            if pd.isna(value):
                converted_values.append(None)

            # Convert NumPy values to Python values
            else:
                converted_values.append(
                    value.item() if hasattr(value, "item") else value
                )

        values = converted_values

        # Create placeholders for the values
        placeholders = ", ".join(["%s"] * len(values))

        # Create the INSERT query
        query = f"""
            INSERT INTO robot_data ({", ".join(safe_columns)})
            VALUES ({placeholders})
        """

        # Insert the data
        self.cursor.execute(query, values)

        # Save the changes
        self.connection.commit()

    def fetch_all(self):
        return pd.read_sql(
            f"SELECT * FROM {self.table_name}",
            self.connection
        )

    def fetch_latest(self, n=50):
        return pd.read_sql(
            f"SELECT * FROM {self.table_name} "
            f"ORDER BY id DESC LIMIT {n}",
            self.connection
        ).iloc[::-1]

    
    def insertBulkData(self, data):

        columns = data.columns

        # Convert column names to database column names
        safe_columns = []

        for column in columns:
            safe_column = column.lower().replace(" ", "_").replace("#", "")
            safe_columns.append(safe_column)

        # Convert the DataFrame to normal Python values
        records = []

        for _, row in data.iterrows():

            values = []

            for value in row.tolist():

                if pd.isna(value):
                    values.append(None)
                else:
                    values.append(
                        value.item() if hasattr(value, "item") else value
                    )

            records.append(tuple(values))

        placeholders = ", ".join(["%s"] * len(columns))

        query = f"""
            INSERT INTO robot_data ({", ".join(safe_columns)})
            VALUES ({placeholders})
        """

        # Insert records in batches
        batch_size = 500

        for i in range(0, len(records), batch_size):

            batch = records[i:i + batch_size]

            self.cursor.executemany(query, batch)

            self.connection.commit()

            print(f"{min(i + batch_size, len(records))} records inserted...")

        print("Bulk insertion completed.")
        print("Total records inserted:", len(data))

