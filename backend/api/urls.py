import rest_framework_jwt.views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^tokens/auth/', rest_framework_jwt.views.obtain_jwt_token),
    url(r'^tokens/verify/', rest_framework_jwt.views.verify_jwt_token),
    url(r'^tokens/refresh/', rest_framework_jwt.views.refresh_jwt_token),
    url(r'^auth/', include('djoser.urls')),
]
