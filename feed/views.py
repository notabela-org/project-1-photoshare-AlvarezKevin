from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from feed.models import Profile

# Create your views here.
@login_required
def index(request):
    return render(request, 'feed/index.html')

@login_required
def profile(request,username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except ObjectDoesNotExist:
        profile = None
    return render(request, 'feed/profile.html', {'profile':profile,'username':user.get_username()})
