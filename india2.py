import streamlit as st
from streamlit_folium import folium_static
import folium

# Create a folium map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Define the state boundaries and information
state_info = {
    'Maharashtra': 'Information about Maharashtra',
    'Karnataka': 'Information about Karnataka',
    # Add more states as needed
}

# Add GeoJSON data for Indian states (you can get this data online)
geojson_data = r"states_india.geojson"  # Replace with the actual path

# Add the GeoJSON layer to the map
folium.GeoJson(
    geojson_data,
    name='geojson',
    style_function=lambda feature: {
        'fillColor': 'lightblue',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.6
    },
    highlight_function=lambda x: {'weight': 3, 'fillColor': 'yellow', 'color': 'yellow', 'fillOpacity': 0.6}
).add_to(india_map)

# Function to handle state button clicks
def state_button_click(feature, layer):
    state_name = feature['properties']['name']
    st.write(f"**{state_name} Information:**")
    st.write(state_info[state_name])

# Streamlit app
st.title("Interactive India Map")

# Display the folium map
folium_static(india_map)