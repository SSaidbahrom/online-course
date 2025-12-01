from django.contrib import admin
from django.urls import path
from course_app import views

app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('teacher/', views.teacher, name='teacher'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
]
