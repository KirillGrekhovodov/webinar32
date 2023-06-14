from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.cat import Cat


# Create your views here.


def index_view(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        Cat.name = request.POST.get("cat_name")
        return HttpResponseRedirect('/cat_stats/')


def cat_stats_view(request):
    if request.method == "GET":
        context = {
            "name": Cat.name,
            "age": Cat.age,
            "satiety": Cat.satiety,
            "avatar": Cat.avatar
        }
        return render(request, "cat_stats.html", context)
    else:
        action = request.POST.get("action")
        if action == "play":
            Cat.play()
            print(Cat.avatar)
        elif action == "feed":
            pass
        return HttpResponseRedirect('/cat_stats/')
