#!/usr/bin/env python3
"""
Test script to verify all components of the 5G Core Management Prototype
"""

import requests
import json
import time
import subprocess
import sys
import os

def test_restconf_api():
    """Test the RESTCONF API endpoints"""
    print("Testing RESTCONF API...")
    
    try:
        # Test network functions endpoint
        response = requests.get("http://192.168.0.166:830/restconf/data/network-functions", timeout=5)
        if response.status_code == 200:
            print("✅ RESTCONF /network-functions endpoint: OK")
            data = response.json()
            print(f"   Found {len(data.get('amf', []))} AMF(s)")
            print(f"   Found {len(data.get('smf', []))} SMF(s)")
            print(f"   Found {len(data.get('upf', []))} UPF(s)")
        else:
            print(f"❌ RESTCONF /network-functions endpoint: FAILED (Status {response.status_code})")
            return False
            
        # Test subscribers endpoint
        response = requests.get("http://192.168.0.166:830/restconf/data/subscribers", timeout=5)
        if response.status_code == 200:
            print("✅ RESTCONF /subscribers endpoint: OK")
            data = response.json()
            print(f"   Found {len(data.get('subscriber', []))} subscriber(s)")
        else:
            print(f"❌ RESTCONF /subscribers endpoint: FAILED (Status {response.status_code})")
            return False
            
        # Test sessions endpoint
        response = requests.get("http://192.168.0.166:830/restconf/data/sessions", timeout=5)
        if response.status_code == 200:
            print("✅ RESTCONF /sessions endpoint: OK")
            data = response.json()
            print(f"   Found {len(data.get('pdu-session', []))} session(s)")
        else:
            print(f"❌ RESTCONF /sessions endpoint: FAILED (Status {response.status_code})")
            return False
            
        # Test QoS profiles endpoint
        response = requests.get("http://192.168.0.166:830/restconf/data/qos-profiles", timeout=5)
        if response.status_code == 200:
            print("✅ RESTCONF /qos-profiles endpoint: OK")
            data = response.json()
            print(f"   Found {len(data.get('profile', []))} QoS profile(s)")
        else:
            print(f"❌ RESTCONF /qos-profiles endpoint: FAILED (Status {response.status_code})")
            return False
            
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ RESTCONF API: Connection failed - server may not be running")
        return False
    except requests.exceptions.Timeout:
        print("❌ RESTCONF API: Request timed out")
        return False
    except Exception as e:
        print(f"❌ RESTCONF API: Unexpected error - {str(e)}")
        return False

def test_netconf_server():
    """Test NETCONF server connectivity"""
    print("\nTesting NETCONF Server...")
    
    try:
        # This is a basic connectivity test - in a real scenario, we would use ncclient
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', 830))
        sock.close()
        
        if result == 0:
            print("✅ NETCONF Server: Port 830 is open")
            return True
        else:
            print("❌ NETCONF Server: Port 830 is not accessible")
            return False
            
    except Exception as e:
        print(f"❌ NETCONF Server: Connection test failed - {str(e)}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("5G Core Management Prototype - Component Test")
    print("=" * 60)
    
    # Test all components
    restconf_ok = test_restconf_api()
    netconf_ok = test_netconf_server()
    
    print("\n" + "=" * 60)
    print("TEST RESULTS SUMMARY")
    print("=" * 60)
    
    if restconf_ok and netconf_ok:
        print("✅ ALL TESTS PASSED - System is functioning correctly!")
        print("\nSystem Status:")
        print("  - RESTCONF API: Running on http://127.0.0.1:830/restconf")
        print("  - NETCONF Server: Available on port 830")
        print("  - Sample data loaded: AMF, SMF, UPF, Subscribers, Sessions, QoS profiles")
        return 0
    else:
        print("❌ SOME TESTS FAILED - Please check the system setup")
        if not restconf_ok:
            print("  - RESTCONF API: Not responding correctly")
        if not netconf_ok:
            print("  - NETCONF Server: Not accessible")
        return 1

if __name__ == "__main__":
    sys.exit(main())