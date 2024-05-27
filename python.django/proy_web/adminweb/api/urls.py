from rest_framework.routers import DefaultRouter
from adminweb.api.views import ProductoViewSet, ClienteViewSet, FacturaViewSet, DetalleProductoViewSet, EmpleadoViewSet

router = DefaultRouter()

router.register('productos', ProductoViewSet, basename='producto')
router.register('clientes', ClienteViewSet, basename='cliente')
router.register('facturas', FacturaViewSet, basename='factura')
router.register('detalles', DetalleProductoViewSet, basename='detalle')
router.register('empleados', EmpleadoViewSet, basename='empleados')

urlpatterns = router.urls

