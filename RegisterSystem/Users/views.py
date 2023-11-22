from django.shortcuts import render
from .models import User

def home(request): 
    return render(request, 'Users/home.html')

def users(request):
    #Getting the data from user input and saving it on database;
    new_user = User()
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    new_user.save()

    #Retrieving saved data;
    users_in = {
        'users': User.objects.all()
    }

    #Returning data;
    return render(request, 'Users/users.html', users_in)