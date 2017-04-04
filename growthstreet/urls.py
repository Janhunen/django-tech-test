from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
	url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url(r'^admin/', admin.site.urls),
	url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^finance/', include('demo.urls'))
]
