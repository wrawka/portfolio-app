from django.shortcuts import render

from projects.models import Project


def index(request):
    return render(request, 'index.html', {})


def projects_index(requset):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(requset, 'projects_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)