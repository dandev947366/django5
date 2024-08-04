from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

projectList = Project.objects.all()


def projects(request):
    page = "projects"
    number = 9
    context = {"page": page, "number": number, "projects": projectList}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {"project": projectObj})
