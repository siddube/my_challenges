from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges_dict = {
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

def get_month_index():
    return list(monthly_challenges_dict.keys())

# Create your views here.
def index(request):
    list_items = ''
    months = get_month_index()
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenges', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def month_by_number(request, month):
    months = get_month_index()
    
    if month > len(months):
        return HttpResponseNotFound('Not a month, so chill!')
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenges', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def month(request, month):
    challenge_text = ''
    try:
        challenge_text = monthly_challenges_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('Not a month, so chill!')
