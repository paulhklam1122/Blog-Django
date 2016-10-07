from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from .views import CommentListAPIView, CommentDetailAPIView

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<id>\d+)/delete/$', views.comment_delete, name='delete'),
]
