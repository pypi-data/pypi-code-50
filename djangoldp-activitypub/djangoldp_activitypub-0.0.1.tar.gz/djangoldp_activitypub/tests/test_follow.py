# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, APIClient

from djangoldp_activitypub.models import Activity, Follower
from djangoldp_activitypub.tests.models import JobOffer


class FollowTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_service(self):
        activity = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": "http://example.org/activities/123",
            "type" : "Follow",
            "actor" : "https://social.lemee.co/@jb",
            "object": "http://happy-dev.fr/job-offers/",
        }
        response = self.client.post('http://happy-dev.fr/job-offers/inbox/', data=json.dumps(activity),HTTP_ACCEPT='application/activity+json', content_type='application/activity+json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Follower.objects.all().count(), 1)


        response = self.client.get('/job-offers/inbox/', HTTP_ACCEPT='application/activity+json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"type": "OrderedCollection", "orderedItems": [{"type": "Follow", "id": "http://example.org/activities/123", "actor": "https://social.lemee.co/@jb", "object": "http://happy-dev.fr/job-offers/"}], "totalItems": 1, "@context": "https://www.w3.org/ns/activitystreams"}')

    def test_group(self):
        job = JobOffer.objects.create(title="job offer", slug="top-job")
        activity = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": "http://example.org/activities/123",
            "type" : "Follow",
            "actor" : "https://social.lemee.co/@jb",
            "object": "http://happy-dev.fr/job-offers/{}/".format(job.slug),
        }
        response = self.client.post('http://happy-dev.fr/job-offers/{}/inbox/'.format(job.slug), data=json.dumps(activity),HTTP_ACCEPT='application/activity+json', content_type='application/activity+json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, Follower.objects.all().count())

        response = self.client.get('/job-offers/{}/inbox/'.format(job.slug), HTTP_ACCEPT='application/activity+json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"type": "OrderedCollection", "orderedItems": [{"type": "Follow", "id": "http://example.org/activities/123", "actor": "https://social.lemee.co/@jb", "object": "http://happy-dev.fr/job-offers/top-job/"}], "totalItems": 1, "@context": "https://www.w3.org/ns/activitystreams"}')

        undo = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "type": "Undo",
            "id": "https://social.lemee.co/@jb#undo/stuff/4",
            "actor": "https://social.lemee.co/@jb",
            "object": {
                "id": "http://example.org/activities/123",
                "type" : "Follow",
                "actor" : "https://social.lemee.co/@jb",
                "object": "http://happy-dev.fr/job-offers/{}/".format(job.slug),
            },
        }

        response = self.client.post('http://happy-dev.fr/job-offers/{}/inbox/'.format(job.slug), data=json.dumps(undo),HTTP_ACCEPT='application/activity+json', content_type='application/activity+json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, Follower.objects.all().count())




