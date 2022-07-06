from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Document_templates, Document_details
# Create your views here.

#For inserting values
def insert(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        Document_template_path = request.POST['Document_template_path']
        data = Document_templates(id=id, name=name, Document_template_path=Document_template_path)
        data.save()
        return redirect('show/')
    else:
        return render(request, 'insert.html')