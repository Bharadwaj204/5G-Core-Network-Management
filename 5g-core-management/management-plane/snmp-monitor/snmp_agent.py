#!/usr/bin/env python3

"""
SNMP Agent for 5G Core Network Metrics
This agent exposes metrics from 5G core network functions via SNMP.
"""

from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.proto.api import v2c
import random
import time
import threading
from datetime import datetime

# Simulated metric values (in a real implementation, these would come from the actual 5G core)
metrics = {
    'amf_active_sessions': 1250,
    'amf_cpu_utilization': 45,
    'amf_memory_utilization': 60,
    'smf_active_pdu_sessions': 1120,
    'smf_cpu_utilization': 35,
    'smf_memory_utilization': 55,
    'upf_active_users': 980,
    'upf_throughput': 125000000,  # bits per second
    'upf_packet_loss': 0.05  # percentage
}

# Update metrics periodically with simulated data
def update_metrics():
    while True:
        # Simulate changing metrics
        metrics['amf_active_sessions'] = random.randint(1000, 1500)
        metrics['amf_cpu_utilization'] = random.randint(30, 70)
        metrics['amf_memory_utilization'] = random.randint(50, 80)
        metrics['smf_active_pdu_sessions'] = random.randint(900, 1300)
        metrics['smf_cpu_utilization'] = random.randint(25, 60)
        metrics['smf_memory_utilization'] = random.randint(45, 75)
        metrics['upf_active_users'] = random.randint(800, 1200)
        metrics['upf_throughput'] = random.randint(100000000, 150000000)
        metrics['upf_packet_loss'] = round(random.uniform(0.01, 0.1), 2)
        time.sleep(5)  # Update every 5 seconds

# SNMP MIB definitions
# These OIDs are custom for our 5G core monitoring
# In a real implementation, we would use standard 3GPP MIBs or define our own

# Base OID for our 5G core metrics
BASE_OID = (1, 3, 6, 1, 4, 1, 55555)  # Example enterprise OID

# AMF metrics OIDs
AMF_ACTIVE_SESSIONS_OID = BASE_OID + (1, 1, 1)
AMF_CPU_UTILIZATION_OID = BASE_OID + (1, 1, 2)
AMF_MEMORY_UTILIZATION_OID = BASE_OID + (1, 1, 3)

# SMF metrics OIDs
SMF_ACTIVE_PDU_SESSIONS_OID = BASE_OID + (1, 2, 1)
SMF_CPU_UTILIZATION_OID = BASE_OID + (1, 2, 2)
SMF_MEMORY_UTILIZATION_OID = BASE_OID + (1, 2, 3)

# UPF metrics OIDs
UPF_ACTIVE_USERS_OID = BASE_OID + (1, 3, 1)
UPF_THROUGHPUT_OID = BASE_OID + (1, 3, 2)
UPF_PACKET_LOSS_OID = BASE_OID + (1, 3, 3)

# SNMP Agent implementation
class SNMPAgent:
    def __init__(self):
        # Create SNMP engine
        self.snmpEngine = engine.SnmpEngine()

        # Transport setup
        config.addTransport(
            self.snmpEngine,
            udp.domainName,
            udp.UdpTransport().openServerMode(('localhost', 161))
        )

        # SNMPv2c setup
        config.addV1System(self.snmpEngine, '5g-core-agent', 'public')

        config.addTargetParams(
            self.snmpEngine, '5g-core-params', '5g-core-agent', 'noAuthNoPriv', 1
        )

        # Create SNMP context
        self.snmpContext = context.SnmpContext(self.snmpEngine)

        # Register SNMP applications
        cmdrsp.GetCommandResponder(self.snmpEngine, self.snmpContext)
        cmdrsp.SetCommandResponder(self.snmpEngine, self.snmpContext)
        cmdrsp.NextCommandResponder(self.snmpEngine, self.snmpContext)
        cmdrsp.BulkCommandResponder(self.snmpEngine, self.snmpContext)

    def start(self):
        """Start the SNMP agent"""
        print("5G Core SNMP Agent starting on localhost:161")
        print("Community string: public")
        print("Press Ctrl+C to stop")
        
        # Start metrics update thread
        metrics_thread = threading.Thread(target=update_metrics)
        metrics_thread.daemon = True
        metrics_thread.start()
        
        # Create and run the SNMP dispatcher
        dispatcher = AsyncoreDispatcher()
        try:
            dispatcher.runDispatcher()
        except KeyboardInterrupt:
            print("\nShutting down SNMP agent...")
            dispatcher.closeDispatcher()
            raise

if __name__ == "__main__":
    agent = SNMPAgent()
    agent.start()