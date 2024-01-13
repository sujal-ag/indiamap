import streamlit as st
from streamlit_folium import folium_static
import folium
import json

def state_selection(selected_state, state_info):
    st.write(f"## {selected_state} Information")
    st.write(state_info[selected_state])

def page1():
    
    # Define the state boundaries and information
    state_info = {
        'Maharashtra': 'Information about Maharashtra',
        'Karnataka': 'Information about Karnataka',
        'sujal': 'Information about Sujal',
        # Add more states as needed
    }
    
    # Dropdown for state selection
    selected_state = st.selectbox("Select a state", list(state_info.keys()))

    # Display state information based on selection
    if selected_state:
        state_selection(selected_state, state_info)

def page2():
    
    # Create a folium map centered on India
    india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

    # Add GeoJSON data for Indian states (you can get this data online)
    geojson_data = r"C:\Users\Sujal\OneDrive\Desktop\hackathon\states_india.geojson"  # Replace with the actual path

    # Function to customize tooltip content
    def get_tooltip_content(feature):
        state_name = feature['properties']['st_nm']
        return f"State: {state_name}"

    # Add the GeoJSON layer to the map with tooltips
    folium.GeoJson(
        geojson_data,
        name='geojson',
        style_function=lambda feature: {
            'fillColor': 'lightblue',
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.6
        },
        highlight_function=lambda x: {'weight': 3, 'fillColor': 'yellow', 'color': 'yellow', 'fillOpacity': 0.6},
        tooltip=folium.GeoJsonTooltip(fields=['st_nm'], aliases=['State'], localize=True, style="font-weight: bold"),
        popup=folium.GeoJsonPopup(fields=['st_nm'], aliases=['Sujal\nSujal\nSujal'], localize=True),
        control=False
    ).add_to(india_map)

    # Streamlit app
    st.title("Interactive India Map")

    # Display the folium map
    folium_static(india_map)

# Main App
st.title("Underarted tourist places list state-wise")

# Button to navigate to Page 2
if st.button("Interactive Map"):
    st.session_state.page = 2

# Button to navigate to Page 
if st.button("Dropdown"):
    st.session_state.page = 1

# Check the selected page and display the corresponding content
if hasattr(st.session_state, 'page'):
    if st.session_state.page == 1:
        page1()
    elif st.session_state.page == 2:
        page2()
