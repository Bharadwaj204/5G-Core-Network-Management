# RESTCONF API

Implementation of the RESTCONF protocol for 5G core network management following RFC 8040 standards.

## Overview

The RESTCONF API provides a modern, HTTP-based interface for managing 5G core network functions. It follows the RESTCONF standard defined in RFC 8040 and uses JSON for data exchange, making it easy to integrate with modern applications and tools.

## Features

- RFC 8040 compliant RESTCONF implementation
- JSON-based data exchange
- Full CRUD operations for all resources
- Standard HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Error handling with appropriate HTTP status codes
- Resource discovery endpoints

## Requirements

- Python 3.8 or higher
- Flask
- lxml

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

```bash
python restconf_server.py
```

The server will start on port 8081 by default.

### API Endpoints

#### Discovery Endpoints
- `GET /.well-known/host-meta` - RESTCONF root discovery
- `GET /restconf` - RESTCONF capabilities
- `GET /restconf/data` - All network data

#### Network Functions
- `GET /restconf/data/network-functions` - Get all network functions
- `GET /restconf/data/network-functions/amf` - Get all AMFs
- `GET /restconf/data/network-functions/amf/<amf_id>` - Get specific AMF
- `POST /restconf/data/network-functions/amf` - Create new AMF
- `PUT /restconf/data/network-functions/amf/<amf_id>` - Update existing AMF
- `PATCH /restconf/data/network-functions/amf/<amf_id>` - Partially update AMF
- `DELETE /restconf/data/network-functions/amf/<amf_id>` - Delete AMF

#### Subscribers
- `GET /restconf/data/subscribers` - Get all subscribers
- `GET /restconf/data/subscribers/subscriber` - Get all subscribers
- `GET /restconf/data/subscribers/subscriber/<imsi>` - Get specific subscriber
- `POST /restconf/data/subscribers/subscriber` - Create new subscriber
- `PUT /restconf/data/subscribers/subscriber/<imsi>` - Update existing subscriber
- `DELETE /restconf/data/subscribers/subscriber/<imsi>` - Delete subscriber

#### Sessions
- `GET /restconf/data/sessions` - Get all sessions
- `GET /restconf/data/sessions/pdu-session` - Get all PDU sessions
- `GET /restconf/data/sessions/pdu-session/<session_id>` - Get specific session
- `POST /restconf/data/sessions/pdu-session` - Create new session
- `PUT /restconf/data/sessions/pdu-session/<session_id>` - Update existing session
- `DELETE /restconf/data/sessions/pdu-session/<session_id>` - Delete session

#### QoS Profiles
- `GET /restconf/data/qos-profiles` - Get all QoS profiles
- `GET /restconf/data/qos-profiles/profile` - Get all profiles
- `GET /restconf/data/qos-profiles/profile/<profile_id>` - Get specific profile
- `POST /restconf/data/qos-profiles/profile` - Create new profile
- `PUT /restconf/data/qos-profiles/profile/<profile_id>` - Update existing profile
- `DELETE /restconf/data/qos-profiles/profile/<profile_id>` - Delete profile

## API Examples

### Get All Network Functions
```bash
curl http://localhost:8081/restconf/data/network-functions
```

### Get Specific Subscriber
```bash
curl http://localhost:8081/restconf/data/subscribers/subscriber/001010000000001
```

### Create New Session
```bash
curl -X POST http://localhost:8081/restconf/data/sessions/pdu-session \
  -H "Content-Type: application/json" \
  -d '{
    "session-id": "session-002",
    "imsi": "001010000000002",
    "status": "active",
    "sst": 1,
    "sd": "000002",
    "dnn": "internet",
    "qos": {
      "qfi": 2,
      "arp": 9,
      "gbr-ul": "2000000",
      "gbr-dl": "4000000",
      "mbr-ul": "10000000",
      "mbr-dl": "20000000"
    }
  }'
```

### Update QoS Profile
```bash
curl -X PUT http://localhost:8081/restconf/data/qos-profiles/profile/qos-profile-001 \
  -H "Content-Type: application/json" \
  -d '{
    "profile-id": "qos-profile-001",
    "qfi": 1,
    "resource-type": "gbr",
    "priority-level": 8,
    "packet-delay-budget": 150,
    "packet-error-rate": "1e-5",
    "gbr": {
      "uplink": "1500000",
      "downlink": "3000000"
    },
    "mbr": {
      "uplink": "7500000",
      "downlink": "15000000"
    }
  }'
```

## Sample Data

The API is pre-loaded with sample data:
- 1 AMF (Access and Mobility Management Function)
- 1 SMF (Session Management Function)
- 1 UPF (User Plane Function)
- 1 Subscriber with complete security parameters
- 1 PDU Session
- 1 QoS Profile

## Testing

Run the test suite to verify functionality:
```bash
cd ../../tests
python test_restconf_api.py
```

## Standards Compliance

This implementation follows:
- RFC 8040 - RESTCONF Protocol
- RFC 7951 - JSON Encoding of Data Modeled with YANG
- RFC 7950 - The YANG 1.1 Data Modeling Language