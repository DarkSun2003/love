# core/views.py
from django.shortcuts import render
from .models import ValentineVideo

def valentine_home(request):
    # Fetch the active video. If none marked active, grab the first one uploaded.
    video_obj = ValentineVideo.objects.filter(is_active=True).first()
    
    # Fallback if no active video exists
    if not video_obj:
        video_obj = ValentineVideo.objects.first()

    video_url = ""
    if video_obj and video_obj.video_file:
        video_url = video_obj.video_file.url

    context = {
        'video_url': video_url
    }
    return render(request, 'core/index.html', context)