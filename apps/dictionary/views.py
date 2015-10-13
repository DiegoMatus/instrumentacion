from django.shortcuts import render
from apps.dictionary.models import Instrumentation

# Create your views here.
def index(request):
	instruments = Instrumentation.objects.all()
	context = {'instruments': instruments}
	return render(request, 'index.html', context)