from django import forms


class CreatePollForm(forms.Form):
    duration = forms.IntegerField(max_value=59, min_value=1)
    start = forms.BooleanField(required=False)
    question = forms.CharField(max_length=200, widget=forms.Textarea())
    option_1 = forms.CharField(max_length=100, widget=forms.TextInput())
    option_2 = forms.CharField(max_length=100, widget=forms.TextInput())
    option_3 = forms.CharField(max_length=100, widget=forms.TextInput(), required=False)
    option_4 = forms.CharField(max_length=100, widget=forms.TextInput(), required=False)
    option_5 = forms.CharField(max_length=100, widget=forms.TextInput(), required=False)
    option_6 = forms.CharField(max_length=100, widget=forms.TextInput(), required=False)
