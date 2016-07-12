from django.shortcuts import render
from .models import Lectures

# Just using function based views for now because they're easy
def lectures_home(request):
    queryset = Lectures.objects.all()
    if request.user.is_authenticated():
        context = {
        "object_list": queryset,
        "title":"List"
    }
    else:
        context = {
        "title":"bruh"
    }

    return render(request, "lectures.html", context)