# myapp/views.py
from django.shortcuts import render
import pandas as pd
import os

def moon(request):
    # Construct the full path to the CSV file
    csv_file_path = os.path.join('myapp', 'static', 'data', 'nakamura_1979_sm_locations.csv')

    # Load CSV data into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Extract relevant data including year and day
    relevant_data = df[['Year', 'Day', 'Lat', 'Long', 'Magnitude']]  # Adjust column names if necessary

    # Convert DataFrame to a list of dictionaries
    data_list = relevant_data.to_dict(orient='records')

    # Pass the data to the template
    context = {'data_list': data_list}

    return render(request, 'moon.html', context)
