from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h4>Checking the work<h4>")