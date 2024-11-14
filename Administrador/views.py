from django.shortcuts import render,redirect
from iniusuario.models import DatosUsuario 
from django.contrib.auth.models import User
from Webprincipal.models import Productos,Categoria,Marca,Ordene,OrdeneProducto
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

def AdminUsu(request):
    nombre=request.user.username
    usuarios=DatosUsuario.objects.all()
    return render(request,'inte/adminUsu.html',{'usu':usuarios,'name':nombre})

def ResultadoUsu(request):
    elemento = request.POST.get('bus', '')

    if elemento == "*":
        resul = DatosUsuario.objects.all()
    elif elemento.isalpha():
        resul = DatosUsuario.objects.filter(nombre__icontains=elemento)
    elif elemento.isdigit():
        resul = DatosUsuario.objects.filter(cedula=elemento)
    else:
        resul = []

    return render(request, 'inte/adminUsu.html', {'usu': resul})


def Cambio(request):
    usuariop=request.POST['username']
    usuario=DatosUsuario.objects.get(id=usuariop)
    if usuario.estado=="activo":
        usuario.estado = DatosUsuario.EstadoChoices.INACTIVO 
        usuario.save()
        return redirect('adminUsu')
    else:
        usuario.estado = DatosUsuario.EstadoChoices.ACTIVO 
        usuario.save()
        return redirect('adminUsu')
    
def AdminProducto(request):
    nombre=request.user.username
    usuarios=Productos.objects.all()
    return render(request,'inte/adminProductos.html',{'usu':usuarios,'name':nombre})

def ResultadoProduct(request):
    elemento = request.POST['bus']
    if elemento=="*":
        productos = Productos.objects.all() 
    else:
        productos = Productos.objects.filter(Q(nombre__icontains=elemento)) 

    return render(request, 'inte/adminProductos.html', {'usu': productos})


def CambioProd(request):
    usuariop=request.POST['username']
    usuario=Productos.objects.get(id=usuariop)
    if usuario.estado=="activo":
        usuario.estado = Productos.EstadoChoices.INACTIVO 
        usuario.save()
        return redirect('adminProduct')
    else:
        usuario.estado = Productos.EstadoChoices.ACTIVO 
        usuario.save()
        return redirect('adminProduct')

def AdminCate(request):
    nombre=request.user.username
    cate=Categoria.objects.all()
    return render(request,'inte/adminCategorias.html',{'usu':cate,'name':nombre})

def ResultadoCate(request):
    elemento = request.POST['bus']
    if elemento=="*":
        productos = Categoria.objects.all() 
    else:
        productos = Categoria.objects.filter(Q(nombre__icontains=elemento)) 

    return render(request, 'inte/adminCategorias.html', {'usu': productos})

def CambioCate(request):
    usuariop=request.POST['username']
    usuario=Categoria.objects.get(id=usuariop)
    if usuario.estado=="activo":
        usuario.estado = Categoria.EstadoChoices.INACTIVO 
        usuario.save()
        return redirect('adminCate')
    else:
        usuario.estado = Categoria.EstadoChoices.ACTIVO 
        usuario.save()
        return redirect('adminCate')

def AdminMarca(request):
    nombre=request.user.username
    cate=Marca.objects.all()
    return render(request,'inte/adminMarca.html',{'usu':cate,'name':nombre})

def ResultadoMarca(request):
    elemento = request.POST['bus']
    if elemento=="*":
        productos = Marca.objects.all() 
    else:
        productos = Marca.objects.filter(Q(nombreMar__icontains=elemento)) 

    return render(request, 'inte/adminMarca.html', {'usu': productos})

def CambioMar(request):
    usuariop=request.POST['username']
    usuario=Marca.objects.get(id=usuariop)
    if usuario.estado=="activo":
        usuario.estado = Marca.EstadoChoices.INACTIVO 
        usuario.save()
        return redirect('adminMarca')
    else:
        usuario.estado = Marca.EstadoChoices.ACTIVO 
        usuario.save()
        return redirect('adminMarca')
    
def AdminOrden(request):
    compras = Ordene.objects.filter(usuario=request.user.username).order_by('-fecha')
    productos_por_orden = []
    
    for compra in compras:
        productos = OrdeneProducto.objects.filter(orden=compra)
        productos_por_orden.append({'orden': compra, 'productos': productos})
    
    nombre=request.user.username
    cate=Ordene.objects.all()

    return render(request,'inte/adminOrdenes.html',{'usu':cate,'name':nombre,'productos_por_orden': productos_por_orden})

def ResultadoOrden(request):
    elemento = request.POST['bus']
    if elemento=="*":
        productos = Ordene.objects.all() 
    else:
        productos = Ordene.objects.filter(Q(nombreMar__icontains=elemento)) 

    return render(request, 'inte/adminOrdenes.html', {'usu': productos})

def CambioOrpen(request):
    usuariop=request.POST['username']
    usuario=Ordene.objects.get(id=usuariop)
    if usuario.estado!="pendiente":
        usuario.estado = Ordene.EstadoChoices.PENDIENTE 
        usuario.save()
        return redirect('adminOrden')

def CambioOrcan(request):
    usuariop=request.POST['username']
    usuario=Ordene.objects.get(id=usuariop)
    if usuario.estado!="cancelada":
        usuario.estado = Ordene.EstadoChoices.CANCELADA 
        usuario.save()
        return redirect('adminOrden')

def CambioOrcom(request):
    usuariop=request.POST['username']
    usuario=Ordene.objects.get(id=usuariop)
    if usuario.estado!="completada":
        usuario.estado = Ordene.EstadoChoices.COMPLETADA 
        usuario.save()
        return redirect('adminOrden')

def AggCate(request):
    nuevo=request.POST['agg']
    Categoria.objects.create(nombre=nuevo)
    return redirect('adminCate')

def AggMar(request):
    nuevo=request.POST['agg']
    Marca.objects.create(nombreMar=nuevo)
    return redirect('adminMarca')

def agregar_producto(request):
    if request.method == 'POST' and request.FILES['imagen']:
        nombre = request.POST['nombre']
        peso = request.POST['peso']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        categoria_id = request.POST['categoria']
        marca_id = request.POST['marca']
        estado = request.POST['estado']
        imagen = request.FILES['imagen']

        categoria = Categoria.objects.get(id=categoria_id)
        marca = Marca.objects.get(id=marca_id)

        producto = Productos(
            nombre=nombre,
            peso=peso,
            precio=precio,
            cantidad=cantidad,
            categoria=categoria,
            marca=marca,
            estado=estado,
            imagen=imagen
        )
        producto.save()
        return redirect('adminProduct') 
    else:
        categorias = Categoria.objects.all()
        marcas = Marca.objects.all()
        estados = Productos.EstadoChoices.choices
    return render(request, 'inte/aggProducto.html', {
        'categorias': categorias,
        'marcas': marcas,
        'estados': estados
    })

