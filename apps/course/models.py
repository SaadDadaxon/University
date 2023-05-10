from django.db import models
from apps.main.models import Category, Tag
from ckeditor.fields import RichTextField
from django.conf import settings
Profile = settings.AUTH_USER_MODEL


class Timestamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def course_page(instance, filename):
    return f'courses/{instance.id}/cover/{filename}'


class Course(Timestamp):
    DIFFICULTY = (
        (0, 'Beginner'),
        (1, 'intermediate'),
        (2, 'Advanced'),
    )
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 1})
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=228)
    cover = models.ImageField(upload_to=course_page, null=True)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0, null=True, blank=True)
    body = RichTextField()
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    discount_price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    is_free = models.BooleanField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


def file_path(instance, filename):
    return f'courses/{instance.lesson.course.title}/{instance.lesson.title}/{filename}'


class Lesson(Timestamp):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=228)
    body = RichTextField()

    def __str__(self):
        return self.title


class LessonFiles(Timestamp):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_file')
    files = models.FileField(upload_to=file_path)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson.title


class SoldCourse(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'role': 0})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile} -> {self.course.title}'




