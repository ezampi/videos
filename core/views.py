from django.shortcuts import render

def index(request):
    return render(request, template_name='core/index.html')

def list_videos(request):
    return render(request, template_name= 'core/videos.html')

def player(request, slug):
    return render(request, template_name='core/player.html')
