import streamlit as st
from streamlit_folium import folium_static
import folium
import json

# Create a folium map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Define the state boundaries and information
state_info = {
    'Maharashtra': 'Information about Maharashtra',
    'Karnataka': 'Information about Karnataka',
    'sujal': 'Information about Karnataka',
    # Add more states as needed
}

# Add GeoJSON data for Indian states (you can get this data online)
geojson_data = r"states_india.geojson"  # Replace with the actual path

# Function to handle state selection
def state_selection(state_name):
    st.write(f"## {state_name} Information")
    st.write(state_info[state_name])

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
    popup=folium.GeoJsonPopup(fields=['st_nm'], aliases=['sujal\nsujal\nsujal'], localize=True),
    control=False
).add_to(india_map)

# Streamlit app
st.title("Interactive India Map")

# Display the folium map
folium_static(india_map)

# Dropdown for state selection
selected_state = st.selectbox("Select a state", list(state_info.keys()))

# Display state information based on selection
if selected_state:
    state_selection(selected_state)
