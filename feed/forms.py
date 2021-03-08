from django import forms
from .models import * 

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150,required=False)
    class Meta:
        model = Profile
        fields = ('bio','image')

        widget = {
            'bio': forms.TextInput(attrs={'placeholder':'Bio'}),
            'image': forms.FileInput()
        }

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields  = ('image','description')

        widget = {
            'description':forms.TextInput(),
            'image': forms.FileInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)
        
        widget = {
            'description':forms.TextInput()
        }