from django.http import HttpResponse
from . models import Movie_details
from django.shortcuts import render, redirect
from .forms import MovieForm

# Create your views here.
def index(request):
    ##get all data
    obj=Movie_details.objects.all()
    return render(request,"index.html",{'movie_list':obj})
def details(request,movie_id):
    #get data of particular id
    obj= Movie_details.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':obj})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('movie_name',)
        desc = request.POST.get('movie_desc', )
        year = request.POST.get('movie_year', )
        img = request.FILES['movie_image']
        movie=Movie_details(movie_name=name,movie_desc=desc,movie_year=year,movie_image=img)
        movie.save()
    return render(request,"add.html")
def update_movie(request,movie_id):
    movie=Movie_details.objects.get(id=movie_id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movie})
def delete_movie(request,movie_id):
    if request.method=='POST':
        movie=Movie_details.objects.get(id=movie_id)
        movie.delete()
        return  redirect('/')
    return render(request,"delete.html")