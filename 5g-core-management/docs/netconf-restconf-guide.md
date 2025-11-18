# NETCONF and RESTCONF Guide

This document provides detailed instructions on how to use the NETCONF and RESTCONF APIs for managing the 5G core network.

## Overview

NETCONF and RESTCONF are standardized protocols for network configuration management. This project implements both protocols to provide flexible management interfaces for the 5G core network.

## NETCONF API

The NETCONF server provides a standards-compliant interface for managing network configuration.

### Connecting to the NETCONF Server

The NETCONF server runs on port 830. You can connect using any NETCONF client.

Example using ssh:

```bash
ssh -p 830 admin@localhost
```

### NETCONF Operations

The server supports the following standard NETCONF operations:

1. **get-config**: Retrieve configuration data
2. **edit-config**: Modify configuration data
3. **copy-config**: Copy configuration between datastores
4. **delete-config**: Delete configuration data
5. **lock/unlock**: Lock and unlock configuration datastores
6. **get**: Retrieve both configuration and state data

### Example NETCONF Session

Here's an example NETCONF session using the ncclient Python library:

```python
from ncclient import manager

# Connect to the NETCONF server
with manager.connect(host='localhost',
                     port=830,
                     username='admin',
                     password='admin',
                     hostkey_verify=False) as m:
    
    # Get configuration
    config = m.get_config(source='running')
    print(config.data_xml)
    
    # Edit configuration (example)
    config_xml = """
    <config>
      <network-functions xmlns="urn:5g-core:nf">
        <amf>
          <id>amf-001</id>
          <status>active</status>
          <capacity>50</capacity>
        </amf>
      </network-functions>
    </config>
    """
    
    # Apply configuration
    m.edit_config(target='running', config=config_xml)
```

## RESTCONF API

The RESTCONF API provides a web-based interface for managing the 5G core network, following RFC 8040 standards.

### API Endpoints

#### Network Functions

- **GET /restconf/data/network-functions**: Get all network functions
- **GET /restconf/data/network-functions/amf**: Get all AMFs
- **GET /restconf/data/network-functions/amf/{id}**: Get specific AMF
- **POST /restconf/data/network-functions/amf**: Create new AMF
- **PUT /restconf/data/network-functions/amf/{id}**: Update existing AMF
- **DELETE /restconf/data/network-functions/amf/{id}**: Delete AMF

- **GET /restconf/data/network-functions/smf**: Get all SMFs
- **GET /restconf/data/network-functions/smf/{id}**: Get specific SMF
- **POST /restconf/data/network-functions/smf**: Create new SMF
- **PUT /restconf/data/network-functions/smf/{id}**: Update existing SMF
- **DELETE /restconf/data/network-functions/smf/{id}**: Delete SMF

- **GET /restconf/data/network-functions/upf**: Get all UPFs
- **GET /restconf/data/network-functions/upf/{id}**: Get specific UPF
- **POST /restconf/data/network-functions/upf**: Create new UPF
- **PUT /restconf/data/network-functions/upf/{id}**: Update existing UPF
- **DELETE /restconf/data/network-functions/upf/{id}**: Delete UPF

#### Subscribers

- **GET /restconf/data/subscribers**: Get all subscribers
- **GET /restconf/data/subscribers/subscriber**: Get all subscribers
- **GET /restconf/data/subscribers/subscriber/{imsi}**: Get specific subscriber
- **POST /restconf/data/subscribers/subscriber**: Create new subscriber
- **PUT /restconf/data/subscribers/subscriber/{imsi}**: Update existing subscriber
- **DELETE /restconf/data/subscribers/subscriber/{imsi}**: Delete subscriber

#### Sessions

- **GET /restconf/data/sessions**: Get all sessions
- **GET /restconf/data/sessions/pdu-session**: Get all PDU sessions
- **GET /restconf/data/sessions/pdu-session/{session-id}**: Get specific PDU session
- **POST /restconf/data/sessions/pdu-session**: Create new PDU session
- **PUT /restconf/data/sessions/pdu-session/{session-id}**: Update existing PDU session
- **DELETE /restconf/data/sessions/pdu-session/{session-id}**: Delete PDU session

#### QoS Profiles

- **GET /restconf/data/qos-profiles**: Get all QoS profiles
- **GET /restconf/data/qos-profiles/profile**: Get all QoS profiles
- **GET /restconf/data/qos-profiles/profile/{profile-id}**: Get specific QoS profile
- **POST /restconf/data/qos-profiles/profile**: Create new QoS profile
- **PUT /restconf/data/qos-profiles/profile/{profile-id}**: Update existing QoS profile
- **DELETE /restconf/data/qos-profiles/profile/{profile-id}**: Delete QoS profile

### Example API Calls

#### Get All Network Functions

```bash
curl -X GET http://localhost:8081/restconf/data/network-functions
```

#### Get Specific AMF

```bash
curl -X GET http://localhost:8081/restconf/data/network-functions/amf/amf-001
```

#### Create New AMF

```bash
curl -X POST http://localhost:8081/restconf/data/network-functions/amf \
  -H "Content-Type: application/json" \
  -d '{
    "id": "amf-002",
    "status": "active",
    "capacity": 30,
    "mcc": "001",
    "mnc": "01",
    "region-id": 1,
    "set-id": 1,
    "pointer": 1
  }'
```

#### Update Existing AMF

```bash
curl -X PUT http://localhost:8081/restconf/data/network-functions/amf/amf-001 \
  -H "Content-Type: application/json" \
  -d '{
    "id": "amf-001",
    "status": "active",
    "capacity": 60,
    "mcc": "001",
    "mnc": "01",
    "region-id": 1,
    "set-id": 1,
    "pointer": 1
  }'
```

#### Delete AMF

```bash
curl -X DELETE http://localhost:8081/restconf/data/network-functions/amf/amf-001
```

### Authentication and Authorization

The RESTCONF API currently does not implement authentication. In a production environment, you would need to add:

1. **Basic Authentication**: Username and password protection
2. **Token-based Authentication**: OAuth or JWT tokens
3. **Certificate-based Authentication**: Client certificates
4. **Role-based Access Control**: Different permissions for different users

### Error Handling

The RESTCONF API returns standard HTTP status codes:

- **200 OK**: Successful GET, PUT, or PATCH request
- **201 Created**: Successful POST request
- **204 No Content**: Successful DELETE request
- **400 Bad Request**: Invalid request data
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Access denied
- **404 Not Found**: Resource not found
- **405 Method Not Allowed**: HTTP method not supported
- **409 Conflict**: Resource conflict
- **500 Internal Server Error**: Server error

Error responses include a JSON body with error details:

```json
{
  "error": "AMF not found"
}
```

## Using the APIs for Management

### Subscriber Provisioning

To provision a new subscriber:

1. Create the subscriber using the RESTCONF API:
   ```bash
   curl -X POST http://localhost:8081/restconf/data/subscribers/subscriber \
     -H "Content-Type: application/json" \
     -d '{
       "imsi": "001010000000002",
       "msisdn": "1234567891",
       "status": "active",
       "apn": "internet",
       "qci": 9,
       "arp": 8,
       "security": {
         "auth-key": "11223344556677889900aabbccddeeff",
         "opc": "eeffddccbbaa99887766554433221100"
       },
       "ambr": {
         "uplink": "50000000",
         "downlink": "100000000"
       }
     }'
   ```

2. Verify the subscriber was created:
   ```bash
   curl -X GET http://localhost:8081/restconf/data/subscribers/subscriber/001010000000002
   ```

### Network Function Management

To manage network functions:

1. Get all AMFs:
   ```bash
   curl -X GET http://localhost:8081/restconf/data/network-functions/amf
   ```

2. Update an AMF's capacity:
   ```bash
   curl -X PUT http://localhost:8081/restconf/data/network-functions/amf/amf-001 \
     -H "Content-Type: application/json" \
     -d '{
       "id": "amf-001",
       "status": "active",
       "capacity": 75,
       "mcc": "001",
       "mnc": "01",
       "region-id": 1,
       "set-id": 1,
       "pointer": 1
     }'
   ```

### Session Management

To manage PDU sessions:

1. Create a new PDU session:
   ```bash
   curl -X POST http://localhost:8081/restconf/data/sessions/pdu-session \
     -H "Content-Type: application/json" \
     -d '{
       "session-id": "session-002",
       "imsi": "001010000000002",
       "status": "active",
       "sst": 1,
       "sd": "000001",
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

2. Get all PDU sessions:
   ```bash
   curl -X GET http://localhost:8081/restconf/data/sessions/pdu-session
   ```

## Testing and Validation

### Automated Testing

The project includes automated tests for both APIs:

1. **NETCONF Tests**: Located in `tests/netconf-tests/`
2. **RESTCONF Tests**: Located in `tests/restconf-tests/`

Run the tests using pytest:

```bash
cd tests
python -m pytest netconf-tests/
python -m pytest restconf-tests/
```

### Manual Testing

For manual testing, you can use tools like:

1. **curl**: For RESTCONF API testing
2. **ncclient**: For NETCONF testing
3. **Postman**: For RESTCONF API testing with a GUI
4. **Netopeer**: For NETCONF testing with a GUI

## Security Considerations

When using the management APIs, consider the following security aspects:

1. **Transport Security**: Use HTTPS/TLS for RESTCONF and SSH for NETCONF
2. **Authentication**: Implement strong authentication mechanisms
3. **Authorization**: Use role-based access control
4. **Input Validation**: Validate all input data against the YANG models
5. **Audit Logging**: Log all management operations
6. **Rate Limiting**: Implement rate limiting to prevent abuse

## Troubleshooting

### Common Issues

1. **Connection Refused**: Check that the services are running and listening on the correct ports.

2. **Authentication Errors**: Verify credentials and authentication configuration.

3. **Invalid Data**: Ensure data conforms to the YANG models.

4. **Permission Denied**: Check authorization policies.

### Debugging Tools

1. **Wireshark**: Capture and analyze network traffic
2. **tcpdump**: Command-line packet capture
3. **Logs**: Check service logs for error messages
4. **API Documentation**: Refer to the API documentation for correct usage

## Next Steps

After learning to use the NETCONF and RESTCONF APIs, you can:

1. Integrate with network management systems
2. Develop custom management applications
3. Automate network configuration tasks
4. Monitor network state and performance
5. Implement advanced management features