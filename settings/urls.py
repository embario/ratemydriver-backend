from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from ratemydriver.urls import router as auth_router

router = routers.DefaultRouter()
router.registry.extend(auth_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('ratemydriver.urls')),
    path('api/v1/', include(router.urls)),
]
