from rest_framework import viewsets

from api import models
from api import serializers


class ChateauViewSet(viewsets.ModelViewSet):
    queryset = models.Chateau.objects.all()
    serializer_class = serializers.ChateauSerializer


class MillesimeViewSet(viewsets.ModelViewSet):
    queryset = models.Millesime.objects.all()
    serializer_class = serializers.MillesimeSerializer


class AppellationViewSet(viewsets.ModelViewSet):
    queryset = models.Appellation.objects.all()
    serializer_class = serializers.AppellationSerializer


class ClassementViewSet(viewsets.ModelViewSet):
    queryset = models.Classement.objects.all()
    serializer_class = serializers.ClassementSerializer


class CouleurViewSet(viewsets.ModelViewSet):
    queryset = models.Couleur.objects.all()
    serializer_class = serializers.CouleurSerializer


class ISWNViewSet(viewsets.ModelViewSet):
    queryset = models.ISWN.objects.all()
    serializer_class = serializers.ISWNSerializer
