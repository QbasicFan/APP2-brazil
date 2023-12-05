from django import forms
from .models import listWord, Info

class listWordForm(forms.ModelForm):
    class Meta:
        model = listWord
        fields = ['en','bra','liked']


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title','text','img']



