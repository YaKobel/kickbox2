from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('contact.html', views.contact, name="contact"),
	path('about.html', views.about, name="about"),
	path('feder.html', views.pricing, name="feder"),
	path('sport.html', views.service, name="sport"),
	path('appointment.html', views.appointment, name="appointment"),

	path('blog.html', views.ShowNewsView.as_view(), name="blog"),
	path('user/<str:username>/', views.UserAllNewsView.as_view(), name="user-news"),
	path('news/<int:pk>/', views.NewsDetailView.as_view(), name="news-detail"),
	path('news/add/', views.CreateNewsView.as_view(), name="news-add"),
	path('news/<int:pk>/update/', views.UpdateNewsView.as_view(), name="news-update"),
	path('news/<int:pk>/delete/', views.DeleteNewsView.as_view(), name="news-delete"),
	path('blog.html', views.blog, name="blog"),

]
