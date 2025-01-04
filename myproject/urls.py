from django.contrib import admin
from django.urls import path
from shapes import views 

urlpatterns = [
    path('admin/', admin.site.urls),        # Admin page
    # path('add/', views.add_numbers, name='add_numbers'),  # URL for the add_numbers view
    path('fetch-data/', views.fetch_data, name='fetch_data'),
    path('export-csv/', views.export_to_csv, name='export_to_csv'),  # Export CSV view

]

for pattern in urlpatterns:
    print(pattern)