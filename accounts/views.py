from django.shortcuts import render, redirect
from .forms import CustomCreationForm, CodeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import CustomUser, Code
# Create your views here.
def log(request):
  form = AuthenticationForm()
  if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username = username, password = password)

      if user is not None:
          request.session['id'] = user.id
          #send mail
          return redirect(verify_view)
  return render(request, 'account/login.html', {'form':form})


def verify_view(request):
    form = CodeForm(request.POST)
    pk = request.session.get('id')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        if not request.POST:
            print(code)
            ...
        if form.is_valid():
            num = form.cleaned_data['number']
            if num == str(code):
                code.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            else:
                return redirect('login')
        
    return render(request, 'account/verify.html', {'form': form})

def reg(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('login')
    else:
        form = CustomCreationForm(request.POST)
    context = {
      'form':form
    }

    return render(request, 'account/reg.html', context)

def landing_page(request):
    return render(request, "main/landing.html")

@login_required
def home(request):
  
  return render(request, "main/home.html")