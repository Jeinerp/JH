from django.urls import path, include
from rest_framework import routers
from .views import VentasViewSet

router= routers.DefaultRouter()
router.register(r'',VentasViewSet)

urlpatterns =[

    path('', include(router.urls)),
]