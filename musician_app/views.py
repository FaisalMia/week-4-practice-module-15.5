from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.
def add_music(request):
    if request.method == 'POST':
        music_form = forms.CreateMusic(request.POST)
        if music_form.is_valid():
            music_form.save()
            return redirect("add_music")
    else:
        music_form = forms.CreateMusic()
    return render(request,'add_music.html',{'form' : music_form})


def edit_music(request,first_name,last_name):
    musician = models.Musician.objects.get(first_Name=first_name,last_Name=last_name)
    musician_form = forms.CreateMusic(instance=musician)
    if request.method == 'POST':
        musician_form = forms.CreateMusic(request.POST ,instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("homepage")
    return render(request,'add_music.html',{'form' : musician_form})