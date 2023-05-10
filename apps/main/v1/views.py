from django.shortcuts import render, redirect
from ..models import Category, Contact, Tag, Answer, FAQ
from apps.course.models import Course
from apps.blog.models import Post
from .forms import ContactForm
from django.conf import settings
Profile = settings.AUTH_USER_MODEL


def about(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'main/about.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:contact')
    context = {
        "form": form
    }
    return render(request, 'main/contact.html', context)


def index(request):
    categories = Category.objects.all()
    randomly_5_courses = Course.objects.order_by('?')[:5]
    profiles = Profile.objects.filter(role=1).order_by('?')[:3]
    last_post = Post.objects.last()
    resent_posts = Post.objects.exclude(id=last_post.id).order_by('-id')[:4]
    context = {
        'randomly_5_courses': randomly_5_courses,
        'categories': categories,
        'profiles': profiles,
        'resent_posts': resent_posts,
        'last_post': last_post,
    }
    return render(request, 'main/index.html', context)
