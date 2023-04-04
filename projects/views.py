from django.shortcuts import render, get_object_or_404

from projects.models import Project


def index(request):
    return render(request, 'index.html', {})


def project_index(requset):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(requset, 'projects_index.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
