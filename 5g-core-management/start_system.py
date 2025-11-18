#!/usr/bin/env python3
"""
Startup script for the 5G Core Management Prototype
"""

import subprocess
import sys
import time
import requests
import threading

def start_netconf_server():
    """Start the NETCONF/RESTCONF server"""
    try:
        print("Starting NETCONF/RESTCONF Server...")
        # Change to the netconf-server directory and start the server
        subprocess.Popen([
            sys.executable, 
            "netconf_server.py"
        ], cwd="management-plane/netconf-server")
        print("NETCONF/RESTCONF Server started successfully")
        return True
    except Exception as e:
        print(f"Failed to start NETCONF/RESTCONF Server: {e}")
        return False

def start_snmp_agent():
    """Start the SNMP agent"""
    try:
        print("Starting SNMP Agent...")
        # Change to the snmp-monitor directory and start the agent
        subprocess.Popen([
            sys.executable, 
            "snmp_agent.py"
        ], cwd="management-plane/snmp-monitor")
        print("SNMP Agent started successfully")
        return True
    except Exception as e:
        print(f"Failed to start SNMP Agent: {e}")
        return False

def check_server_status():
    """Check if the servers are running"""
    try:
        # Check RESTCONF server
        response = requests.get("http://192.168.0.166:830/restconf/data/network-functions", timeout=5)
        if response.status_code == 200:
            print("✅ RESTCONF Server: Running")
        else:
            print("❌ RESTCONF Server: Not responding correctly")
            
        # Check NETCONF port
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('192.168.0.166', 830))
        sock.close()
        if result == 0:
            print("✅ NETCONF Server: Port 830 is open")
        else:
            print("❌ NETCONF Server: Port 830 is not accessible")
            
    except Exception as e:
        print(f"Error checking server status: {e}")

def main():
    """Main startup function"""
    print("=" * 60)
    print("5G Core Management Prototype - System Startup")
    print("=" * 60)
    
    # Start the servers
    netconf_started = start_netconf_server()
    time.sleep(3)  # Give the server time to start
    
    # Check status
    print("\nChecking system status...")
    check_server_status()
    
    print("\n" + "=" * 60)
    print("SYSTEM STARTUP COMPLETE")
    print("=" * 60)
    print("The 5G Core Management Prototype is now running!")
    print("\nAccess the system using:")
    print("  RESTCONF API: http://192.168.0.166:830/restconf")
    print("  NETCONF Server: Port 830")
    print("\nTo test the system, run:")
    print("  python test_all_components.py")
    print("  python api_usage_examples.py")
    print("\nPress Ctrl+C to stop the servers")

    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        sys.exit(0)

if __name__ == "__main__":
    main()