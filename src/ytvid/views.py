from django.shortcuts import render

# Create your views here.

# create retrieve update delete

#list



def main_view(request):
	context = {}
	return render(request, "index.html", context)