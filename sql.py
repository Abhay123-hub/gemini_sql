from dotenv import load_dotenv
load_dotenv()  # Load all environment variables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Google Gemini API key
genai.configure(api_key=os.getenv("Google_API_KEY"))

# Function to load Google Gemini model and provide queries as response
def get_gemini_response(question, prompt):
    # Verify if the API model initialization and method are correct
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text.strip()

# Function to retrieve query results from the database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        curr = conn.cursor()
        curr.execute(sql)
        rows = curr.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return f"Error executing query: {e}"

# Prompt for the AI model
prompt = """
You are an expert in converting English sentences to SQL queries.
The SQL database has the name STUDENTS3 and has the following columns: NAME, CLASS, SUBJECT.
Example: How many entries of record are present?
The SQL command will be something like: SELECT COUNT(*) FROM STUDENTS3;
Ensure the SQL command is valid and does not include unnecessary characters such as `sql` or ``` in the output.
"""

# Set up user interface
st.set_page_config(page_title="SQL Query Retriever with Gemini")
st.header("Gemini App to Retrieve SQL Data")

# Get user input
question = st.text_input("Input your question", key="input")

# When the submit button is clicked
if st.button("Ask the question"):
    if question:
        # Get SQL query from Gemini model
        generated_query = get_gemini_response(question, prompt)
        
        st.subheader("Generated SQL Query:")
        st.write(generated_query)  # Display the generated query

        # Execute the query and retrieve results from the SQLite database
        result = read_sql_query(generated_query, "student1.db")
        
        st.subheader("Query Result:")
        if isinstance(result, list):  # If the result is valid rows from the database
            for row in result:
                st.write(row)
        else:  # If there was an error
            st.error(result)
    else:
        st.error("Please enter a question.")

     