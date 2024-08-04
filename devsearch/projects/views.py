from django.http import HttpResponse
from django.shortcuts import render

projectList = [
    {
        "id": "1",
        "title": "Ecommerce website",
        "description": "fully functional ecommerce web",
    },
    {
        "id": "2",
        "title": "Porfolio website",
        "description": "A porfolio website",
    },
    {
        "id": "3",
        "title": "Content management",
        "description": "Content management website",
    },
]


def projects(request):
    page = "projects"
    number = 9
    context = {"page": page, "number": number, "projects": projectList}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i["id"] == pk:
            projectObj = i
    return render(request, "projects/single-project.html", {"project": projectObj})
