from django.test.utils import setup_test_environment
from django.test import Client, TestCase
from django.urls import reverse

import json


client = Client()

class QuestionIndexViewTests(TestCase):
    header = {
        "HTTP_Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imt3YWsiLCJleHAiOjE2MTk2OTI5MDYsImVtYWlsIjoia3dha0Brd2FrLmNvbSIsIm9yaWdfaWF0IjoxNjE5MDg4MTA2fQ.KXNoYMuzZ68t7LYr16_9219gbaSoTBtkQh9zFgrhIPc"
    }
    # print(header)
    # response = client.get(path=reverse("club:project", kwargs={'club_id': 1}), **header)

    # print(dir(response))
    # print(response.json())

    def test_project_get(self):
        response = client.get(path=reverse('club:project', kwargs={'club_id': 2}), headers=self.header)
        print(response)
        self.assertEqual(response.status_code, 200)
        # print(response.status_code==200)
