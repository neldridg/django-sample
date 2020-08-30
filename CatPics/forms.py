from django import forms
from CatPics.models import Pic


class PicForm(forms.ModelForm):
    class Meta:
        model = Pic
        fields = {'image'}
