from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.CreateAlbum(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect("add_album")
    else:
        album_form = forms.CreateAlbum()
    return render(request,'add_album.html',{'form' : album_form})


def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.CreateAlbum(instance=album)
    if request.method == 'POST':
        album_form = forms.CreateAlbum(request.POST ,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect("homepage")
    return render(request,'add_album.html',{'form' : album_form})

def delete_album(request,id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect("homepage")