from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    return render(
        request,
        "HelloT2SRApp/index.html",
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "HelloT2SRApp/about.html",
        {
            'title' : "About HelloT2SRApp",
            'message' : "",
            'content' : "CONTENU POUR ABOUT."
        }
    )