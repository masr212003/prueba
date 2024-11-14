from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from iniusuario.models import DatosUsuario
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        user = form.get_user()
        try:
            prueba = DatosUsuario.objects.get(nombre_usu=user)
            if prueba.estado == 'inactivo':
                form.add_error(None, 'Tu cuenta está inactiva.')
                return self.form_invalid(form)
        except DatosUsuario.DoesNotExist:
            form.add_error(None, 'No se pudo verificar el estado de tu cuenta.')
            return self.form_invalid(form)
        
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('Home')

def exit(request):
    logout(request)
    return redirect('Home')

def Registro(request):
    if request.method == 'POST':
        usu = request.POST['username']
        cl = request.POST['password']
        cl_vali = request.POST['password_r']
        cedu = request.POST['cedula']
        nomb = request.POST['name']
        ape = request.POST['last_name']
        tlf = request.POST['telefono']
        
        if cl == cl_vali:
            cedula_exi = DatosUsuario.objects.filter(cedula=cedu).exists()
            if cedula_exi:
                return render(request, 'inte/registroA.html', {'error': 'Cedula ya registrada'})
            else:
                usu_exi = User.objects.filter(username=usu).exists()
                if usu_exi:
                    return render(request, 'inte/registroA.html', {'error': 'Usuario ya existente'})
                else:
                    validacion = Validar_datos(nomb, ape, cedu, tlf, usu, cl)
                    if validacion == True:
                        usuario = User.objects.create_user(username=usu, password=cl, email='nada@gmail.com')
                        usuario.save()
                        DatosUsuario.objects.create(nombre_usu=usuario, nombre=nomb, apellido=ape, cedula=cedu, telefono=tlf, tp_usu="Usuario")
                        return redirect('Login')
                    else:
                        return render(request, 'inte/registroA.html', {'error': validacion})
        else:
            return render(request, 'inte/registroA.html', {'error': 'Claves diferentes'})
    
    return render(request, 'inte/registroA.html')
   
def Validar_datos(nombre,apellido,cedula,tlf,nombre_usu,clave):
    
    nombre_vali=len(nombre)
    apellido_vali=len(apellido)
    cedula_vali=len(cedula)
    tlf_vali=len(tlf)
    nombre_usu_vali=len(nombre_usu)
    clave_vali=len(clave)
    
    if nombre_usu_vali>=6 and nombre_usu_vali<=20:
        if clave_vali>=8 and clave_vali<=16:
            if nombre_vali>=4 and nombre_vali<=10:
                if apellido_vali>=4 and apellido_vali<=10:
                    if cedula_vali>=7 and cedula_vali<=8 and cedula.isdigit()==True:
                        if tlf[0]=="0" and tlf[1]=="4" and tlf_vali==11:
                            return True
                        else:
                            return "Telefono invalido"    
                    else:
                        return "Cedula invalida"    
                else:
                    return "Apellido invalido"    
            else:
                return "Nombre invalda"    
        else:
            return "Contraseña invalida"    
    else:
        return "Usuario invalido"    
         
         

