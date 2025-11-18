#!/usr/bin/env python3

"""
SNMP Poller for 5G Core Network Metrics
This script polls metrics from the 5G core network functions via SNMP
and exports them to various formats.
"""

from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity  # type: ignore

import json
import csv
import time
from datetime import datetime

# SNMP target configuration
SNMP_TARGET = 'localhost'
SNMP_PORT = 161
SNMP_COMMUNITY = 'public'

# Base OID for our 5G core metrics
BASE_OID = '1.3.6.1.4.1.55555'

# AMF metrics OIDs
AMF_ACTIVE_SESSIONS_OID = f'{BASE_OID}.1.1.1'
AMF_CPU_UTILIZATION_OID = f'{BASE_OID}.1.1.2'
AMF_MEMORY_UTILIZATION_OID = f'{BASE_OID}.1.1.3'

# SMF metrics OIDs
SMF_ACTIVE_PDU_SESSIONS_OID = f'{BASE_OID}.1.2.1'
SMF_CPU_UTILIZATION_OID = f'{BASE_OID}.1.2.2'
SMF_MEMORY_UTILIZATION_OID = f'{BASE_OID}.1.2.3'

# UPF metrics OIDs
UPF_ACTIVE_USERS_OID = f'{BASE_OID}.1.3.1'
UPF_THROUGHPUT_OID = f'{BASE_OID}.1.3.2'
UPF_PACKET_LOSS_OID = f'{BASE_OID}.1.3.3'

# List of OIDs to poll
OID_LIST = [
    ('amf_active_sessions', AMF_ACTIVE_SESSIONS_OID),
    ('amf_cpu_utilization', AMF_CPU_UTILIZATION_OID),
    ('amf_memory_utilization', AMF_MEMORY_UTILIZATION_OID),
    ('smf_active_pdu_sessions', SMF_ACTIVE_PDU_SESSIONS_OID),
    ('smf_cpu_utilization', SMF_CPU_UTILIZATION_OID),
    ('smf_memory_utilization', SMF_MEMORY_UTILIZATION_OID),
    ('upf_active_users', UPF_ACTIVE_USERS_OID),
    ('upf_throughput', UPF_THROUGHPUT_OID),
    ('upf_packet_loss', UPF_PACKET_LOSS_OID)
]

def snmp_get(oid):
    """Perform SNMP GET operation for a single OID"""
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(SNMP_COMMUNITY),
        UdpTransportTarget((SNMP_TARGET, SNMP_PORT)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    
    if errorIndication:
        print(f"SNMP Error: {errorIndication}")
        return None
    elif errorStatus:
        print(f"SNMP Error: {errorStatus.prettyPrint()}")
        return None
    else:
        for varBind in varBinds:
            # Return the value part of the OID-value pair
            return varBind[1]
    return None

def poll_metrics():
    """Poll all metrics from the SNMP agent"""
    metrics = {}
    timestamp = datetime.now().isoformat()
    
    print(f"Polling metrics at {timestamp}")
    
    for name, oid in OID_LIST:
        value = snmp_get(oid)
        if value is not None:
            metrics[name] = str(value)
            print(f"  {name}: {value}")
        else:
            metrics[name] = "N/A"
            print(f"  {name}: N/A")
    
    metrics['timestamp'] = timestamp
    return metrics

def export_to_json(metrics, filename):
    """Export metrics to JSON file"""
    with open(filename, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f"Metrics exported to {filename}")

def export_to_csv(metrics, filename):
    """Export metrics to CSV file"""
    # Create file with headers if it doesn't exist
    file_exists = False
    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass
    
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        
        # Write headers if file is new
        if not file_exists:
            headers = ['timestamp'] + [name for name, _ in OID_LIST]
            writer.writerow(headers)
        
        # Write metrics data
        row = [metrics['timestamp']] + [metrics[name] for name, _ in OID_LIST]
        writer.writerow(row)
    
    print(f"Metrics appended to {filename}")

def continuous_polling(interval=30, export_format='json'):
    """Continuously poll metrics at specified interval"""
    print(f"Starting continuous polling every {interval} seconds...")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            metrics = poll_metrics()
            
            # Export based on format
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if export_format.lower() == 'json':
                export_to_json(metrics, f"metrics_{timestamp}.json")
            elif export_format.lower() == 'csv':
                export_to_csv(metrics, "metrics.csv")
            elif export_format.lower() == 'both':
                export_to_json(metrics, f"metrics_{timestamp}.json")
                export_to_csv(metrics, "metrics.csv")
            
            print(f"Waiting {interval} seconds...\n")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping continuous polling...")

def main():
    """Main function"""
    print("5G Core SNMP Metrics Poller")
    print("=" * 30)
    
    # Single poll example
    metrics = poll_metrics()
    export_to_json(metrics, "metrics.json")
    
    # Uncomment the following line to start continuous polling
    # continuous_polling(interval=30, export_format='both')

if __name__ == "__main__":
    main()