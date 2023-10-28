from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("record/", views.record, name="record"),
    path('openai/', views.query_view, name='query'), 
]