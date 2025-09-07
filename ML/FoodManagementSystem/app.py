import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Function to create a connection to the SQLite database
def get_connection():
    return sqlite3.connect('food_wastage.db')

# Function to run SQL queries and return a DataFrame
def run_query(query):
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.set_page_config(layout="wide")

st.title("Local Food Wastage Management System")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Viewer", "Analytical Queries", "CRUD Operations"])

# --- Home Page ---
if page == "Home":
    st.header("Welcome to the Food Wastage Management System")
    st.write("""
    This application helps manage surplus food by connecting providers with receivers.
    Use the navigation panel on the left to explore different sections:
    - **Data Viewer**: View the raw data from our database tables.
    - **Analytical Queries**: Explore insights through pre-defined SQL queries and visualizations.
    - **CRUD Operations**: Interact with the database to add, view, update, or delete records.
    """)
    st.image("data:image/jpeg;base64,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?q=80&w=2070&auto=format&fit=crop", caption="Connecting Communities, Reducing Waste")

# --- Data Viewer Page ---
elif page == "Data Viewer":
    st.header("Database Table Viewer")
    table_name = st.selectbox("Select a table to view", ["providers", "receivers", "food_listings", "claims"])
    st.dataframe(run_query(f"SELECT * FROM {table_name}"))

# --- Analytical Queries Page ---
elif page == "Analytical Queries":
    st.header("Analytical Queries & Insights")

    queries = {
        "1. How many food providers and receivers are there in each city?": "SELECT City, COUNT(Provider_ID) AS Number_of_Providers FROM providers GROUP BY City ORDER BY Number_of_Providers DESC;",
        "2. Which type of food provider (restaurant, grocery store, etc.) contributes the most food?": "SELECT Provider_Type, SUM(Quantity) AS Total_Quantity_Donated FROM food_listings GROUP BY Provider_Type ORDER BY Total_Quantity_Donated DESC;",
        "3. What is the contact information of food providers in a specific city (e.g., 'New Jessica')?": "SELECT Name, Address, Contact FROM providers WHERE City = 'New Jessica';",
        "4. Which receivers have claimed the most food?": "SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims FROM receivers r JOIN claims c ON r.Receiver_ID = c.Receiver_ID GROUP BY r.Name ORDER BY Total_Claims DESC LIMIT 10;",
        "5. What is the total quantity of food available from all providers?": "SELECT SUM(Quantity) AS Total_Available_Food_Quantity FROM food_listings;",
        "6. Which city has the highest number of food listings?": "SELECT Location AS City, COUNT(Food_ID) AS Number_of_Listings FROM food_listings GROUP BY Location ORDER BY Number_of_Listings DESC LIMIT 1;",
        "7. What are the most commonly available food types?": "SELECT Food_Name, COUNT(*) AS Frequency FROM food_listings GROUP BY Food_Name ORDER BY Frequency DESC LIMIT 10;",
        "8. How many food claims have been made for each food item?": "SELECT fl.Food_Name, COUNT(c.Claim_ID) AS Number_of_Claims FROM food_listings fl JOIN claims c ON fl.Food_ID = c.Food_ID GROUP BY fl.Food_Name ORDER BY Number_of_Claims DESC LIMIT 10;",
        "9. Which provider has had the highest number of successful food claims?": "SELECT p.Name AS Provider_Name, COUNT(c.Claim_ID) AS Successful_Claims FROM providers p JOIN food_listings fl ON p.Provider_ID = fl.Provider_ID JOIN claims c ON fl.Food_ID = c.Food_ID WHERE c.Status = 'Completed' GROUP BY p.Name ORDER BY Successful_Claims DESC LIMIT 1;",
        "10. What percentage of food claims are completed vs. pending vs. canceled?": "SELECT Status, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims) AS Percentage FROM claims GROUP BY Status;",
        "11. What is the average quantity of food claimed per receiver?": "SELECT r.Name, AVG(fl.Quantity) AS Average_Quantity_Claimed FROM receivers r JOIN claims c ON r.Receiver_ID = c.Receiver_ID JOIN food_listings fl ON c.Food_ID = fl.Food_ID GROUP BY r.Name ORDER BY Average_Quantity_Claimed DESC LIMIT 10;",
        "12. Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?": "SELECT fl.Meal_Type, COUNT(c.Claim_ID) AS Number_of_Claims FROM food_listings fl JOIN claims c ON fl.Food_ID = c.Food_ID GROUP BY fl.Meal_Type ORDER BY Number_of_Claims DESC;",
        "13. What is the total quantity of food donated by each provider?": "SELECT p.Name, SUM(fl.Quantity) AS Total_Donated_Quantity FROM providers p JOIN food_listings fl ON p.Provider_ID = fl.Provider_ID GROUP BY p.Name ORDER BY Total_Donated_Quantity DESC LIMIT 10;",
        "14. Which food listings are about to expire (e.g., in the next 5 days)?": "SELECT Food_Name, Expiry_Date, Quantity FROM food_listings WHERE Expiry_Date BETWEEN DATE('now') AND DATE('now', '+5 days') ORDER BY Expiry_Date ASC;",
        "15. Which receiver types (NGO, Shelter, etc.) are most active?": "SELECT Type, COUNT(c.Claim_ID) AS Number_of_Claims FROM receivers r JOIN claims c ON r.Receiver_ID = c.Receiver_ID GROUP BY Type ORDER BY Number_of_Claims DESC;",
        "16. What is the average number of claims per day?": "SELECT AVG(daily_claims) AS Average_Claims_Per_Day FROM (SELECT DATE(Timestamp) as claim_date, COUNT(Claim_ID) as daily_claims FROM claims GROUP BY claim_date);",
        "17. What are the top 5 most common food categories (Vegetarian, Non-Vegetarian, Vegan) listed?": "SELECT Food_Type, COUNT(Food_ID) as Number_of_Listings FROM food_listings GROUP BY Food_Type ORDER BY Number_of_Listings DESC;",
        "18. Which providers have the highest quantity of a specific food, e.g., 'Bread'?": "SELECT p.Name, fl.Quantity FROM providers p JOIN food_listings fl ON p.Provider_ID = fl.Provider_ID WHERE fl.Food_Name = 'Bread' ORDER BY fl.Quantity DESC LIMIT 5;",
        "19. How many claims are made per receiver type in each city?": "SELECT r.City, r.Type, COUNT(c.Claim_ID) AS Number_of_Claims FROM receivers r JOIN claims c ON r.Receiver_ID = c.Receiver_ID GROUP BY r.City, r.Type ORDER BY r.City, Number_of_Claims DESC;",
        "20. What is the distribution of provider types (Supermarket, Restaurant, etc.) across the top 5 cities with the most providers?": "SELECT City, Type, COUNT(Provider_ID) AS Type_Count FROM providers WHERE City IN (SELECT City FROM providers GROUP BY City ORDER BY COUNT(Provider_ID) DESC LIMIT 5) GROUP BY City, Type ORDER BY City, Type_Count DESC;"
    }

    query_choice = st.selectbox("Select a Query", list(queries.keys()))

    if query_choice:
        result_df = run_query(queries[query_choice])
        st.write("**Query Result:**")
        st.dataframe(result_df)

        st.write("**Visualization:**")
        try:
            if "Percentage" in result_df.columns:
                fig = px.pie(result_df, names=result_df.columns[0], values='Percentage', title=query_choice)
            elif "Total_Quantity_Donated" in result_df.columns or "Total_Donated_Quantity" in result_df.columns or "Number_of_Claims" in result_df.columns or "Frequency" in result_df.columns or "Number_of_Listings" in result_df.columns or "Number_of_Providers" in result_df.columns:
                fig = px.bar(result_df, x=result_df.columns[0], y=result_df.columns[1], title=query_choice)
            else:
                st.warning("No suitable visualization for this query.")
                fig = None
            if fig:
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Could not generate visualization: {e}")


# --- CRUD Operations Page ---
elif page == "CRUD Operations":
    st.header("Database Management (CRUD)")

    table_to_manage = st.selectbox("Select Table to Manage", ["providers", "receivers"])
    operation = st.radio("Select Operation", ["Create", "Read/Filter", "Update", "Delete"])

    conn = get_connection()
    cursor = conn.cursor()

    if operation == "Create":
        st.subheader(f"Add a New Record to `{table_to_manage}`")
        if table_to_manage == 'providers':
            with st.form(key='add_provider_form'):
                name = st.text_input("Name")
                ptype = st.text_input("Type")
                address = st.text_area("Address")
                city = st.text_input("City")
                contact = st.text_input("Contact")
                submit_button = st.form_submit_button(label='Add Provider')

                if submit_button:
                    cursor.execute('INSERT INTO providers (Name, Type, Address, City, Contact) VALUES (?,?,?,?,?)', (name, ptype, address, city, contact))
                    conn.commit()
                    st.success("Provider added successfully!")

    elif operation == "Read/Filter":
        st.subheader(f"View and Filter Data from `{table_to_manage}`")
        filter_col = st.selectbox("Filter by Column", pd.read_sql(f'PRAGMA table_info({table_to_manage});', conn)['name'].tolist())
        filter_val = st.text_input(f"Value for {filter_col}")
        if st.button("Filter"):
            st.dataframe(run_query(f"SELECT * FROM {table_to_manage} WHERE {filter_col} LIKE '%{filter_val}%'"))

    elif operation == "Update":
        st.subheader(f"Update a Record in `{table_to_manage}`")
        id_col = 'Provider_ID' if table_to_manage == 'providers' else 'Receiver_ID'
        record_id = st.number_input(f"Enter {id_col} of the record to update", min_value=1, step=1)
        if table_to_manage == 'providers':
            new_contact = st.text_input("Enter new contact information")
            if st.button("Update Contact"):
                cursor.execute(f'UPDATE providers SET Contact = ? WHERE Provider_ID = ?', (new_contact, record_id))
                conn.commit()
                st.success(f"Provider {record_id} updated successfully!")

    elif operation == "Delete":
        st.subheader(f"Delete a Record from `{table_to_manage}`")
        id_col = 'Provider_ID' if table_to_manage == 'providers' else 'Receiver_ID'
        record_id_del = st.number_input(f"Enter {id_col} of the record to delete", min_value=1, step=1)
        if st.button("Delete Record"):
            cursor.execute(f'DELETE FROM {table_to_manage} WHERE {id_col} = ?', (record_id_del,))
            conn.commit()
            st.warning(f"Record with ID {record_id_del} deleted from `{table_to_manage}`!")

    conn.close()
