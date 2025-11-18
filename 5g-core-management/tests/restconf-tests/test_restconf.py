#!/usr/bin/env python3

"""
RESTCONF API Tests
"""

import unittest
import sys
import os

# Add the restconf-api directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'management-plane', 'restconf-api'))

class TestRESTCONFServer(unittest.TestCase):
    
    def test_restconf_server_import(self):
        """Test that the RESTCONF server module can be imported"""
        try:
            import restconf_server
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import restconf_server module")
    
    def test_sample_data_initialization(self):
        """Test that sample data is properly initialized"""
        import restconf_server
        self.assertTrue(len(restconf_server.network_data["network-functions"]["amf"]) > 0)
        self.assertTrue(len(restconf_server.network_data["network-functions"]["smf"]) > 0)
        self.assertTrue(len(restconf_server.network_data["network-functions"]["upf"]) > 0)
        self.assertTrue(len(restconf_server.network_data["subscribers"]["subscriber"]) > 0)

if __name__ == '__main__':
    unittest.main()