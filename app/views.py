from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Usuario

def home(request):
    return render(request, 'authentication/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Redirigir a la página deseada después del inicio de sesión
            return redirect('home')
        else:
            # Mostrar mensaje de error si la autenticación falla
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')

    return render(request, 'authentication/login.html')


def signup(request):
    if request.method == 'POST':
        # Procesar la lógica de registro cuando se envía el formulario POST
        name = request.POST['name']
        last_name = request.POST['last_name']
        rut = request.POST['rut']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validaciones y lógica de registro
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este correo electrónico ya está registrado.')
        elif password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
        else:
            # Hashear la contraseña antes de almacenarla
            hashed_password = make_password(password)

            # Crear una instancia del modelo Usuario
            nuevo_usuario = Usuario(
                name=name,
                last_name=last_name,
                rut=rut,
                email=email,
                password=hashed_password
            )

            # Guardar el nuevo usuario en la base de datos
            nuevo_usuario.save()
            messages.success(request, 'Registro exitoso. ¡Ahora estás autenticado!')
            return redirect('login')  # Ajusta el nombre de la vista de inicio de sesión

    return render(request, 'authentication/signup.html')

def view(request):
    return render(request, 'products/view.html')

