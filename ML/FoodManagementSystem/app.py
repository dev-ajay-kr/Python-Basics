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
    st.image("https://images.unsplash.com/photo-1604162953252-2b604a5a8f4c?q=80&w=2070&auto=format&fit=crop", caption="Connecting Communities, Reducing Waste")

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
