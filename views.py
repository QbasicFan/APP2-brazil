from django.shortcuts import redirect, render
# Create your views here.
from .models import listWord, Info
from .forms import listWordForm, InfoForm

from termOsCss.models import MMpost



import pyttsx3





def index(request):
   dd = listWord.objects.all()
   return render(request, 'Tutor/index.html', {"dd":dd} )




def play(request, id):
   

    dd = listWord.objects.get(id = id)

    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-100)

    engine.setProperty('gender', 'female')

    engine.setProperty('voice', "brazil")
    engine.say(dd.bra)
    engine.runAndWait()

    return render(request, 'Tutor/play.html', {} )




def add(request):

   form = listWordForm()

   if request.method == 'POST':
        form = listWordForm(request.POST, request.FILES or None)


        if form.is_valid():
            form.save()
            return redirect('/Tutor/')

   return render(request, 'Tutor/addWord.html', {"form":form} )




def addInfo(request):

   form = InfoForm()

   if request.method == 'POST':
        form = InfoForm(request.POST  or None, request.FILES or None)


        if form.is_valid():
            form.save()
            return redirect('/Tutor/')

   return render(request, 'Tutor/addInfo.html', {"form":form} )




def blog(request):
   posts = MMpost.objects.all()

   return render(request, 'Tutor/blog.html', {"posts":posts} )


def quizz(request):
   return render(request, 'Tutor/quizz.html', {} )


def travel(request):
   return render(request, 'Tutor/travel.html', {} )



def about(request):

   info = Info.objects.all()

   return render(request, 'Tutor/about.html', {"info":info} )









