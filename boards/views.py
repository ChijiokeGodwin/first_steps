from django.shortcuts import render
from .models import Board


def home(request):
    boards = Board.objects.all()
    b = {'boards': boards}
    return render(request, 'boards/home.html', b)
