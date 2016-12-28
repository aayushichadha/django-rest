from django import forms

class PostForm(forms.Form):

    num = forms.IntegerField(label= 'Number')