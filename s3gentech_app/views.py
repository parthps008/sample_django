from django.shortcuts import render
from .models import CompanyInfo, Service, ContactSubmission
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'home.html', {'company_info': company_info})

def about_us(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'about_us.html', {'company_info': company_info})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contact_us(request):
    if request.method == 'POST':
        # Handle form submission here and save to the database
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        from_email = settings.EMAIL_HOST_USER  # Get the sender's email from settings
        recipient_list = [settings.EMAIL_HOST_USER]  # List of recipients (you can change this)
        send_mail(
            'Your Subject Here',
            message,
            from_email,
            recipient_list,
            fail_silently=False
        )
    return render(request, 'contact_us.html')
