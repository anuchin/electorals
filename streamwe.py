import streamlit as st
import pandas as pd
data = pd.read_csv('data.csv')

# Session state variable to track the current page
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Function to switch pages
def switch_page(new_page):
    st.session_state.page = new_page

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.button('Home', on_click=lambda: switch_page('Home'))
st.sidebar.button('Purchaser Data', on_click=lambda: switch_page('Purchaser Data'))

# Show content based on the current page
if st.session_state.page == 'Home':
    # Display the home page content here
    st.write("Welcome to the home page!")
    grouped_data = data.groupby('Purchaser Name')['Amount'].sum().reset_index()

# Create a Streamlit app
    st.write("Purchase Data")
    st.write("-------------")
    st.dataframe(grouped_data, width=1000)

elif st.session_state.page == 'Purchaser Data':
    # Load the CSV file

    # Create a new page
    st.title("Purchaser Data")

    # Get the list of unique purchaser names
    purchaser_names = data['Purchaser Name'].unique().tolist()

    # Create a dropdown to select a purchaser name
    selected_purchaser = st.selectbox("Select a purchaser name", purchaser_names)

    # Filter the DataFrame based on the selected purchaser name
    filtered_data = data[data['Purchaser Name'] == selected_purchaser]

    # Display the filtered DataFrame
    st.write("Purchase Data for", selected_purchaser)
    st.write("-------------")
    st.dataframe(filtered_data)

else:
    st.write("Page not found!")