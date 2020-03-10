# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from gpa_api.models.calculation import Calculation  # noqa: E501
from gpa_api.models.calculation_body import CalculationBody  # noqa: E501
from gpa_api.models.ship import Ship  # noqa: E501
from gpa_api.test import BaseTestCase


class TestLngController(BaseTestCase):
    """LngController integration test stubs"""

    def test_calculate(self):
        """Test case for calculate

        Calculate LNG Ageing
        """
        calculation_body = {
  "standard" : {
    "createdDate" : "2000-01-23T04:56:07.000+00:00",
    "idealGasReferenceState" : 7.061401241503109,
    "measurementTemperature" : 2.3021358869347655,
    "id" : "id",
    "standardVersion" : "standardVersion",
    "combustionTemperature" : 5.637376656633329
  },
  "ship" : {
    "country" : "country",
    "name" : "name"
  },
  "fluid" : {
    "nButane" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    },
    "ethane" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    },
    "createdDate" : "2000-01-23T04:56:07.000+00:00",
    "iButane" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    },
    "nitrogen" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    },
    "propane" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    },
    "methane" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    },
    "nHexane" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    },
    "id" : "id",
    "nPentane" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    },
    "iPentane" : {
      "unit" : "unit",
      "value" : 0.8008281904610115
    }
  },
  "transport" : {
    "volume" : 6.027456183070403,
    "fromDate" : "2000-01-23T04:56:07.000+00:00",
    "createdDate" : "2000-01-23T04:56:07.000+00:00",
    "toDate" : "2000-01-23T04:56:07.000+00:00",
    "id" : "id",
    "pressure" : 1.4658129805029452,
    "boilOffRate" : 5.962133916683182
  }
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/lng/calculations',
            method='POST',
            headers=headers,
            data=json.dumps(calculation_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_calculation(self):
        """Test case for get_calculation

        Get LNG Ageing calculation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/lng/calculations/{calculation_id}'.format(calculation_id='calculation_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_calculations(self):
        """Test case for get_calculations

        Get a list of LNG Ageing calculations
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/lng/calculations',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ships(self):
        """Test case for get_ships

        Get a list of ships.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/lng/ships',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
