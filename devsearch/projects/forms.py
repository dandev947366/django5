from django import forms

from .models import Project  # Ensure you have a Project model defined


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "demo_link",
            "source_link",
            "tags",
        ]  # Add other fields as necessary
