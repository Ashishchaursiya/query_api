from .models import Question,Answer
from rest_framework import serializers


class QuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question']


class AnsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['QuestionID','answer']