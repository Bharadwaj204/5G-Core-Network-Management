# Open5GS Configuration Guide

This document provides detailed instructions for configuring Open5GS network functions.

## Overview

Open5GS is an open-source implementation of 5G core network functions. This guide covers the configuration of the main network functions:

1. AMF (Access and Mobility Management Function)
2. SMF (Session Management Function)
3. UPF (User Plane Function)
4. HSS (Home Subscriber Server)
5. UDM (Unified Data Management)
6. AUSF (Authentication Server Function)
7. NRF (Network Repository Function)

## Configuration Files

Each network function has its own configuration file in YAML format. The configuration files are located in the `open5gs-setup/config-files` directory.

### AMF Configuration

The AMF configuration file (`amf.yaml`) contains settings for:

- Network identity (MCC, MNC)
- AMF region, set, and pointer
- Network interfaces
- Security parameters

Example AMF configuration:

```yaml
# AMF Configuration
logger:
  level: info

amf:
  sbi:
    server:
      address: 127.0.0.1
      port: 7777
    client:
      nrf:
        address: 127.0.0.1
        port: 7777
  ngap:
    server:
      address: 127.0.0.1
      port: 38412
  guami:
    - plmn_id:
        mcc: 001
        mnc: 01
      amf_id:
        region: 2
        set: 1
  tai:
    - plmn_id:
        mcc: 001
        mnc: 01
      tac: 1
  plmn_support:
    - plmn_id:
        mcc: 001
        mnc: 01
      s_nssai:
        - sst: 1
          sd: 000001
```

### SMF Configuration

The SMF configuration file (`smf.yaml`) contains settings for:

- Network interfaces
- PFCP association with UPF
- DNN configuration
- QoS parameters

Example SMF configuration:

```yaml
# SMF Configuration
logger:
  level: info

smf:
  sbi:
    server:
      address: 127.0.0.1
      port: 7778
    client:
      nrf:
        address: 127.0.0.1
        port: 7777
  pfcp:
    server:
      address: 127.0.0.1
      port: 8805
  gtpc:
    server:
      address: 127.0.0.1
      port: 2123
  gtpu:
    server:
      address: 127.0.0.1
      port: 2152
  pdn:
    - dnn: internet
      ue_pool:
        - network: 10.45.0.0/16
      dns:
        - 8.8.8.8
        - 8.8.4.4
```

### UPF Configuration

The UPF configuration file (`upf.yaml`) contains settings for:

- Network interfaces
- PFCP association with SMF
- User plane IP addresses
- QoS handling

Example UPF configuration:

```yaml
# UPF Configuration
logger:
  level: info

upf:
  pfcp:
    server:
      address: 127.0.0.1
      port: 8805
    client:
      smf:
        address: 127.0.0.1
        port: 8805
  gtpu:
    server:
      address: 127.0.0.1
      port: 2152
  session:
    - subnet: 10.45.0.0/16
```

### HSS Configuration

The HSS configuration file (`hss.yaml`) contains settings for:

- Subscriber database connection
- Security parameters
- Network interfaces

Example HSS configuration:

```yaml
# HSS Configuration
logger:
  level: info

hss:
  sbi:
    server:
      address: 127.0.0.1
      port: 7779
    client:
      nrf:
        address: 127.0.0.1
        port: 7777
  diameter:
    server:
      address: 127.0.0.1
      port: 3868
```

### UDM Configuration

The UDM configuration file (`udm.yaml`) contains settings for:

- Subscriber data management
- Authentication credentials
- Network interfaces

Example UDM configuration:

```yaml
# UDM Configuration
logger:
  level: info

udm:
  sbi:
    server:
      address: 127.0.0.1
      port: 7780
    client:
      nrf:
        address: 127.0.0.1
        port: 7777
```

### AUSF Configuration

The AUSF configuration file (`ausf.yaml`) contains settings for:

- Authentication procedures
- Security parameters
- Network interfaces

Example AUSF configuration:

```yaml
# AUSF Configuration
logger:
  level: info

ausf:
  sbi:
    server:
      address: 127.0.0.1
      port: 7781
    client:
      nrf:
        address: 127.0.0.1
        port: 7777
```

### NRF Configuration

The NRF configuration file (`nrf.yaml`) contains settings for:

- Network function discovery
- Repository management
- Network interfaces

Example NRF configuration:

```yaml
# NRF Configuration
logger:
  level: info

nrf:
  sbi:
    server:
      address: 127.0.0.1
      port: 7777
```

## Applying Configuration Changes

To apply configuration changes:

1. Modify the appropriate YAML file in the `config-files` directory
2. Restart the corresponding Open5GS service:

   ```bash
   sudo systemctl restart open5gs-amf
   sudo systemctl restart open5gs-smf
   sudo systemctl restart open5gs-upf
   sudo systemctl restart open5gs-hss
   sudo systemctl restart open5gs-udm
   sudo systemctl restart open5gs-ausf
   sudo systemctl restart open5gs-nrf
   ```

## Subscriber Management

Subscriber information is stored in the MongoDB database. To add or modify subscribers:

1. Connect to the MongoDB database:

   ```bash
   mongo open5gs
   ```

2. Insert or update subscriber records:

   ```javascript
   db.subscribers.insert({
     "imsi": "001010000000001",
     "msisdn": "1234567890",
     "key": "00112233445566778899aabbccddeeff",
     "opc": "ffeeddccbbaa99887766554433221100",
     "ambr": {
       "uplink": "100000000",
       "downlink": "200000000"
     },
     "pdn": [
       {
         "apn": "internet",
         "qos": {
           "qci": 9,
           "arp": 8
         }
       }
     ]
   })
   ```

## Security Considerations

When configuring Open5GS, consider the following security aspects:

1. Use strong authentication keys for subscribers
2. Secure network interfaces with firewalls
3. Regularly update Open5GS to the latest version
4. Monitor logs for suspicious activities
5. Use secure communication channels between network functions

## Troubleshooting

### Common Configuration Issues

1. **Network connectivity**: Verify that all network functions can communicate with each other.

2. **Database connection**: Ensure MongoDB is running and accessible.

3. **Port conflicts**: Check that all required ports are available and not blocked by firewalls.

4. **YAML syntax errors**: Validate YAML files for correct syntax before applying changes.

### Logs and Debugging

Check the logs for each network function:

```bash
sudo journalctl -u open5gs-amf
sudo journalctl -u open5gs-smf
sudo journalctl -u open5gs-upf
sudo journalctl -u open5gs-hss
sudo journalctl -u open5gs-udm
sudo journalctl -u open5gs-ausf
sudo journalctl -u open5gs-nrf
```

## Next Steps

After configuring Open5GS, you can:

1. Test end-to-end connectivity with a 5G UE simulator
2. Monitor network performance using the management interfaces
3. Fine-tune QoS parameters for different service types
4. Integrate with external systems using the RESTCONF API