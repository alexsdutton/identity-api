import datetime

from django.test import TransactionTestCase

from idm_core.identity.exceptions import MergeTypeDisparity
from idm_core.organization.models import Organization
from idm_core.person.models import Person
from idm_core.person.serializers import PersonSerializer


class MergingTestCase(TransactionTestCase):
    fixtures = ['initial']

    def create_person_from_json(self, data):
        serializer = PersonSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def testSimpleMerge(self):
        primary = Person.objects.create()
        secondary = Person.objects.create()

        primary.merge(secondary)

        self.assertEqual(secondary.merged_into, primary)
        self.assertEqual(secondary.state, 'merged')

    def testCantMergeDifferentTypes(self):
        primary = Person.objects.create()
        secondary = Organization.objects.create()

        with self.assertRaises(MergeTypeDisparity):
            primary.merge(secondary)


    def testEverythingMoved(self):
        primary = self.create_person_from_json({
            'names': [{
                "context": "legal",
                "components": [{"type": "given", "value": "Alice"}],
            }],
            'identifiers': [{
                "type": "username",
                "value": "abcd0001",
            }],
        })
        secondary = self.create_person_from_json({
            'names': [{
                "context": "presentational",
                "components": [{"type": "given", "value": "Bob"}],
            }],
            'identifiers': [{
                "type": "username",
                "value": "abcd0002",
            }],
            'sex': '2',
            'date_of_birth': '1970-01-02',
            'date_of_death': '1970-01-03',
        })

        primary.merge(secondary)

        self.assertEqual(primary.names.count(), 2)
        self.assertEqual(secondary.names.count(), 1)

        self.assertEqual(primary.identifiers.count(), 2)
        self.assertEqual(secondary.identifiers.count(), 0)

        self.assertEqual(primary.sex, '2')
        self.assertEqual(primary.date_of_birth, datetime.date(1970, 1, 2))
        self.assertEqual(primary.date_of_death, datetime.date(1970, 1, 3))

    def testDontDuplicateNationalities(self):
        primary = self.create_person_from_json({
            'names': [{
                "context": "legal",
                "components": [{"type": "given", "value": "Alice"}],
            }],
            'nationalities': [{
                "country": "GBR",
            }],
        })
        secondary = self.create_person_from_json({
            'names': [{
                "context": "presentational",
                "components": [{"type": "given", "value": "Bob"}],
            }],
            'nationalities': [{
                "country": "GBR",
            }],
        })

        primary.merge(secondary)

        self.assertEqual(primary.nationalities.count(), 1)
        self.assertEqual(secondary.nationalities.count(), 0)

    def testReverseMerge(self):
        primary = Person.objects.create()
        secondary = Person.objects.create()

        secondary.merge_into(primary)

        self.assertEqual(secondary.merged_into, primary)
        self.assertEqual(secondary.state, 'merged')
