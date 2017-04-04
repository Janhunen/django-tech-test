from django import forms

from .models import Application

class ContactForm(forms.Form):
        full_name = forms.CharField(required=False)
        email = forms.EmailField()
        message = forms.CharField()


class ApplicationForm(forms.ModelForm):
        class Meta:
                model = Application
                fields = ['company_name','company_number','telephone', 'amount', 'sector','duration','email']

        def clean_email(self):
                email = self.cleaned_data.get('email')
                email_base, provider = email.split("@")
                domain, extension = provider.split('.')
                return email
	
	def clean_sector(self):
		sector = self.cleaned_data.get('sector')
		return sector 

        def clean_full_name(self):
                full_name = self.cleaned_data.get('full_name')
                return full_name

        def clean_telephone(self):
                telephone = self.cleaned_data.get('telephone')
                return telephone

        def clean_company_name(self):
                company_name = self.cleaned_data.get('company_name')
                return company_name

        def clean_company_number(self):
                company_number = self.cleaned_data.get('company_number')
                return company_number


        def clean_amount(self):
                amount = self.cleaned_data.get('amount')
                return amount

        def clean_duration(self):
                duration = self.cleaned_data.get('duration')
                return duration
