from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Importa tu modelo personalizado

class CustomUserCreationForm(UserCreationForm):

    tipo_usuario = forms.ChoiceField(
        choices=CustomUser.TIPO_USUARIO_CHOICES,
        label="Tipo de Usuario",
        required=True,
        widget=forms.Select(attrs={'class': 'custom-select'}),
    )

    # Nuevo campo para la imagen de perfil
    profile_picture = forms.ImageField(
        required=False,  # Esto permite que el campo sea opcional
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label="Imagen de Perfil"
    )

    class Meta:
        model = CustomUser  # Usa tu modelo personalizado en lugar de User
        fields = ['username', 'tipo_usuario', 'first_name', 'last_name', 'profile_picture', 'email', 'password1', 'password2']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'tipo_usuario', 'profile_picture', 'first_name', 'last_name', 'email']
