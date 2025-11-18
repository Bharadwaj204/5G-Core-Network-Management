#!/usr/bin/env python3

"""
SNMP Agent Tests
"""

import unittest
import sys
import os

# Add the snmp-monitor directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'management-plane', 'snmp-monitor'))

class TestSNMPAgent(unittest.TestCase):
    
    def test_snmp_agent_import(self):
        """Test that the SNMP agent module can be imported"""
        try:
            import snmp_agent
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import snmp_agent module")
    
    def test_snmp_poller_import(self):
        """Test that the SNMP poller module can be imported"""
        try:
            import snmp_poller
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import snmp_poller module")

if __name__ == '__main__':
    unittest.main()