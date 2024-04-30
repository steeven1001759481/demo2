# importing django routing libraries
from . import views
from django.urls import path, include
from .views import *
# from .feeds import blogFeed

urlpatterns = [
	# home page
	path('', views.postslist.as_view(), name='posts'),
	# route for posts
	path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
]
