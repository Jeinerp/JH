from django.urls import path, include
from rest_framework import routers
from .views import ProductosViewSet
from .views import TipoProductoViewSet

router= routers.DefaultRouter()
router.register(r'productos',ProductosViewSet)
router.register(r'tipo',TipoProductoViewSet)


urlpatterns =[

    path('', include(router.urls)),
]