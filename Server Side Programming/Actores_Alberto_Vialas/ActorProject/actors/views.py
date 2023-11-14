from django.shortcuts import render
from .models import Actor

def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'actors/actor_list.html', {'actors': actors})

def actor_detail(request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    return render(request, 'actors/actor_detail.html', {'actor': actor})

