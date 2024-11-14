from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from iniusuario.models import DatosUsuario
from Webprincipal.models import Productos,Categoria,CarritoProducto,Ordene,OrdeneProducto
from django.contrib.auth.models import User
from django.db.models import Q

def Home(request):
    categorias = Categoria.objects.all()[:2]
    productos_por_categoria = {}
    for categoria in categorias:
        productos = Productos.objects.filter(categoria=categoria)
        productos_por_categoria[categoria] = productos

    if request.user.is_authenticated:
        user = request.user
        datos_usuario = DatosUsuario.objects.get(nombre_usu=user)
    else:
        datos_usuario = None  

    return render(request, 'inte/home.html', {'productos_por_categoria': productos_por_categoria, 'DatosUsuario': datos_usuario})

def Buscar(request):
    producto=request.GET["buscar"]
    if request.user.is_authenticated:
        user = request.user
        datos_usuario = DatosUsuario.objects.get(nombre_usu=user)
    else:
        datos_usuario = None  
        
    if producto: 
        productos = Productos.objects.filter(Q(nombre__icontains=producto)) 
        return render(request, 'inte/busqueda.html', {'productos': productos, 'DatosUsuario': datos_usuario}) 
    else: 
        mensaje = "no colocaste nada" 
        return render(request, 'inte/busqueda.html', {'mensaje': mensaje, 'DatosUsuario': datos_usuario})

@login_required
def Usuario(request):
    user = get_object_or_404(User, username=request.user.username)
    datos_usuario = DatosUsuario.objects.filter(nombre_usu=user).first()
    return render(request, 'inte/usuario.html', {'user': user, 'datos': datos_usuario})

@login_required
def Agregar(request, producto_id):
    producto_agg = get_object_or_404(Productos, id=producto_id)
    usuario=request.user.username
    cantidad_agg=1
    precio_agg=producto_agg.precio
    preciof=cantidad_agg*precio_agg
    CarritoProducto.objects.create(producto=producto_agg, cantidad=cantidad_agg, precio=precio_agg, user=usuario, precioFin=preciof)
    
    return redirect('Home')

@login_required
def ver_carrito(request):
    carrito_productos = CarritoProducto.objects.filter(user=request.user.username)
    if request.user.is_authenticated:
        user = request.user
        datos_usuario = DatosUsuario.objects.get(nombre_usu=user)
    else:
        datos_usuario = None  
    total=0
    
    for canti in carrito_productos:
        total+=canti.precio * canti.cantidad
    
    final=total+2
  
    return render(request, 'inte/carrito.html', {'carrito_productos': carrito_productos, 'total':total,'fin':final,'DatosUsuario': datos_usuario})

@login_required
def eliminarProducto(request,item_id):
    productoCarrito=get_object_or_404(CarritoProducto, id=item_id)
    productoCarrito.delete()
    return redirect('Ver')

@login_required
def PagosPedi(request):
    receptorP = request.POST['username']
    refe = request.POST['refe']
    ubi = request.POST['ubi']
    usu = request.user.username
    carrito = CarritoProducto.objects.filter(user=request.user.username) 
    total2 = 2


    for j in carrito:
        total2 += j.precioFin

    for i in carrito:
        id_car = i.producto.id
        prod = Productos.objects.get(id=id_car)
        cantidad = i.cantidad
        cantidadProducto = prod.cantidad

        canFinal = cantidadProducto - cantidad
        Productos.objects.filter(id=id_car).update(cantidad=canFinal)

    orden = Ordene.objects.create(receptor=receptorP, referencia=refe, ubicacion=ubi, total=total2, usuario=usu, estado=Ordene.EstadoChoices.PENDIENTE) 

    for carrito_producto in carrito: 
        OrdeneProducto.objects.create(orden=orden, producto=carrito_producto.producto, cantidad=carrito_producto.cantidad)

    carrito.delete()
    return render(request, 'inte/carrito.html')


@login_required
def Pagos(request):
     return render(request, 'inte/pago.html')

@login_required
def ActualizarCantidad(request,item_id):
    newCantidad=int(request.POST['ct'])
    carrito=request.POST['carrito_id']
    prod=Productos.objects.get(id=item_id)
    precio=prod.precio
    can=prod.cantidad

    if can<newCantidad:
        return redirect('Ver')
    else:
        final=precio*newCantidad
        CarritoProducto.objects.filter(id=carrito).update(cantidad=newCantidad, precioFin=final)
        return redirect('Ver')

@login_required

def Compras(request):
    compras = Ordene.objects.filter(usuario=request.user.username).order_by('-fecha')
    productos_por_orden = []
        

    if request.user.is_authenticated:
        user = request.user
        datos_usuario = DatosUsuario.objects.get(nombre_usu=user)
    else:
        datos_usuario = None  
        
    for compra in compras:
        productos = OrdeneProducto.objects.filter(orden=compra)
        productos_por_orden.append({'orden': compra, 'productos': productos})
    
    return render(request, 'inte/compras.html', {'productos_por_orden': productos_por_orden,'DatosUsuario': datos_usuario})
