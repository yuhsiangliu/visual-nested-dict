from django import forms

in_fm = (("JSON", "JSON"), ("Python", "Python"), ("Url", "Url"))
ou_ty = (("Tree", "Tree"), ("Text", "Text"))
ou_fm = (("JSON", "JSON"), ("Python", "Python"))

class EnterCode(forms.Form):
	obj_name = forms.CharField(label='Name', max_length=50, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	input_format = forms.ChoiceField(label="Input Format", choices=in_fm, widget=forms.Select(attrs={"class": "form-control"}))
	code = forms.CharField(label='', max_length=5000, widget=forms.Textarea(attrs={"rows":16, "class": "form-control", "style":"resize:none;"}))
	output_type = forms.ChoiceField(label="Output", choices=ou_ty, widget=forms.Select(attrs={"class": "form-control"}))
	output_format = forms.ChoiceField(label="", choices=ou_fm, widget=forms.Select(attrs={"class": "form-control"}))