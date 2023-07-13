import pyodbc

# Define connection string
conn_str = (
    r"Driver={SQL Server Native Client 11.0};"
    r"Server=SERVER_NAME;"
    r"Database=DATABASE_NAME;"
    r"UID=USERNAME;"
    r"PWD=PASSWORD;"
)

# Establish connection and create cursor
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Execute SQL query and fetch results
cursor.execute("SELECT * FROM TABLE_NAME")
results = cursor.fetchall()

# Do something with results, such as convert to pandas DataFrame
import pandas as pd
df = pd.DataFrame(results)

# Close cursor and connection
cursor.close()
conn.close()