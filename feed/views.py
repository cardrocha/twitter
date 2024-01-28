from django.shortcuts import get_object_or_404, render, redirect
from .models import NewTweet
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def feed(request):
  if not request.user.is_authenticated:
      return redirect('/usuarios/logar')

  if request.method == "GET":
      tweets = NewTweet.objects.all().order_by('-id')
      return render(request, 'feed.html', {'tweets': tweets})

  elif request.method == "POST":
      tweet_text = request.POST.get('feed')

      if len(tweet_text.strip()) == 0:
          messages.add_message(request, messages.ERROR, "O campo de texto não pode estar vazio, digite algo!")
          return redirect('/feeds/feed')
      
      tweet = NewTweet(user=request.user, tweet=tweet_text)
      tweet.save()

      messages.add_message(request, messages.SUCCESS, "Tweet postado!")
      return redirect('/feeds/feed')
  
def deletar_tweet(request, id):
    tweet = get_object_or_404(NewTweet, id=id)

    if tweet.user == request.user:
        tweet.delete()
        messages.add_message(request, constants.SUCCESS, 'Tweet deletado com sucesso!')
        return redirect('feed')
    else:
        messages.add_message(request, constants.ERROR, 'Você não tem permissão para excluir este tweet.')
        return redirect('feed')
    
def logout(request):
  auth.logout(request)
  return redirect('/usuarios/logar')