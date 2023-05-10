from rest_framework import serializers
from ..models import Category, Tag, FAQ, Contact, Subscribe, Answer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
    #
    # def to_representation(self, instance):
    #     data = super(CategorySerializer, self).to_representation(instance)
    #     return data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'body', 'created_date')


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('id', 'email')


class MiniAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer')


class FAQGETSerializer(serializers.ModelSerializer):
    answer = MiniAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')


class FAQPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question')


class AnswerGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer')


class AnswerPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer')

    def create(self, validated_data):
        request = self.context['request']
        question_id = self.context['question_id']
        user_id = request.user.id
        instance = Answer(question_id=question_id, **validated_data)
        instance.profile_id = user_id
        instance.save()
        return instance

