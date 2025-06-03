from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm

def landing_page(request):
    films = Film.objects.all()
    return render(request, 'film/landing.html', {'films': films})

def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    reviews = film.reviews.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.film = film
                review.user = request.user
                review.save()
                return redirect('film_detail', film_id=film.id)
        else:
            return redirect('login')
    else:
        form = ReviewForm()

    return render(request, 'film/film_detail.html', {
        'film': film,
        'reviews': reviews,
        'form': form,  
    })

@login_required
def add_review(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.film = film
            review.user = request.user
            review.save()
            return redirect('film_detail', film_id=film.id)
    else:
        form = ReviewForm()
    return render(request, 'film/add_review.html', {'form': form, 'film': film})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('landing')
    else:
        form = AuthenticationForm()
    return render(request, 'film/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Arahkan ke login setelah berhasil daftar
    else:
        form = UserCreationForm()
    return render(request, 'film/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')



