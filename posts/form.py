from django import forms
from .models import Posts


class WriteForm(forms.ModelForm):
    class Meta:
        # モデルを指定
        model = Posts
        fields = ('task',)
