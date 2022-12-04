from django.shortcuts import render

def renderBlog(request):
    return render(request,'index.html')