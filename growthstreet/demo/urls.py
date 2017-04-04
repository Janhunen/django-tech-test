from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^t/', views.testing, name='testing'),
url(r'^application/', views.home, name='home'),
url(r'^savedata/', views.save_form_data, name='save_form_data')
]
