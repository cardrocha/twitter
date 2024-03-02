from django import forms
from feed.models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class TweetForm(forms.ModelForm):
  body = forms.CharField(
    required=True,
    widget=forms.widgets.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Poste seu tweet...'
        }
    ),
    label=""
  )
  
  class Meta:
    model = Tweet
    exclude = ("user",)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Obrigatório. 150 caracteres ou menos. Apenas letras, dígitos e @/./+/-/_ são permitidos.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser muito semelhante às suas outras informações pessoais.</li><li>Sua senha não pode ser uma senha que é frequentemente utilizada.</li><li>A sua senha não pode ser completamente numérica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a Senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Digite a mesma senha novamente, para verificação.</small></span>'
        
class ProfileForm(forms.ModelForm):
    bio = forms.CharField(
        label="Biografia",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva uma biografia até 60 palavras...'}),
        required=False,
    )
    profile_image = forms.ImageField(label="Profile Picture")


    class Meta:
        model = Profile
        fields = ('bio','profile_image')