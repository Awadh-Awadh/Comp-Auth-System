from django.shortcuts import render
from .forms import CustomCreationForm

# Create your views here.
def log(request):
  ...

def reg(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
    else:
        form = CustomCreationForm(request.POST)
    context = {
      'form':form
    }

    return render(request, 'accounts/reg.html', context)

