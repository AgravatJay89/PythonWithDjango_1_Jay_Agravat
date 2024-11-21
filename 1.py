import requests
import pandas as pd
from django.http import HttpResponse
import csv

def fetch_and_save_cities(request):
    # Step 1: Define the API URL (Replace with an actual API providing city data)
    api_url = "https://example.com/api/indian-cities"  # Replace this with a real API

    # Step 2: Make a GET request to the API
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for HTTP errors
        cities_data = response.json()  # Parse the response as JSON
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error fetching cities: {e}", status=500)

    # Step 3: Process the data (assuming 'name' key contains city names)
    cities = []
    for city in cities_data:
        cities.append({'City Name': city.get('name', 'Unknown')})

    # Step 4: Convert data to a DataFrame
    df = pd.DataFrame(cities)

    # Step 5: Save the DataFrame to a CSV file
    csv_file_path = "indian_cities.csv"
    df.to_csv(csv_file_path, index=False)

    # Step 6: Offer the file for download
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{csv_file_path}"'
    writer = csv.writer(response)
    writer.writerow(['City Name'])  # Header
    for city in cities:
        writer.writerow([city['City Name']])

    return response
