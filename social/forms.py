from django import forms
from datetime import datetime, date
from django.forms import extras
from .models import SocialUser, Comment, Interests

from django.contrib.auth.models import User


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

user = get_user_model()


class RegistrationForm(forms.Form):
    email_ver = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    b_day = forms.DateField(widget=extras.SelectDateWidget(years=range(1939, datetime.now().year)), required=True)
    gender = forms.CharField(widget=forms.RadioSelect(
        choices=SocialUser.GENDER_CHOICES
    ), required=True)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email_ver')
        print email
        print email2
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email).first()
        if email_qs:
            raise forms.ValidationError("This email has already been registered")
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        print password
        # user = authenticate(username=email, password=password)

        user_qs = User.objects.filter(email=email).first()
        print user_qs, "yolo"
        if not user_qs:
           raise forms.ValidationError("This user does not exist")
        else:
            # user = authenticate(username=email, password=password)
            if not user_qs.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user_qs.is_active:
                raise forms.ValidationError("This user is not longer active")

        return super(LoginForm, self).clean(*args, **kwargs)


class PostForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "body",
            "post"
        ]


class InterestsForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields = [
            "name",
            "category",
            "img"
        ]
