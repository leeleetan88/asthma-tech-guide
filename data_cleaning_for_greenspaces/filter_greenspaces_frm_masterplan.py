import json

# Function to filter GeoJSON features by the presence of 'PARK' or 'OPEN SPACE', while excluding 'BUSINESS PARK'
def filter_geojson_by_description(geojson_data, include_strings, exclude_string):
    # Filter features based on the presence of 'PARK' or 'OPEN SPACE' and exclusion of 'BUSINESS PARK'
    filtered_features = [
        feature for feature in geojson_data['features']
        if any(include_string in feature['properties'].get('Description', '') for include_string in include_strings)
        and exclude_string not in feature['properties'].get('Description', '')
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

# Filter features that have 'PARK' or 'OPEN SPACE' but not 'BUSINESS PARK' in the 'Description' field
include_strings = ["PARK", "OPEN SPACE"]
exclude_string = "BUSINESS PARK"
filtered_data = filter_geojson_by_description(geojson_data, include_strings, exclude_string)

# Save the filtered data to a new GeoJSON file (replace 'filtered_output_greenspaces.geojson')
with open('./Data_collected/filtered_output_greenspaces.geojson', 'w') as f:
    json.dump(filtered_data, f, indent=4)

print("Filtered GeoJSON data saved to './Data_collected/filtered_output_greenspaces.geojson'.")
