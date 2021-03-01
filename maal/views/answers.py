from ..serializers.answers import AnswersSerializer
from ..models.answers import Answers
from rest_framework_json_api.views import ModelViewSet
from rest_framework import mixins


class AnswersViewSet(ModelViewSet):
	queryset = Answers.objects.all()
	serializer_class = AnswersSerializer
