from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'feed/index.html')

@login_required
def profile(request,username):
    return render(request, 'feed/profile.html', {'username':username})
