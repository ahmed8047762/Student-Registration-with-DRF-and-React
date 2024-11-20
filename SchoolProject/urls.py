from django.contrib import admin
from django.urls import path
from StudentApp import views

urlpatterns = [
    path('student/', views.StudentListCreate.as_view(), name='student-list-create'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
    path('admin/', admin.site.urls),
]