from django.urls import path

from . import views

app_name = "ToDo"

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /ToDo/
    path("", views.index, name="index"),
    # ex: /ToDo/5/
    path("<int:task_id>/", views.detail, name="detail"),
    # ex: /ToDo/5/complete/
    path("<int:task_id>/complete/", views.complete, name="complete"),
    # ex: /ToDo/5/delete/
    path("<int:task_id>/delete/", views.delete, name="delete"),
]