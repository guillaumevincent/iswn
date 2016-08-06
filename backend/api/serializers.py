from rest_framework import serializers

from api import models


class ChateauSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chateau


class MillesimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Millesime


class AppellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appellation


class ClassementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classement


class CouleurSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Couleur


class ISWNSerializer(serializers.ModelSerializer):
    chateau = ChateauSerializer(read_only=True)
    millesime = MillesimeSerializer(read_only=True)
    appellation = AppellationSerializer(read_only=True)
    classement = ClassementSerializer(read_only=True)
    couleur = CouleurSerializer(read_only=True)

    class Meta:
        model = models.ISWN
