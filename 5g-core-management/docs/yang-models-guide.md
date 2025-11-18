# YANG Models Guide

This document describes the YANG models used in the 5G Core Management Prototype and how to use them.

## Overview

YANG (Yet Another Next Generation) is a data modeling language used to model configuration and state data manipulated by the NETCONF protocol. This project uses three main YANG models:

1. Subscriber Management
2. Session Management
3. QoS Parameters

## Subscriber Management Model

The subscriber management model (`subscriber-management.yang`) defines the structure for managing 5G subscribers.

### Key Components

- **subscribers**: Container for all subscriber data
- **subscriber**: List of individual subscribers
- **imsi**: International Mobile Subscriber Identity (key)
- **msisdn**: Mobile Station International Subscriber Directory Number
- **status**: Subscriber status (active, inactive, suspended)
- **apn**: Access Point Name
- **security**: Security parameters (auth-key, opc)
- **ambr**: Aggregate Maximum Bit Rate (uplink/downlink)

### Using the Model

To validate the model using pyang:

```bash
cd management-plane/yang-models
pyang -f tree subscriber-management.yang
```

This will output a tree representation of the model:

```
module: subscriber-management
  +--rw subscribers
     +--rw subscriber* [imsi]
        +--rw imsi            string
        +--rw msisdn          string
        +--rw status          enumeration
        +--rw apn             string
        +--rw qci             uint8
        +--rw arp             uint8
        +--rw security
        |  +--rw auth-key    string
        |  +--rw opc         string
        +--rw ambr
           +--rw uplink      string
           +--rw downlink    string
```

## Session Management Model

The session management model (`session-management.yang`) defines the structure for managing PDU sessions.

### Key Components

- **sessions**: Container for all session data
- **pdu-session**: List of individual PDU sessions
- **session-id**: Unique identifier for the session (key)
- **imsi**: Associated subscriber
- **status**: Session status (active, inactive, released)
- **sst**: Slice/Service Type
- **sd**: Slice Differentiator
- **dnn**: Data Network Name
- **qos**: QoS parameters (qfi, arp, gbr, mbr)

### Using the Model

To validate the model using pyang:

```bash
cd management-plane/yang-models
pyang -f tree session-management.yang
```

This will output a tree representation of the model:

```
module: session-management
  +--rw sessions
     +--rw pdu-session* [session-id]
        +--rw session-id    string
        +--rw imsi          string
        +--rw status        enumeration
        +--rw sst           uint8
        +--rw sd            string
        +--rw dnn           string
        +--rw qos
           +--rw qfi         uint8
           +--rw arp         uint8
           +--rw gbr-ul      string
           +--rw gbr-dl      string
           +--rw mbr-ul      string
           +--rw mbr-dl      string
```

## QoS Parameters Model

The QoS parameters model (`qos-parameters.yang`) defines the structure for managing QoS profiles.

### Key Components

- **qos-profiles**: Container for all QoS profiles
- **profile**: List of individual QoS profiles
- **profile-id**: Unique identifier for the profile (key)
- **qfi**: QoS Flow Identifier
- **resource-type**: Resource type (gbr, non-gbr)
- **priority-level**: Priority level
- **packet-delay-budget**: Packet delay budget in milliseconds
- **packet-error-rate**: Packet error rate
- **gbr**: Guaranteed Bit Rate parameters
- **mbr**: Maximum Bit Rate parameters

### Using the Model

To validate the model using pyang:

```bash
cd management-plane/yang-models
pyang -f tree qos-parameters.yang
```

This will output a tree representation of the model:

```
module: qos-parameters
  +--rw qos-profiles
     +--rw profile* [profile-id]
        +--rw profile-id           string
        +--rw qfi                  uint8
        +--rw resource-type        enumeration
        +--rw priority-level       uint8
        +--rw packet-delay-budget  uint16
        +--rw packet-error-rate    string
        +--rw gbr
        |  +--rw uplink    string
        |  +--rw downlink  string
        +--rw mbr
           +--rw uplink    string
           +--rw downlink  string
```

## Working with YANG Models

### Converting to Other Formats

YANG models can be converted to other formats using pyang:

1. **JSON Schema**:
   ```bash
   pyang -f jtox subscriber-management.yang > subscriber-management.json
   ```

2. **HTML Documentation**:
   ```bash
   pyang -f docs subscriber-management.yang > subscriber-management.html
   ```

3. **XSD Schema**:
   ```bash
   pyang -f xsd subscriber-management.yang > subscriber-management.xsd
   ```

### Validating Configurations

YANG models can be used to validate configurations using tools like pyang:

```bash
pyang -f yang subscriber-management.yang
```

This will check the syntax and semantics of the YANG model.

## Integration with Management Protocols

### NETCONF Integration

The YANG models are used by the NETCONF server to:

1. Define the data model for configuration data
2. Validate incoming configuration changes
3. Provide structured responses to GET operations

### RESTCONF Integration

The YANG models are used by the RESTCONF API to:

1. Map REST resources to YANG data nodes
2. Validate JSON payloads against the YANG schema
3. Provide consistent data representation across protocols

## Best Practices

### Model Design

1. **Use descriptive names**: Choose clear, descriptive names for containers, lists, and leaf nodes.

2. **Define appropriate data types**: Use the most specific data type possible (e.g., uint8 instead of string for small integers).

3. **Include descriptions**: Provide clear descriptions for all nodes to aid in understanding.

4. **Use enumerations**: Define enumerations for fields with a fixed set of values.

5. **Define constraints**: Use range and pattern statements to constrain values where appropriate.

### Model Evolution

1. **Version control**: Keep YANG models under version control to track changes.

2. **Backward compatibility**: Maintain backward compatibility when updating models.

3. **Revision statements**: Use revision statements to document changes to the model.

4. **Feature flags**: Use feature statements to enable optional functionality.

## Troubleshooting

### Common Issues

1. **Syntax errors**: Check for proper YANG syntax, including correct indentation and matching braces.

2. **Missing dependencies**: Ensure all imported modules are available.

3. **Validation failures**: Check that all constraints and data types are correctly defined.

### Tools for Debugging

1. **pyang**: Use pyang with different output formats to validate and visualize models.

2. **yanglint**: Use yanglint for detailed validation and error reporting.

3. **Online validators**: Use online YANG validators to check syntax and semantics.

## Next Steps

After understanding the YANG models, you can:

1. Use them with the NETCONF server to manage configuration
2. Interact with the RESTCONF API to retrieve and update data
3. Extend the models to include additional functionality
4. Integrate with other management systems that support YANG