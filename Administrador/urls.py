from django.urls import path,include
from Administrador import views
urlpatterns = [
    path('adminUsu/', views.AdminUsu, name='adminUsu'),
    path('cambio/', views.Cambio, name="cambio"),
    path('buscarUsu/', views.ResultadoUsu, name="resultado"),  
    path('adminProductos/', views.AdminProducto, name="adminProduct"),
    path('cambioPro/', views.CambioProd, name="cambioPro"),
    path('buscarProduct/', views.ResultadoProduct, name="resultadoProdct"),
    path('adminCategorias/', views.AdminCate, name="adminCate"),
    path('buscarCate/', views.ResultadoCate, name="resultadoCate"),
    path('cambioCate/', views.CambioCate, name="cambioCate"),
    path('adminMarcas/', views.AdminMarca, name="adminMarca"),
    path('buscarMarca/', views.ResultadoMarca, name="resultadoMarca"),
    path('cambioMar/', views.CambioMar, name="cambioMar"),
    path('adminOrdenes/', views.AdminOrden, name="adminOrden"),
    path('buscarOrden/', views.ResultadoOrden, name="resultadoOrden"),
    path('cambioOrpen/', views.CambioOrpen, name="cambioOrpen"),
    path('cambioOrcan/', views.CambioOrcan, name="cambioOrcan"),
    path('cambioOrcom/', views.CambioOrcom, name="cambioOrcom"),
    path('aggCate/', views.AggCate, name="aggCate"),
    path('aggMar/', views.AggMar, name="aggMar"),
     path('aggProducto/', views.agregar_producto, name="aggProductos"),
]
