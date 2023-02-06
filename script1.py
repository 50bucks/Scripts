import requests
import json

# Connect to the API
url = "https://swapi.dev/api/vehicles/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data
    data = json.loads(response.text)

    # Create a set to store unique manufacturers
    manufacturers = set()

    # Iterate over the vehicles in the data
    for vehicle in data["results"]:
        # Add the manufacturer to the set
        manufacturers.add(vehicle["manufacturer"])

    # Convert the set to a list and sort it
    manufacturers = sorted(list(manufacturers))

    # Print the first 5 manufacturers
    for i, manufacturer in enumerate(manufacturers[:5]):
        print(f"{i + 1}. {manufacturer}")
else:
    # If the request was unsuccessful, print an error message
    print(f"Request failed with status code {response.status_code}")
