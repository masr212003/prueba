from django.urls import path
from Webprincipal import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('usuario/', views.Usuario, name='usuario'),
    path('busqueda/', views.Buscar, name='Busqueda'),
    path('agregar/<int:producto_id>/', views.Agregar, name='agregar'),
    path('eliminar/<int:item_id>/', views.eliminarProducto, name='eliminar'),
    path('carrito/', views.ver_carrito, name='Ver'),
    path('pagosPedi/', views.PagosPedi, name='PagosPedi'),
    path('pagos/', views.Pagos, name='Pagos'),
    path('actu/<int:item_id>/', views.ActualizarCantidad, name='Actu'),
    path('compras/', views.Compras, name='Compras'),
]