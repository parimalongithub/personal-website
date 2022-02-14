from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("projects",views.porjects,name="projects"),
    path("skills",views.skills,name="skills"),
    path("achievments",views.achievments,name="achievments"),


   
   
]
