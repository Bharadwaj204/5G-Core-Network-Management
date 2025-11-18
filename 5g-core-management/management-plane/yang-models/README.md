# YANG Models

Standardized YANG data models for 5G core network management including subscriber, session, and QoS parameters.

## Overview

This directory contains YANG data models that define the structure and semantics of 5G core network configuration and state data. These models are used by the NETCONF and RESTCONF implementations to ensure standardized data exchange.

## YANG Models

### Subscriber Management Model
File: [subscriber-management.yang](subscriber-management.yang)
- Defines the structure for subscriber information
- Includes IMSI, MSISDN, security parameters, and QoS settings
- Supports subscriber lifecycle management

### Session Management Model
File: [session-management.yang](session-management.yang)
- Defines the structure for PDU session information
- Includes session identifiers, QoS profiles, and state information
- Supports session establishment and modification

### QoS Parameters Model
File: [qos-parameters.yang](qos-parameters.yang)
- Defines the structure for Quality of Service profiles
- Includes GBR/MBR parameters, packet delay budgets, and priority levels
- Supports QoS profile management and assignment

## Validation

All YANG models have been validated using the pyang tool:

```bash
pyang subscriber-management.yang
pyang session-management.yang
pyang qos-parameters.yang
```

## Model Structure

### Subscriber Management
```
subscribers
├── subscriber [key: imsi]
    ├── imsi
    ├── msisdn
    ├── status
    ├── apn
    ├── qci
    ├── arp
    ├── security
    │   ├── auth-key
    │   └── opc
    └── ambr
        ├── uplink
        └── downlink
```

### Session Management
```
sessions
└── pdu-session [key: session-id]
    ├── session-id
    ├── imsi
    ├── status
    ├── sst
    ├── sd
    ├── dnn
    └── qos
        ├── qfi
        ├── arp
        ├── gbr-ul
        ├── gbr-dl
        ├── mbr-ul
        └── mbr-dl
```

### QoS Parameters
```
qos-profiles
└── profile [key: profile-id]
    ├── profile-id
    ├── qfi
    ├── resource-type
    ├── priority-level
    ├── packet-delay-budget
    ├── packet-error-rate
    ├── gbr
    │   ├── uplink
    │   └── downlink
    └── mbr
        ├── uplink
        └── downlink
```

## Usage

### Validation
To validate the YANG models:
```bash
pyang -f tree subscriber-management.yang
pyang -f tree session-management.yang
pyang -f tree qos-parameters.yang
```

### Compilation
To generate Python bindings:
```bash
pyang -f pybind subscriber-management.yang > subscriber_management.py
```

### Documentation
To generate HTML documentation:
```bash
pyang -f jstree subscriber-management.yang > subscriber-management.html
```

## Integration

These YANG models are integrated with:
- NETCONF server for configuration management
- RESTCONF API for HTTP-based access
- SNMP monitor for metrics exposure

## Example Data Instances

### Subscriber Instance
```xml
<subscriber>
  <imsi>001010000000001</imsi>
  <msisdn>1234567890</msisdn>
  <status>active</status>
  <apn>internet</apn>
  <qci>9</qci>
  <arp>8</arp>
  <security>
    <auth-key>00112233445566778899aabbccddeeff</auth-key>
    <opc>ffeeddccbbaa99887766554433221100</opc>
  </security>
  <ambr>
    <uplink>100000000</uplink>
    <downlink>200000000</downlink>
  </ambr>
</subscriber>
```

### Session Instance
```xml
<pdu-session>
  <session-id>session-001</session-id>
  <imsi>001010000000001</imsi>
  <status>active</status>
  <sst>1</sst>
  <sd>000001</sd>
  <dnn>internet</dnn>
  <qos>
    <qfi>1</qfi>
    <arp>8</arp>
    <gbr-ul>1000000</gbr-ul>
    <gbr-dl>2000000</gbr-dl>
    <mbr-ul>5000000</mbr-ul>
    <mbr-dl>10000000</mbr-dl>
  </qos>
</pdu-session>
```

### QoS Profile Instance
```xml
<profile>
  <profile-id>qos-profile-001</profile-id>
  <qfi>1</qfi>
  <resource-type>gbr</resource-type>
  <priority-level>8</priority-level>
  <packet-delay-budget>100</packet-delay-budget>
  <packet-error-rate>1e-6</packet-error-rate>
  <gbr>
    <uplink>1000000</uplink>
    <downlink>2000000</downlink>
  </gbr>
  <mbr>
    <uplink>5000000</uplink>
    <downlink>10000000</downlink>
  </mbr>
</profile>
```

## Standards Compliance

These models follow:
- RFC 7950 - The YANG 1.1 Data Modeling Language
- RFC 7951 - JSON Encoding of Data Modeled with YANG
- 3GPP TS 29.510 - Network Function Repository Services