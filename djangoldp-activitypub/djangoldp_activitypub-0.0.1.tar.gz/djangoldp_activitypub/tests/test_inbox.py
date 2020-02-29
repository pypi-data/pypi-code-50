# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from djangoldp_activitypub.models import Activity
from djangoldp_activitypub.tests.models import JobOffer


class GetInboxTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_service(self):
        activity = {
            "type" : "Follow",
            "actor" : "https://social.lemee.co/@jb",
            "object": "http://happy-dev.fr/job-offers/",
        }
        Activity.objects.create(local_id="http://happy-dev.fr/job-offers/inbox/", payload=json.dumps(activity).encode('utf-8'))
        response = self.client.get('/job-offers/inbox/', HTTP_ACCEPT='application/activity+json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"type": "OrderedCollection", "orderedItems": [{"type": "Follow", "actor": "https://social.lemee.co/@jb", "object": "http://happy-dev.fr/job-offers/"}], "totalItems": 1, "@context": "https://www.w3.org/ns/activitystreams"}')

    def test_group(self):
        job = JobOffer.objects.create(title="job offer", slug="top-job")
        activity = {
            "type" : "Follow",
            "actor" : "https://social.lemee.co/@jb",
            "object": "http://happy-dev.fr/job-offers/{}/".format(job.slug),
        }
        Activity.objects.create(local_id="http://happy-dev.fr/job-offers/{}/inbox/".format(job.slug), payload=json.dumps(activity).encode('utf-8'))
        response = self.client.get('/job-offers/{}/inbox/'.format(job.slug), HTTP_ACCEPT='application/activity+json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"type": "OrderedCollection", "orderedItems": [{"type": "Follow", "actor": "https://social.lemee.co/@jb", "object": "http://happy-dev.fr/job-offers/top-job/"}], "totalItems": 1, "@context": "https://www.w3.org/ns/activitystreams"}')


