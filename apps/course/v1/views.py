from django.shortcuts import render
from ..models import Course, Lesson, LessonFiles
from django.views import generic

from ...main.models import Category, Tag


# def course_views(request):
#     context = {
#
#     }
#     return render(request, 'course/courses.html', context)
#
#
# def course_single(request):
#     context = {
#
#     }
#     return render(request, 'course/course-single.html', context)


class CourseListView(generic.ListView):
    queryset = Course.objects.all()
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['resent_courses'] = Course.objects.order_by('-id')[:3]
        return context


class CourseDetailView(generic.DetailView):
    queryset = Course.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['resent_courses'] = Course.objects.order_by('-id')[:3]
        context['resent_6_courses'] = Course.objects.order_by('-id')[:6]
        return context


def course_lesson(request, course_id, pk):
    lesson = Lesson.objects.get(id=pk)
    main_lesson = LessonFiles.objects.filter(lesson_id=pk, is_main=True).first()
    # course = Course.objects.get(id=course_id)
    context = {
        'lesson': lesson,
        'main_lesson': main_lesson,
        # 'course': course,
    }
    return render(request, 'course/course_lesson.html', context)
