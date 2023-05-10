from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Course, Lesson, LessonFiles, SoldCourse
from apps.main.api.serializers import CategorySerializer, TagSerializer


class CourseGETSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = Course
        fields = ('id', 'author', 'category', 'title', 'cover', 'difficulty', 'get_difficulty_display', 'body', 'price', 'discount_price', 'is_free', 'tags', 'created_date', 'modified_date')


class CoursePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'author', 'category', 'title', 'cover', 'difficulty', 'get_difficulty_display', 'body', 'price', 'discount_price', 'is_free', 'tags', 'created_date', 'modified_date')

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        instance = super().create(validated_data)
        instance.author_id = user_id
        instance.save()
        return instance


class MiniLessonFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFiles
        fields = ('id', 'files', 'is_main', 'created_date')


class MiniLessonSerializer(serializers.ModelSerializer):
    lesson_file = MiniLessonFilesSerializer(read_only=True, many=True)

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'body', 'lesson_file', 'created_date')


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    tags = TagSerializer(required=False, many=True)
    lessons = MiniLessonSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ('id', 'author', 'category', 'title', 'cover', 'difficulty', 'get_difficulty_display', 'body', 'price', 'discount_price', 'is_free',
                  'tags', 'lessons', 'created_date', 'modified_date')


class LessonGETSerializer(serializers.ModelSerializer):
    course = CourseGETSerializer(read_only=True)
    lesson_file = MiniLessonFilesSerializer(read_only=True, many=True)

    class Meta:
        model = Lesson
        fields = ('id', 'course', 'title', 'body', 'lesson_file')


class LessonPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'body')
        extra_kwargs = {
            'course': {'read_only': True},
        }

    def create(self, validated_data):
        course_id = self.context['course_id']
        instance = Lesson(**validated_data)
        instance.course_id = course_id
        instance.save()
        return instance


class LessonFilesGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFiles
        fields = ('id', 'lesson', 'files', 'is_main', 'created_date')


class LessonFilesPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFiles
        fields = ('id', 'lesson', 'files', 'is_main', 'created_date')
        # extra_kwargs = {
        #     'lesson': {'read_only': True},
        # }

    def create(self, validated_data):
        lesson_id = self.context['lesson_id']
        instance = LessonFiles(**validated_data)
        instance.lesson_id = lesson_id
        instance.save()
        return instance


class SoldCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldCourse
        fields = ('id', 'course', 'profile', 'created_date')
        extra_kwargs = {
            'profile': {'read_only': True},
        }

    def validate(self, attrs):
        request = self.context['request']
        user_id = request.user.id
        course = attrs.get('course')
        my_courses = SoldCourse.objects.filter(profile_id=user_id)
        if (course.id, ) in my_courses.values_list('course'):
            raise ValidationError('already sold')
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        instance = SoldCourse(**validated_data)
        instance.profile_id = user_id
        instance.save()
        return instance



