from django.contrib import admin
from .forms import ApplicationForm
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
        list_display = ["__unicode__","company_name","company_number","telephone","amount", "purpose","duration", "timestamp", "updated"]
        form = ApplicationForm
        class Meta:
                model = Application

admin.site.register(Application, ApplicationAdmin)
