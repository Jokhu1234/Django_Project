from django import forms
from . import models


class CreateJob(forms.ModelForm):
    class Meta:
        model = models.Job
        fields = [
            "title",
            "company",
            "location",
            "jobtype",
            "description",
            "applylink",
        ]