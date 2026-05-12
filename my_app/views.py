from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from .models import *

def about_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Good👌")
            return redirect("home")
    else:
        form=ContactForm()

    context={'form':form,
             'port':Portfolio.objects.all(),
             'h':Home.objects.last(),
             'ab':About.objects.last(),
             's':Service.objects.all()}
    return render(request,"index.html",context)
# Create your views here.
