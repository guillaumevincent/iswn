import rest_framework_jwt.views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register(r'chateau', views.ChateauViewSet, base_name='chateau')
router.register(r'millesime', views.MillesimeViewSet, base_name='millesime')
router.register(r'appellation', views.AppellationViewSet, base_name='appellation')
router.register(r'classement', views.ClassementViewSet, base_name='classement')
router.register(r'couleur', views.CouleurViewSet, base_name='couleur')
router.register(r'iswn', views.ISWNViewSet, base_name='iswn')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^tokens/auth/', rest_framework_jwt.views.obtain_jwt_token),
    url(r'^tokens/verify/', rest_framework_jwt.views.verify_jwt_token),
    url(r'^tokens/refresh/', rest_framework_jwt.views.refresh_jwt_token),
    url(r'^auth/', include('djoser.urls')),
]
