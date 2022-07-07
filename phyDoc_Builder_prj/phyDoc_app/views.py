from django.shortcuts import render, redirect
from django.http import HttpResponse
from phyDoc_app.models import Document_templates, Document_details
from django.contrib import messages
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

# Delete Employee
def remove(request, pk):
    document_templates = Document_templates.objects.get(id=pk)

    if request.method == 'POST':
        document_templates.delete()
    context = {
        'document_templates': document_templates,
    }

    return render(request, 'delete.html', context)