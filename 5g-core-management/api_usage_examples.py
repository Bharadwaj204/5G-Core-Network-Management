#!/usr/bin/env python3
"""
API Usage Examples for the 5G Core Management Prototype
"""

import requests
import json

# Server address
SERVER_URL = "http://192.168.0.166:830"
RESTCONF_BASE = f"{SERVER_URL}/restconf/data"

def print_response(title, response):
    """Pretty print API response"""
    print(f"\n{title}")
    print("-" * len(title))
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        try:
            data = response.json()
            print("Response Data:")
            print(json.dumps(data, indent=2))
        except:
            print("Response Data:")
            print(response.text)
    else:
        print(f"Error: {response.text}")

def main():
    """Demonstrate API usage"""
    print("5G Core Management Prototype - API Usage Examples")
    print("=" * 50)
    
    # Example 1: Get all network functions
    response = requests.get(f"{RESTCONF_BASE}/network-functions")
    print_response("1. Get All Network Functions", response)
    
    # Example 2: Get all subscribers
    response = requests.get(f"{RESTCONF_BASE}/subscribers")
    print_response("2. Get All Subscribers", response)
    
    # Example 3: Get all sessions
    response = requests.get(f"{RESTCONF_BASE}/sessions")
    print_response("3. Get All Sessions", response)
    
    # Example 4: Get all QoS profiles
    response = requests.get(f"{RESTCONF_BASE}/qos-profiles")
    print_response("4. Get All QoS Profiles", response)
    
    # Example 5: Get specific AMF
    response = requests.get(f"{RESTCONF_BASE}/network-functions/amf/amf-001")
    print_response("5. Get Specific AMF (amf-001)", response)
    
    # Example 6: Get specific subscriber
    response = requests.get(f"{RESTCONF_BASE}/subscribers")
    print_response("6. Get Specific Subscriber (001010000000001)", response)
    
    print("\n" + "=" * 50)
    print("API Usage Examples Completed")
    print("=" * 50)

if __name__ == "__main__":
    main()