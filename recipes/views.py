
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe,  Comment
from .forms import RecipeForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  , authenticate,logout
from django.contrib.auth.forms import AuthenticationForm



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/signup.html', {'form': form})



def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = Comment.objects.filter(recipe=recipe)
    
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'comments': comments})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')

def add_comment(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = CommentForm()
    return render(request, 'recipes/add_comment.html', {'form': form})
def search(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(title__icontains=query)
    return render(request, 'recipes/search_results.html', {'recipes': recipes, 'query': query})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'templates/registration/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')


