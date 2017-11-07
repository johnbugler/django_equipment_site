from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from .models import Device

class MyUser(AbstractUser):
    pass

USERNAME_LENGTH = 10
MyUser._meta.get_field('username').max_length = USERNAME_LENGTH
MyUser._meta.get_field('username').validators[0].limit_value = USERNAME_LENGTH
MyUser._meta.get_field('username').validators[1].limit_value = USERNAME_LENGTH
UserCreationForm.base_fields['username'].max_length = USERNAME_LENGTH
UserCreationForm.base_fields['username'].validators[0].limit_value = USERNAME_LENGTH

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = 'Maximum of 10 characters'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters'
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class NewDeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('equipment', 'description', 'location', 'email', )