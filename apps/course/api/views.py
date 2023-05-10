from rest_framework import generics, status, permissions
from ..models import Course, Lesson, LessonFiles, SoldCourse
from .serializers import CoursePOSTSerializer, CourseGETSerializer, LessonGETSerializer, LessonPOSTSerializer, \
        CourseDetailSerializer, LessonFilesGETSerializer, LessonFilesPOSTSerializer, SoldCourseSerializer


class CourseListCreate(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/course/api/course-list-create/
    queryset = Course.objects.all()
    serializer_class = CourseGETSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CoursePOSTSerializer
        return super().get_serializer_class()


class CourseRUD(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/course/api/{course_id}
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LessonListCreate(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/course/api/{course_id}/lesson-list-create
    queryset = Lesson.objects.all()
    serializer_class = LessonGETSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LessonPOSTSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.kwargs.get('course_id')
        qs = qs.filter(course_id=course_id)
        return qs

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['course_id'] = self.kwargs.get('course_id')
        return ctx


class LessonRUD(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/course/api/{course_id}/lesson-rud/{lesson_id}
    queryset = Lesson.objects.all()
    serializer_class = LessonGETSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LessonFilesListCreate(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/course/api/{course_id}/lessons/{lesson_id}/lesson-file-list-create/
    queryset = LessonFiles.objects.all()
    serializer_class = LessonFilesGETSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LessonFilesPOSTSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = super().get_queryset()
        lesson_id = self.kwargs.get('lesson_id')
        qs = qs.filter(lesson_id=lesson_id)
        return qs

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['lesson_id'] = self.kwargs.get('lesson_id')
        return ctx


class LessonFilesRUD(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/course/api/{course_id}/lessons/{lesson_id}/lesson-file-list-create/{file_id}
    queryset = LessonFiles.objects.all()
    serializer_class = LessonFilesGETSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MyCourseListCreate(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/course/api/my-course/
    queryset = SoldCourse.objects.all()
    serializer_class = SoldCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user_id = self.request.user.id
        if qs:
            qs = qs.filter(profile_id=user_id)
            return qs
        return []







