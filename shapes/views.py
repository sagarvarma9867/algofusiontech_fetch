# from django.shortcuts import render
# from .forms import AdditionForm

# def add_numbers(request):
#     result = None
#     if request.method == "POST":
#         form = AdditionForm(request.POST)
#         if form.is_valid():
#             num1 = form.cleaned_data['num1']
#             num2 = form.cleaned_data['num2']
#             result = num1 + num2
#     else:
#         form = AdditionForm()

#     return render(request, 'calculator/addition.html', {'form': form, 'result': result})



import csv
from django.http import HttpResponse  # <-- Make sure this is imported
from django.shortcuts import render
import requests

def fetch_data(request):
    url = "https://www.oracle.com/a/ocom/docs/cloudestimator2/data/shapes.json?ver=1634"  # Replace with your actual URL

    # Fetch data from the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Assuming the response is in JSON format
        count = data.get('count', 0)  # Get the count (default to 0 if not present)
        items = data.get('items', [])  # Get the items (default to empty list if not present)
    else:
        count = 0
        items = []
        error_message = "Failed to fetch data from the API."

    # Pass the data and count to the template
    return render(request, 'table_data/data_table.html', {
        'count': count,
        'items': items,
        'error_message': error_message if 'error_message' in locals() else None
    })


def export_to_csv(request):
    # The URL from which we are fetching the data
    url = "https://www.oracle.com/a/ocom/docs/cloudestimator2/data/shapes.json?ver=1634"  # Replace with your actual URL

       # Fetch data from the API
    response = requests.get(url)

    # If the request is successful, process the data
    if response.status_code == 200:
        data = response.json()  # Assuming the response is in JSON format
        items = data.get('items', [])
    else:
        items = []

    # Create an HttpResponse with CSV content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the header row (based on your item structure)
    writer.writerow(['ID', 'Name', 'Shape_type', 'Localdisk', 'Subtype', 'ProcessorType'])

    # Write the data rows
    for item in items:
        writer.writerow([
            item.get('id'), 
            item.get('name'), 
            item.get('shapeType'), 
            item.get('localDisk'), 
            item.get('subType'), 
            item.get('processorType')])

    return response