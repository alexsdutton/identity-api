from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from oxidentity.attestation.serializers import Attestable, AttestationSerializer
from . import models


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Country
        exclude = ('people',)


class NationalitySerializer(Attestable, serializers.HyperlinkedModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = models.Nationality
        exclude = ('person',)

    def to_internal_value(self, data):
        try:
            country = data['country']
        except KeyError:
            raise ValidationError("country must be provided")
        try:
            if isinstance(country, int):
                country = models.Country.objects.get(id=country)
            elif isinstance(country, str) and len(country) == 2:
                country = models.Country.objects.get(alpha_2=country)
            elif isinstance(country, str) and country.isdigit() and len(country) == 3:
                country = models.Country.objects.get(numeric=country)
            elif isinstance(country, str) and len(country) == 3:
                country = models.Country.objects.get(alpha_3=country)
            else:
                raise ValidationError("country must be provided")
        except models.Country.DoesNotExist as e:
            raise ValidationError("No such country") from e
        return {'country': country}