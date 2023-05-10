from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, View
from ..models import Post, Comment
from apps.main.models import Category, Tag
from apps.course.models import Course


# def blog_views(request):
#     context = {
#
#     }
#     return render(request, 'blog/blog.html', context)

#
# def blog_single(request):
#     context = {
#
#     }
#     return render(request, 'blog/blog-single.html', context)


class BlogView(ListView):
    queryset = Post.objects.all()
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['resent_courses'] = Course.objects.order_by('-id')[:3]
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        cate = self.request.GET.get('cate')
        tag = self.request.GET.get('tag')
        q_conditions = Q()
        if q:
            q_conditions = Q(title__icontains=cate)
        cate_conditions = Q()
        if cate:
            cate_conditions = Q(category__title__exact=cate)
        tag_conditions = Q()
        if tag:
            tag_conditions = Q(tags__title__exact=tag)
        qs = qs.filter(q_conditions, cate_conditions, tag_conditions)
        return qs


class BlogDetailView(View):
    template_name = 'blog/blog-single.html'
    queryset = Post.objects.all()

    def get_object(self, pk):
        try:
            post = self.queryset.get(id=pk)
        except Post.DoesNotExist:
            raise Http404
        return post

    def get_context_data(self, pk):
        categories = Category.objects.all()
        tags = Tag.objects.all()
        resent_courses = Course.objects.order_by('-id')[:3]
        context = {
            'object': self.get_object(pk),
            'categories': categories,
            'tags': tags,
            'resent_courses': resent_courses,
        }
        return context

    def get(self, request, pk):

        context = self.get_context_data(pk)
        comments = Comment.objects.filter(post_id=pk, parent_comment__isnull=True)
        context['comments'] = comments
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        context = self.get_context_data(pk)

        if not request.user.is_authenticated:
            return redirect('account:login')

        comment_id = request.GET.get('comment_id', None)
        user_id = request.user.id
        body = request.POST.get('body')
        if body:
            obj = Comment.objects.create(author_id=user_id, post_id=pk, body=body, parent_comment_id=comment_id)
            return redirect(reverse('blog:blog_detail', kwargs={'pk': pk}) + f'#comment_{obj.id}')
        return render(request, self.template_name, context)
