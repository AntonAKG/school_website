from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import main_menu, Teacher_list, lesson_timetable, call_schedule, Show_Teacher, NewsDeteilView

urlpatterns = [
                path('', main_menu, name='main_menu'),
                path('teacher', Teacher_list.as_view(), name='teacher_list'),
                path('lesson_timetable', lesson_timetable, name='lesson_timetable'),
                path('call_schedule', call_schedule, name='call_schedule'),
                path('<int:pk>', NewsDeteilView.as_view(), name='NewsDeteilView'),
                path('teacher/<slug:slug>/', Show_Teacher.as_view(), name='data_teacher')
              ] + static(settings
                         .MEDIA_URL, document_root=settings.MEDIA_ROOT)
