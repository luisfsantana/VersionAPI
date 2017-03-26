# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.properties import Properties
from swagger_server.models.property import Property
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_properties_get(self):
        """
        Test case for properties_get

        Gets some properties
        """
        query_string = [('ax', 56),
                        ('ay', 56),
                        ('bx', 56),
                        ('by', 56)]
        response = self.client.open('/v1/properties',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_properties_id_delete(self):
        """
        Test case for properties_id_delete

        Deletes a property
        """
        response = self.client.open('/v1/properties/{id}'.format(id='id_example'),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_properties_id_get(self):
        """
        Test case for properties_id_get

        Gets a property
        """
        response = self.client.open('/v1/properties/{id}'.format(id='id_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_properties_post(self):
        """
        Test case for properties_post

        Creates a property
        """
        property = Property()
        response = self.client.open('/v1/properties',
                                    method='POST',
                                    data=json.dumps(property),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
