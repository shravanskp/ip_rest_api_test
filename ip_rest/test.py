import json
from unittest.mock import patch, Mock
from django.test import Client, TestCase


class TestIpRoutes(TestCase):
    def setUp(self):
        self.data = {"cidr": "10.0.1.17/32"}
        self.base_url = '/api/ips/'
        res = self.client.post('/api/ips/', self.data)
        self.ip_url = self.base_url + str(res.data['id']) + '/'
        self.acquire_url = self.ip_url + 'acquire/'
        self.release_url = self.ip_url + 'release/'

    def test_should_return_all_available_ips_from_db(self):
        """ Can we get all available IP's  """
        res = self.client.get(self.base_url, None)
        self.assertEqual(res.status_code, 200)

    def test_should_retrieve_ip_by_id(self):
        """ Can we retrieve a particular IP  """
        res = self.client.get(self.ip_url)
        self.assertEqual(res.status_code, 200)

    def test_should_create_ip_in_db(self):
        """ Can we store an IP in database  """
        res = self.client.post(self.base_url, {"cidr": "10.0.1.17/16"})
        self.assertEqual(res.status_code, 201)

    def test_should_update_status_acquired(self):
        """ Can we update the status of an IP  """
        res = self.client.put(self.acquire_url, None)
        self.assertEqual(res.status_code, 200)

    def test_should_update_status_available(self):
        """ Can we update the status of an IP  """
        res = self.client.put(self.release_url, None)
        self.assertEqual(res.status_code, 200)
