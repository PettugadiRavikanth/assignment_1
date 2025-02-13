import streamlit as st
import pandas as pd
import mysql.connector

# Establish MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="SQLPYTHON1"
    )

# Function to execute a selected SQL query
def execute_query(query):
    connection = get_connection()
    try:
        df = pd.read_sql(query, connection)
        connection.close()
        return df
    except Exception as e:
        st.error(f" Error: {e}")
        return None

# Streamlit App
st.title("MySQL Query Explorer")

# List of SQL Queries
queries = {
    "1️. View All Transactions": "SELECT * FROM all_months_exp1 LIMIT 2000",
    "2️. Total Amount Spent": "SELECT SUM(Amount_paid) AS Total_Spent FROM all_months_exp1",
    "3️. Average Expense Amount": "SELECT AVG(Amount_paid) AS Average_Spent FROM all_months_exp1",
    "4️. Count Transactions by Category": "SELECT Categories, COUNT(*) AS Count FROM all_months_exp1 GROUP BY Categories",
    "5️. Total Amount Spent by Category": "SELECT Categories, SUM(Amount_paid) AS Total FROM all_months_exp1 GROUP BY Categories",
    "6️. Highest Expense Transaction": "SELECT * FROM all_months_exp1 ORDER BY Amount_paid DESC LIMIT 1",
    "7️. Lowest Expense Transaction": "SELECT * FROM all_months_exp1 ORDER BY Amount_paid ASC LIMIT 1",
    "8️. Count Transactions by Payment Mode": "SELECT Payment_Mode, COUNT(*) FROM all_months_exp1 GROUP BY Payment_Mode",
    "9️. Total Amount Spent by Payment Mode": "SELECT Payment_Mode, SUM(Amount_paid) FROM all_months_exp1 GROUP BY Payment_Mode",
    "10. Expenses by Month": "SELECT MONTH(Date) AS Month, SUM(Amount_paid) FROM all_months_exp1 GROUP BY MONTH(Date)",
    "1️1. Highest Spending Month": "SELECT MONTH(Date) AS Month, SUM(Amount_paid) AS Total FROM all_months_exp1 GROUP BY MONTH(Date) ORDER BY Total DESC LIMIT 1",
    "1️2. Transactions Above 1000": "SELECT * FROM all_months_exp1 WHERE Amount_paid > 1000",
    "1️3. Transactions Below 100": "SELECT * FROM all_months_exp1 WHERE Amount_paid < 100",
    "1️4. Total Cashback Received": "SELECT SUM(Cash_Back) AS Total_Cashback FROM all_months_exp1",
    "1️5. Transactions with Cashback": "SELECT * FROM all_months_exp1 WHERE Cash_Back > 0",
    "1️6. Latest 5 Transactions": "SELECT * FROM all_months_exp1 ORDER BY Date DESC LIMIT 5",
    "1️7. Oldest 5 Transactions": "SELECT * FROM all_months_exp1 ORDER BY Date ASC LIMIT 5",
    "1️8. Expenses in Last 30 Days": "SELECT * FROM all_months_exp1 WHERE Date >= CURDATE() - INTERVAL 30 DAY",
    "1️9. Highest Expense in Each Category": "SELECT Categories, MAX(Amount_paid) FROM all_months_exp1 GROUP BY Categories",
    "2️0. Number of Transactions per Day": "SELECT Date, COUNT(*) FROM all_months_exp1 GROUP BY Date ORDER BY Date DESC"
}

# Dropdown to select a query
selected_query = st.selectbox("Select a Query:", list(queries.keys()))

# Run the query when the user clicks the button
if st.button("Run Query"):
    query = queries[selected_query]
    df = execute_query(query)
    if df is not None:
        st.write(f"### Results for: {selected_query}")
        st.dataframe(df)

