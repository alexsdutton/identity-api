from rest_framework import serializers

from oxidentity.attestation.serializers import Attestable
from . import models


class IdentifierTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IdentifierType


class IdentifierSerializer(Attestable, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Identifier
