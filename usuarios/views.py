from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import TweetForm
from feed.models import Tweet
from .models import Profile
from .forms import TweetForm, SignUpForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
  if request.user.is_authenticated:
    form = TweetForm(request.POST or None)
    if request.method == 'POST':
      if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        messages.success(request, "Tweet postado com sucesso!")
        return redirect('home')
    
    tweets = Tweet.objects.filter().order_by("-created_at")
    return render(request, 'home.html', {"tweets": tweets, "form":form})
  else:
    messages.error(request, "Você deve estar logado para visualizar a página de twitters	.")
    return redirect('login')
def profile_list(request):
  if request.user.is_authenticated:
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html', {'profiles': profiles})
  else:
    messages.error(request, "Você deve estar logado para visualizar a página de perfis.")
    return redirect('login')
  
def profile(request, pk):
  if request.user.is_authenticated:
    profile = Profile.objects.get(user_id=pk)
    tweets = Tweet.objects.filter(user_id=pk).order_by("-created_at")

    if request.method == "POST":
      current_user_profile = request.user.profile
      action = request.POST['follow']
      if action == 'unfollow':
          current_user_profile.follows.remove(profile)
          messages.success(request, f"Você parou de seguir {profile.user.username}.")
      elif action == 'follow':
          current_user_profile.follows.add(profile)
      current_user_profile.save()
      messages.success(request, f"Você está seguindo {profile.user.username}.")

      return render(request, 'profile.html', {"profile": profile, "tweets": tweets})
    else:
      return render(request, 'profile.html', {"profile": profile, "tweets": tweets}) 
  else:
    messages.error(request, "Você deve estar logado para visualizar a página de perfil.")
    return redirect('profile')


def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Logado com sucesso!")
        return redirect('home')
    else:
        messages.error(request, "Usuário ou senha inválidos.")
        return redirect('login')
  else:
      return render(request, 'login.html', {})

def logout_user(request):
  logout(request)
  messages.error(request, "Você desconectou do Twitter!")
  return redirect('login')

def cadastro_user(request):
  if request.user.is_authenticated:
      return redirect('home')

  user = None 
  
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save() 
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']

      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user) 
      else:
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('login')  
  else:
      form = SignUpForm()
  return render(request, 'cadastro.html', {'form': form})

def update_perfil(request):
  if request.user.is_authenticated:
    current_user = User.objects.get(id=request.user.id)
    profile_user = Profile.objects.get(user__id=request.user.id)
    if request.method == 'POST':
      profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_user)
      if profile_form.is_valid():
        profile_form.save()
        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect('home')
    else:
        profile_form = ProfileForm(instance=current_user.profile)
    return render(request, 'update_perfil.html', {'profile_form': profile_form})
  else:
    messages.error(request, "Usuário precisa estar logado para visualizar esta página!")
    return redirect('home')

def delete_tweet(request, id):
    tweet = get_object_or_404(Tweet, id=id)

    if tweet.user == request.user:
        tweet.delete()
        messages.success(request,  'Tweet deletado com sucesso!')
        return redirect('home')
    else:
        messages.error(request, 'Você não tem permissão para excluir este tweet.')
        return redirect('home')