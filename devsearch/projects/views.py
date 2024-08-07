from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ProjectForm
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


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"object": project}
    return render(request, "projects/delete_template.html", context)
