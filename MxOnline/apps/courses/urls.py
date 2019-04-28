# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__date__ = '2018/6/1 22:01'

from django.urls import path, include, re_path
from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView

app_name = 'courses'   # 使用命名空间

urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name="course_list"),
    # 课程详情页
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name='course_detail'),

    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='course_info'),
    # 课程评论
    re_path('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name='course_comments'),
    # 添加课程评论
    path('add_comment/', AddCommentsView.as_view(), name='add_comment'),

    re_path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name='video-play'),

]


