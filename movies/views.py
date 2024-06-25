from django.shortcuts import render
from .models import Movie
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query) | Q(genre__icontains=query))
    else:
        movies = Movie.objects.all()
    
    paginator = Paginator(movies, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})


def movie_detail(request, pk):
    movie = Movie.objects.filter(pk=pk).first()
    if movie is None:
        return render(request, '404.html', status=404)
    return render(request, 'detail.html', {'movie': movie})
