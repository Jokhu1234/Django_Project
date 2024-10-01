from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.jobs_list, name="joblist"),
    path("new-job/", views.job_new, name="new-job"),
]