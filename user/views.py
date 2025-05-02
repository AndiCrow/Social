from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, StoryboardForm
from .models import Profile, Storyboard, Friendship

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'user/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('homepage')
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'user/edit_profile.html', {'profile_form': profile_form})
@login_required
def homepage(request):
    if request.method == 'POST':
        form = StoryboardForm(request.POST, request.FILES)
        if form.is_valid():
            storyboard = form.save(commit=False)
            storyboard.user = request.user
            storyboard.save()
            return redirect('homepage')
    else:
        form = StoryboardForm()
    storyboards = Storyboard.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user/homepage.html', {'form': form, 'storyboards': storyboards})
