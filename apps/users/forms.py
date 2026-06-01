from django import forms
from .models import User, Profile
from cloudinary.forms import CloudinaryFileField

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "input w-full"}),
            "last_name": forms.TextInput(attrs={"class": "input w-full"}),
        }


class EditProfile(forms.ModelForm):
    avatar = CloudinaryFileField(required=False)
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]
        widgets = {
            "bio": forms.Textarea(attrs={"class": "textarea w-full"}),
        }
