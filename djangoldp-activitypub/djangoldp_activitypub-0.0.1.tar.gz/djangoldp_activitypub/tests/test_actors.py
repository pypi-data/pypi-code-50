# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json

from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from djangoldp_activitypub.tests.models import JobOffer


class ActorTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_get_service_actor(self):
        response = self.client.get('/job-offers/', HTTP_ACCEPT='application/activity+json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEquals(content['type'], "Service")
        self.assertEquals(content['inbox'], "http://happy-dev.fr/job-offers/inbox/")
        self.assertIn('publicKey', content)

    def test_get_service_not_found(self):
        response = self.client.get('/unknown/', HTTP_ACCEPT='application/activity+json')
        self.assertEqual(response.status_code, 404)

    def test_get_group_actor(self):
        job = JobOffer.objects.create(slug='abc')
        response = self.client.get('/job-offers/{}/'.format(job.slug), HTTP_ACCEPT='application/activity+json')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEquals(content['type'], "Group")
        self.assertEquals(content['inbox'], "http://happy-dev.fr/job-offers/{}/inbox/".format(job.slug))
        self.assertIn('publicKey', content)

    def test_get_group_actor_not_found(self):
        response = self.client.get('/job-offers/404/', HTTP_ACCEPT='application/activity+json')
        self.assertEqual(response.status_code, 404)
