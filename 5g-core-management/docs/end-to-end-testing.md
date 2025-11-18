# End-to-End Testing Guide

This document provides instructions for testing end-to-end connectivity in the 5G core network, from UE registration to PDU session establishment and data flow.

## Overview

End-to-end testing verifies that all components of the 5G core network are working together correctly. This includes:

1. UE registration with the AMF
2. PDU session establishment with the SMF and UPF
3. Data flow through the user plane
4. Management interface functionality

## Prerequisites

Before performing end-to-end testing, ensure:

1. All network functions are running (AMF, SMF, UPF, etc.)
2. The management services are running (NETCONF, RESTCONF, SNMP)
3. The database (MongoDB) is accessible
4. Network connectivity between all components

## Test Scenarios

### Scenario 1: UE Registration

This test verifies that a UE can successfully register with the network.

#### Steps

1. **Provision Subscriber**: Add a subscriber to the database
   ```bash
   curl -X POST http://localhost:8081/restconf/data/subscribers/subscriber \
     -H "Content-Type: application/json" \
     -d '{
       "imsi": "001010000000003",
       "msisdn": "1234567892",
       "status": "active",
       "apn": "internet",
       "qci": 9,
       "arp": 8,
       "security": {
         "auth-key": "22334455667788990011aabbccddeeff",
         "opc": "ffeeffddccbbaa998877665544332211"
       },
       "ambr": {
         "uplink": "50000000",
         "downlink": "100000000"
       }
     }'
   ```

2. **Simulate UE Registration**: Use a UE simulator to initiate registration

3. **Verify Registration**: Check that the UE is registered
   ```bash
   # Check AMF metrics via SNMP
   snmpget -v2c -c public localhost 1.3.6.1.4.1.55555.1.1.1
   ```

4. **Check Management Interfaces**: Verify the subscriber appears in management interfaces
   ```bash
   curl -X GET http://localhost:8081/restconf/data/subscribers/subscriber/001010000000003
   ```

#### Expected Results

- UE registration succeeds
- AMF active sessions count increases
- Subscriber appears in management interfaces

### Scenario 2: PDU Session Establishment

This test verifies that a UE can establish a PDU session.

#### Steps

1. **Initiate PDU Session**: Use the UE simulator to request a PDU session

2. **Verify Session**: Check that the PDU session is established
   ```bash
   # Check SMF metrics via SNMP
   snmpget -v2c -c public localhost 1.3.6.1.4.1.55555.1.2.1
   ```

3. **Check Management Interfaces**: Verify the session appears in management interfaces
   ```bash
   curl -X GET http://localhost:8081/restconf/data/sessions/pdu-session
   ```

#### Expected Results

- PDU session establishment succeeds
- SMF active PDU sessions count increases
- Session appears in management interfaces

### Scenario 3: Data Flow

This test verifies that user data can flow through the network.

#### Steps

1. **Generate Traffic**: Use the UE simulator to generate user data traffic

2. **Monitor Throughput**: Check UPF throughput metrics
   ```bash
   # Check UPF metrics via SNMP
   snmpget -v2c -c public localhost 1.3.6.1.4.1.55555.1.3.2
   ```

3. **Verify Packet Loss**: Check UPF packet loss metrics
   ```bash
   snmpget -v2c -c public localhost 1.3.6.1.4.1.55555.1.3.3
   ```

#### Expected Results

- Data flows successfully through the network
- UPF throughput increases during traffic generation
- Packet loss remains within acceptable limits

### Scenario 4: Management Interface Operations

This test verifies that all management interfaces are functioning correctly.

#### Steps

1. **NETCONF Operations**:
   - Connect to the NETCONF server
   - Retrieve configuration data
   - Modify configuration data

2. **RESTCONF Operations**:
   - Retrieve network function data
   - Create a new network function
   - Update an existing network function
   - Delete a network function

3. **SNMP Operations**:
   - Retrieve metrics using snmpget
   - Walk the MIB tree using snmpwalk

#### Expected Results

- All management operations succeed
- Data is consistent across interfaces
- Metrics are updated in real-time

## Automated Testing

The project includes automated tests for end-to-end scenarios.

### Running Tests

To run the end-to-end tests:

```bash
cd tests
python -m pytest e2e-tests/
```

### Test Structure

The end-to-end tests are organized as follows:

1. **test_registration.py**: Tests UE registration scenarios
2. **test_session.py**: Tests PDU session establishment scenarios
3. **test_data_flow.py**: Tests user data flow scenarios
4. **test_management.py**: Tests management interface scenarios

## Monitoring During Testing

During testing, monitor the following:

### Grafana Dashboard

Open the Grafana dashboard to observe real-time metrics:

1. AMF metrics (active sessions, CPU/memory utilization)
2. SMF metrics (active PDU sessions, CPU/memory utilization)
3. UPF metrics (active users, throughput, packet loss)

### Log Analysis

Monitor logs from all components:

```bash
# AMF logs
sudo journalctl -u open5gs-amf -f

# SMF logs
sudo journalctl -u open5gs-smf -f

# UPF logs
sudo journalctl -u open5gs-upf -f

# Management service logs
tail -f management-plane/netconf-server/netconf.log
tail -f management-plane/restconf-api/restconf.log
tail -f management-plane/snmp-monitor/snmp.log
```

## Performance Metrics

During testing, collect the following performance metrics:

### Latency

- Registration latency
- PDU session establishment latency
- Data plane latency

### Throughput

- Control plane throughput
- User plane throughput

### Resource Utilization

- CPU utilization by network functions
- Memory utilization by network functions
- Network interface utilization

## Troubleshooting

### Common Issues

1. **Registration Failure**: Check subscriber provisioning and security parameters
2. **Session Establishment Failure**: Verify DNN configuration and QoS parameters
3. **Data Flow Issues**: Check UPF configuration and routing
4. **Management Interface Issues**: Verify service availability and authentication

### Debugging Tools

1. **Wireshark**: Capture and analyze network traffic
2. **tcpdump**: Command-line packet capture
3. **Logs**: Check component logs for error messages
4. **Metrics**: Monitor real-time metrics for anomalies

## Test Results Documentation

Document test results including:

1. **Test Execution**: Date, time, and environment
2. **Test Scenarios**: Which scenarios were executed
3. **Results**: Pass/fail status for each scenario
4. **Metrics**: Performance metrics collected
5. **Issues**: Any issues encountered and their resolution

## Next Steps

After completing end-to-end testing, you can:

1. Optimize network performance based on test results
2. Implement additional test scenarios
3. Integrate with continuous integration systems
4. Perform load and stress testing
5. Document lessons learned for future deployments