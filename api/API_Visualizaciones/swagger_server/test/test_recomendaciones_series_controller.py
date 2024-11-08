# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.recomendaciones_series import RecomendacionesSeries  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRecomendacionesSeriesController(BaseTestCase):
    """RecomendacionesSeriesController integration test stubs"""

    def test_recomendaciones_series_id_get(self):
        """Test case for recomendaciones_series_id_get

        Obtener las recomendaciones para un usario de series
        """
        response = self.client.open(
            '/recomendacionesSeries/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
