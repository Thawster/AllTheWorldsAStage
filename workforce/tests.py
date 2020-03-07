from django.contrib.auth.models import User
from django.test import TestCase

from workforce.models import Clown

class ClownTestCase(TestCase):
    def setUp(self):
        Clown.objects.create(name="Jingle", age=30, description="Bouncer")

    def test_clown(self):
        jingles = Clown.objects.get(name="Jingle")

class ClownListViewTests(TestCase):
    def test_multiple_clowns(self):

        Clown.objects.create(name="Fuller", age=100, description="Ringleader")
        Clown.objects.create(name="Icky", age=40, description="Clown")

        response = self.client.get('/workforce')

        self.assertEqual(response.status_code, 301)

        responses = response.context['clowns']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Clown: My Test Clown>', '<Clown: Another Test Clown>'],
            ordered=False
        )