from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('<int:pk>/new_comment', views.NewComment.as_view(), name='new_comment'),
]
