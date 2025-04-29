from django.contrib import admin
from django.urls import path
from students.views import welcome_page, student_list

urlpatterns = [
    path('', welcome_page, name='home'),  # الصفحة الرئيسية الترحيبية
    path('admin/', admin.site.urls),  # لوحة التحكم
    path('students/', student_list, name='student-list'),  # قائمة الطلاب
]
