from django.shortcuts import render, redirect
from .forms import CustomCreationForm

# Create your views here.
def log(request):
  ...

def reg(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomCreationForm(request.POST)
    context = {
      'form':form
    }

    return render(request, 'account/reg.html', context)

def landing_page(request):
    return render(request, "main/landing.html")

def home(request):
  return render(request, "main/home.html")