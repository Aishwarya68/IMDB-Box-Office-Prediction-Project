from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
# Create your views here.

from joblib import load
from numpy import int64
model = load('./savedModels/model.joblib')


def mainpage(request):
    if request.method == 'POST':
        print('entered')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        print(username)
        print(password)
        print(user)
        if user is not None:
            print("username")
            auth.login(request,user)
            #posts = Feature.objects.all()
            return redirect("main")
        else:
            return render(request,'login.html')
    else:
        return render(request,'main.html')

def prediction(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        duration = request.POST['duration']
        genre = request.POST['genre']
        year = request.POST['year']
        director = request.POST['director']
        actor1 = request.POST['actor1']
        actor2 = request.POST['actor2']
        #actor3 = request.POST['actor3']
        budget = request.POST['budget']
        
        y_pred = model.predict([[year, budget, genre, duration,
                 director, actor1]])
        #y_pred = model.predict([[movie_name,duration,year,genre,director,actor1,actor2,actor3]])
        return render(request,'prediction.html',{'result' : y_pred.astype('int64')})
        #return render(request,'main.html',{'result' : y_pred})
    else:
        return render(request,'prediction.html')
    

   # return render(request,'main.html')

    