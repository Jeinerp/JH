from django.urls import path, include
from rest_framework import routers
from .views import ClientesViewSet

router= routers.DefaultRouter()
router.register(r'',ClientesViewSet)

urlpatterns =[

    path('', include(router.urls)),
]