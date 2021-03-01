from django.contrib import admin

# Register your models here.

from .models.questions import Questions
from .models.answers import Answers


class QuestionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Questions, QuestionsAdmin)


class AnswersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answers, AnswersAdmin)