from django import forms

from .models import *


class PostFormOne(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'




class PostFormTwo(forms.Form):
    choice_mas = [
        (1, 'Москва'), (2, 'Санкт-Петербург'), (3, 'Нижний Новгород'), (4, 'Самара'), (5, 'Ростов')
    ]
    bool = forms.BooleanField()
    date = forms.DateField()
    file = forms.FileField()
    choice = forms.ChoiceField(choices=choice_mas)
