from django.urls import path
from app.views import *
from rest_framework.urlpatterns import format_suffix_patterns

# APP - URLS #

urlpatterns = [
    path('app/',PipeList.as_view()),
    path('app/<int:pk>/',PipeDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)