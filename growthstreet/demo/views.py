from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext
from .forms import ContactForm, ApplicationForm
from .models import Application

def handle404(request):
        response = render_to_response('404.html', {}, context_instance=RequestContext(request))
        response.status_code = 404
        return response

@login_required(login_url="/accounts/login/")
def testing(request):
        return HttpResponse("<h2>Hey!</h2>")

def save_form_data(request):
        if request.method == 'POST':
                form = ApplicationForm(request.POST)
                if form.is_valid():
                        form.save()
        return HttpResponse("<h2>Data Saved</h2>")

@login_required(login_url="/accounts/login/")
def home(request):
        title = 'Sign Up Now'
        form = ApplicationForm(request.POST or None)
        context = {
                "title": title,
                "form": form
        }
        if form.is_valid():
                form.save()
                instance = form.save(commit=False)
                instance.save()
                context = {
                        "title": "Thank you"
                }
                return HttpResponse("<h2>Data Saved</h2>")
        return render(request, "home.html", context)



def contact(request):
        title = 'Contact Us'
        title_align_center = True
        form = ContactForm(request.POST or None)
        if form.is_valid():
                form_email = form.cleaned_data.get("email")
                form_message = form.cleaned_data.get("message")
                form_full_name = form.cleaned_data.get("full_name")
                subject = 'Site contact form'
                from_email = settings.EMAIL_HOST_USER
                to_email = [from_email, 'youotheremail@email.com']
                contact_message = "%s: %s via %s"%(
                                form_full_name,
                                form_message,
                                form_email)
                some_html_message = """
                <h1>hello</h1>
                """
                send_mail(subject,
                                contact_message,
                                from_email,
                                to_email,
                                html_message=some_html_message,
                                fail_silently=True)

        context = {
                "form": form,
                "title": title,
                "title_align_center": title_align_center,
        }
        return render(request, "forms.html", context)


