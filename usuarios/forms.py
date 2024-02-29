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

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}),
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        help_text='<ul class="form-text text-muted small"><li>Sua senha não pode ser muito semelhante às suas outras informações pessoais.</li><li>"Sua senha deve conter pelo menos 8 caracteres."</li><li>"Sua senha não pode ser uma senha que é frequentemente utilizada."</li><li>"A sua senha não pode ser completamente numérica."</li></ul>',
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a Senha'}),
        help_text='<span class="form-text text-muted"><small class="text-white">"Digite a mesma senha novamente, para verificação."</small></span>',
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = '<span class="form-text text-muted"><small class="text-white">Obrigatório. 150 caracteres ou menos. Apenas letras, dígitos e @/./+/-/_ são permitidos.</small></span>'

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(
        label="Biografia",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bibliografia'}),
        required=False,
    )
    profile_image = forms.ImageField(label="Profile Picture")


    class Meta:
        model = Profile
        fields = ('bio','profile_image')