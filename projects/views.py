from django.shortcuts import render
from .models import Project



def project_list(request):
    category = request.GET.get('category')
    projects = Project.objects.all()
    
    if category:
        projects = projects.filter(category=category)
    
    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'current_category': category
    })