from django.shortcuts import render
from django.http import HttpResponse

from .forms import EnterCode
from .VisualNestedDict import VisualNestedDict, Node

# Create your views here.

def index(response):
	return HttpResponse("Hello, <b>world</b>!")

def v1(response):
	return HttpResponse("<h1>Title V.1</h1>")


form = """
<form action='http://www.google.com/search'>
	<input name='q'>
	<input type='submit'>
</form>
"""

def search(response):
	return HttpResponse(form)

def main(response):
	para = {"text": [], "root": None}
	if response.method=="POST":
		para["form"] = EnterCode(response.POST)
		if para["form"].is_valid():
			print(para["form"].cleaned_data)
			code = para["form"].cleaned_data['code']
			VND = VisualNestedDict(name="DefaultName")
			VND.load_json(str(code))
			VND.text()
			para["text"] = VND.result
			para["root"] = VND.root
	else:
		para["form"] = EnterCode()
	return render(response, "main/web.html", para)

def tree(response):
	return render(response, "main/tree.html")

def test(response):
	return render(response, "main/web.html")