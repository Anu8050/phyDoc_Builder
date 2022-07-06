from django.shortcuts import render, redirect
from django.http import HttpResponse
from phyDoc_app.models import Document_templates, Document_details
from django.contrib import messages
# Create your views here.

#For inserting values
def insert(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        Document_template_path = request.POST.get('Document_template_path')
        data = Document_templates(id=id, name=name, Document_template_path=Document_template_path)
        data.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'insert.html')