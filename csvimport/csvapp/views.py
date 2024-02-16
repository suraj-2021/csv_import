from django.shortcuts import render,redirect
from.forms import CSVImportForm
from . models import Book
import csv

def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST,request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                Book.objects.create(
                    title = row['title'],
                    author = row['author'],
                    publicaton_year = row['isbn']
                )
            return redirect('success_page')
    else:
        form = CSVImportForm()

    return render(request,'import.html',{'form':form})
def success_page(request):
    return render (request,'success.html')