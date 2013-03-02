#coding=utf8

import json
import unittest
from flask.ext.testing import TestCase
from app import app

sizheninfo_json = '''
[
    {
        "patientID" : "s000001",
        "patientName" : "1号病人",
        "connectedState" : false,
        "connectedAddinfoID" : null
    },
    {
        "patientID" : "s000002",
        "patientName" : "2号病人",
        "connectedState" : true,
        "connectedAddinfoID" : "a000002"
    }
]
'''


class TestApi(TestCase):
    def create_app(self):
        return app

    def test_sizheninfo(self):
        response = self.client.get("/api/sizheninfo")
        self.assertEquals(response.json, json.loads(sizheninfo_json))


if __name__ == '__main__':
    unittest.main()
