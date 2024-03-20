from django.shortcuts import render
from .models import About
from .forms import AboutContactForm
from django.contrib import messages


def about_bakershub(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        contact_form = AboutContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                 request, messages.SUCCESS,
                 "Message received! We will respond as soon as possible!")
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = AboutContactForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "contact_form": contact_form},
    )
