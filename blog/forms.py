from .models import Comment, Profile, Post
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs=('class': 'form-control', 'type': 'password')))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs=('class': 'form-control', 'type': 'password')))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs=('class': 'form-control', 'type': 'password')))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email')



# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('favourite_quote', 'likes', 'dislikes', 'about', 'profile_pic')

#         widgets = {
#             'favourite_quote': forms.TextInput(attrs={'class': 'form-control'}),
#             'likes': forms.TextInput(attrs={'class': 'form-control'}),
#             'dislikes': forms.TextInput(attrs={'class': 'form-control'}),
#             'about': forms.Textarea(attrs={'class': 'form-control'}),
#             'profile_pic': forms.FileInput(attrs={'class': 'form-control-file'}),
#         }

    # profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # favourite_quote = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # likes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # dislikes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-file'})
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-file'}),

        }