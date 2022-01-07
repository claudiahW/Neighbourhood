from .models import NeighborHood, Profile, Business ,Post
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['bio', 'profile_pic', 'contact','location','neighborhood']

class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        fields = ['admin','occupants_count']
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields=['business_name','email','description','location','neighborhood']  

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title','image','content','location','neighborhood']       


        




