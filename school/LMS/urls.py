from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('action',views.action_lms,name='LMS_choose_action')
              ] + static(settings
                         .MEDIA_URL, document_root=settings.MEDIA_ROOT)