from cgitb import html
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html" )
def about(request):

    return render(request,"aboutme.html") 
def porjects(request):
    
    return render(request,"projects.html") 
def skills(request):
    
    return render(request,"skills.html") 
def achievments(request):
    
    return render(request,"achievments.html") 