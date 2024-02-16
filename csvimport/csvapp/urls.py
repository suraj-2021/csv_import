from django.urls import path
from . import views

urlpatterns = [
    path('import-csv/', views.import_csv, name='import_csv'),
    path('success/', views.success_page, name='success_page'),  # Create this view if needed
]