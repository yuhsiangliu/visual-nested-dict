from django import forms

class EnterCode(forms.Form):
	code = forms.CharField(label='', widget=forms.Textarea(attrs={"rows":25, "cols":80}))