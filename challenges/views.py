from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges_list = {
    'january': 'Chill and meditate',
    'february': 'Chill and play guitar',
    'march': 'Chill and play games',
    'april': 'Chill and meditate',
    'may': 'Chill and play guitar',
    'june': 'Chill and play games',
    'july': 'Chill and meditate',
    'august': 'Chill and play guitar',
    'september': 'Chill and play games',
    'october': 'Chill and meditate',
    'november': 'Chill and play guitar',
    'december': 'Chill and play games',
    }

# Create your views here.
def index(request):
    return HttpResponse('My Monthly Challenges')

def month_by_number(request, month):
    return HttpResponse('Challenges for ' + str(month))

def month(request, month):
    challenge_text = ''
    try:
        challenge_text = monthly_challenges_list[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('Not a month, so chill')
