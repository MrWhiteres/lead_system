from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LeadSystemTestCase(APITestCase):
    url = reverse('lead')
    base_body = {
        'leads':
            [
                {
                    'name': 'Test',
                    'email': 'test@test.com',
                    'phone': 380558877052,
                    'ip_address': '127.0.0.1'
                }
            ]
    }
    duplicate_body = {
        'leads': [
            base_body['leads'][0],
            base_body['leads'][0],
            base_body['leads'][0],
            base_body['leads'][0],
            base_body['leads'][0],
        ]
    }
    invalid_data = {
        'leads': [
            {
                'name': '65654',
                'phone': 26565466546,
                'ip_address': '89.0.142.86'
            }
        ]
    }
    valid_invalid_data = {
        'leads': [
            base_body['leads'][0],
            invalid_data['leads'][0],
        ]
    }

    def test_get_method(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_empty_post_data(self):
        response = self.client.post(self.url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_data = response.json()
        self.assertEqual(response_data['leads'], ['Empty leads'])

    def test_create_lead(self):
        response = self.client.post(self.url, self.base_body, format='json')
        self.assertEqual(response.json()['new_leads'], 1)

    def test_invalid_email_data(self):
        response = self.client.post(self.url, self.invalid_data, format='json')
        self.assertEqual(response.json()['leads'], [{'email': ['This field is required']}])

    def test_create_duplicate_data_lead(self):
        response = self.client.post(self.url, self.duplicate_body, format='json')
        self.assertEqual(response.json()['new_leads'], 1)

    def test_create_lead_with_invalid_and_valid_data(self):
        response = self.client.post(self.url, self.valid_invalid_data, format='json')
        self.assertEqual(response.json()['new_leads'], 1)
