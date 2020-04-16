from django.shortcuts import render, get_object_or_404
from .models import Meeting
# Create your views here.


def detail(request, id):
    # meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "detail.html", {"meeting": meeting})