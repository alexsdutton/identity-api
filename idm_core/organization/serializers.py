from rest_framework.serializers import HyperlinkedModelSerializer

from idm_core.identity.serializers import TypeMixin

from . import models


class OrganizationSerializer(TypeMixin, HyperlinkedModelSerializer):
    class Meta:
        model = models.Organization
        fields = ('id', 'label', 'tags')


class TerseOrganizationSerializer(OrganizationSerializer):
    pass
