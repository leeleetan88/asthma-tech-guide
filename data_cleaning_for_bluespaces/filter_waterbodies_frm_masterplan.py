import json

# Function to filter GeoJSON features by the presence of 'WATERBODY' in the 'Description' field
def filter_geojson_by_description(geojson_data, search_string):
    # Filter features based on the presence of the search_string ('WATERBODY') in the 'Description' field
    filtered_features = [
        feature for feature in geojson_data['features']
        if search_string in feature['properties'].get('Description', '')
    ]
    
    # Create a new GeoJSON structure with the filtered features
    filtered_geojson = {
        "type": geojson_data['type'],
        "crs": geojson_data['crs'],
        "features": filtered_features
    }
    
    return filtered_geojson

# Load your GeoJSON file (replace 'MasterPlan2019LandUselayer.geojson' with the actual filename)
with open('./Data_collected/MasterPlan2019LandUselayer.geojson', 'r') as f:
    geojson_data = json.load(f)

# Filter features that have 'WATERBODY' in the 'Description' field
search_string = "WATERBODY"
filtered_data = filter_geojson_by_description(geojson_data, search_string)

# Save the filtered data to a new GeoJSON file (replace 'filtered_output_waterbodies.geojson')
with open('./Data_collected/filtered_output_waterbodies.geojson', 'w') as f:
    json.dump(filtered_data, f, indent=4)

print("Filtered GeoJSON data saved to './Data_collected/filtered_output_waterbodies.geojson'.")