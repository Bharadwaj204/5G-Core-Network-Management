#!/usr/bin/env python3

"""
NETCONF Server Tests
"""

import unittest
import sys
import os

# Add the netconf-server directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'management-plane', 'netconf-server'))

class TestNETCONFServer(unittest.TestCase):
    
    def test_netconf_server_import(self):
        """Test that the NETCONF server module can be imported"""
        try:
            import netconf_server
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import netconf_server module")
    
    def test_sample_data_initialization(self):
        """Test that sample data is properly initialized"""
        import netconf_server
        self.assertTrue(len(netconf_server.network_data["network-functions"]["amf"]) > 0)
        self.assertTrue(len(netconf_server.network_data["network-functions"]["smf"]) > 0)
        self.assertTrue(len(netconf_server.network_data["network-functions"]["upf"]) > 0)
        self.assertTrue(len(netconf_server.network_data["subscribers"]["subscriber"]) > 0)

if __name__ == '__main__':
    unittest.main()