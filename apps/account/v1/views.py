from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from .forms import SignUpForm
from apps.course.models import Course, SoldCourse
from django.conf import settings
Profile = settings.AUTH_USER_MODEL


# Sign Up View
class RegisterView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main:index')
    return render(request, 'account/logout.html')


def profile_info(request):
    user_id = request.user.profile.id
    profile = Profile.objects.get(user_id=user_id)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile_info.html', context)


def profile_update(request, pk):
    user = request.user
    profile = Profile.objects.get(user_id=user)
    if request.method == "POST":
        email = request.POST.get('email', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        bio = request.POST.get('bio', None)
        image = request.FILES.get('image', None)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        profile.bio = bio
        if image:
            profile.image = image

        user.save()
        profile.save()
        return redirect('account:profile_info')

    context = {
        'profile': profile
    }
    return render(request, 'account/profile_update.html', context)


def my_courses(request):
    profile_id = request.user.profile.id
    courses = SoldCourse.objects.filter(profile_id=profile_id)
    context = {
        'courses': courses
    }
    return render(request, 'account/my_courses.html', context)

