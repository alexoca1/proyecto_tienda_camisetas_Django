from django.shortcuts import render, redirect
from .models import Producto
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


#def productos(request):
    #return render(request, 'core/productos.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)



def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})
    #return redirect('my_usuario')

@login_required
def my_usuario(request):
    # Puedes personalizar lo que se muestra en la página "my_usuario" aquí
    #return render(request, 'my_usuario.html')
    productos = Producto.objects.all()
    productos_aleatorios = random.sample(list(productos), 2)
    return render(request, 'my_usuario.html', {'productos_aleatorios': productos_aleatorios})
    
