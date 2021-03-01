# from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'answers', views.AnswersViewSet, basename='answers')
urlpatterns = router.urls

