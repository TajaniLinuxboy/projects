from django import forms

class FeedBackForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=50, required=True)
    lastname = forms.CharField(label='Last Name', max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    comment = forms.CharField(widget=forms.Textarea, label="Comment", required=True)
