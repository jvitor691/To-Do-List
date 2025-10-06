from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^tasks/?$', views.tasks_list_create, name='tasks_list_create'),
    re_path(r'^tasks/(?P<task_id>\d+)/?$', views.tasks_detail, name='tasks_detail'),
    re_path(r'^tasks/(?P<task_id>\d+)/status/?$', views.patch_status, name='patch_status'),
]
