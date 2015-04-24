from django.shortcuts import render
from django.http import HttpResponse
import requests
import clickbaitgen

from .models import Greeting

# Create your views here.
def index(request):
    phrase = clickbaitgen.create_bait()
    #return HttpResponse(phrase)

    return render(
        request, 'index.html', {
            'phrase': phrase
        }
    )


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

