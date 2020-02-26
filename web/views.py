from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_expense(request):
    '''submit ac expense'''

   
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    now = datetime.now()
    Expense.objects.create(user = this_user, amount=request.POST['amount'],
                            text=request.POST['text'], date=now)
    
    print("I'm in submit expense\n{}".format(this_user))
    print(request.POST)
    
    return JsonResponse({
        'status': 'ok',
        }, encoder=JSONEncoder)
        
        
@csrf_exempt
def submit_income(request):
    '''submit ac income'''

   
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user = this_user, amount=request.POST['amount'],
                            text=request.POST['text'], date=date)
    
    print("I'm in submit expense\n{}".format(this_user))
    print(request.POST)
    
    return JsonResponse({
        'status': 'ok',
        }, encoder=JSONEncoder)