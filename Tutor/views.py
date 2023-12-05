from django.shortcuts import redirect, render
# Create your views here.
from .models import listWord, Info
from .forms import listWordForm, InfoForm

import pyttsx3





def index(request):
   dd = listWord.objects.all()
   info = Info.objects.all()


   return render(request, 'bff/index.html', {"dd":dd, "info":info} )




def play(request, id):
   

    dd = listWord.objects.get(id = id)

    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-100)

    engine.setProperty('gender', 'female')

    engine.setProperty('voice', "brazil")
    engine.say(dd.bra)
    engine.runAndWait()

    return render(request, 'bff/play.html', {} )




def add(request):

   form = listWordForm()

   if request.method == 'POST':
        form = listWordForm(request.POST)


        if form.is_valid():
            form.save()
            return redirect('index')

   return render(request, 'bff/addWord.html', {"form":form} )




def addInfo(request):

   form = InfoForm()

   if request.method == 'POST':
        form = InfoForm(request.POST  or None, request.FILES or None)


        if form.is_valid():
            form.save()
            return redirect('index')

   return render(request, 'bff/addInfo.html', {"form":form} )

