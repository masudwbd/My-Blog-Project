from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required
def index(request):
    return HttpResponseRedirect(reverse('App_Blog:BlogList'))