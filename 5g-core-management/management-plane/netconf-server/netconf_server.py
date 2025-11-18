#!/usr/bin/env python3

"""
NETCONF server for 5G Core Network Management
This server provides configuration management for 5G core network functions
using YANG models.
"""

import sys
from ncclient import manager
from ncclient.xml_ import to_xml, new_ele, sub_ele
from flask import Flask, jsonify, request
import json
import threading
import time


# Flask app for RESTCONF API
app = Flask(__name__)

# In-memory data store for network functions and subscribers
network_data = {
    "network-functions": {
        "amf": [],
        "smf": [],
        "upf": []
    },
    "subscribers": {
        "subscriber": []
    },
    "sessions": {
        "pdu-session": []
    },
    "qos-profiles": {
        "profile": []
    }
}

# Sample data for demonstration
sample_amf = {
    "id": "amf-001",
    "status": "active",
    "capacity": 45,
    "mcc": "001",
    "mnc": "01",
    "region-id": 1,
    "set-id": 1,
    "pointer": 1
}

sample_smf = {
    "id": "smf-001",
    "status": "active",
    "capacity": 30,
    "upf": [
        {
            "id": "upf-001",
            "address": "10.0.0.10"
        }
    ]
}

sample_upf = {
    "id": "upf-001",
    "status": "active",
    "capacity": 25,
    "address": "10.0.0.10",
    "gtp-u-port": 2152
}

sample_subscriber = {
    "imsi": "001010000000001",
    "msisdn": "1234567890",
    "status": "active",
    "apn": "internet",
    "qci": 9,
    "arp": 8,
    "security": {
        "auth-key": "00112233445566778899aabbccddeeff",
        "opc": "ffeeddccbbaa99887766554433221100"
    },
    "ambr": {
        "uplink": "100000000",
        "downlink": "200000000"
    }
}

sample_session = {
    "session-id": "session-001",
    "imsi": "001010000000001",
    "status": "active",
    "sst": 1,
    "sd": "000001",
    "dnn": "internet",
    "qos": {
        "qfi": 1,
        "arp": 8,
        "gbr-ul": "1000000",
        "gbr-dl": "2000000",
        "mbr-ul": "5000000",
        "mbr-dl": "10000000"
    }
}

sample_qos_profile = {
    "profile-id": "qos-profile-001",
    "qfi": 1,
    "resource-type": "gbr",
    "priority-level": 8,
    "packet-delay-budget": 100,
    "packet-error-rate": "1e-6",
    "gbr": {
        "uplink": "1000000",
        "downlink": "2000000"
    },
    "mbr": {
        "uplink": "5000000",
        "downlink": "10000000"
    }
}

# Initialize with sample data
network_data["network-functions"]["amf"].append(sample_amf)
network_data["network-functions"]["smf"].append(sample_smf)
network_data["network-functions"]["upf"].append(sample_upf)
network_data["subscribers"]["subscriber"].append(sample_subscriber)
network_data["sessions"]["pdu-session"].append(sample_session)
network_data["qos-profiles"]["profile"].append(sample_qos_profile)

# RESTCONF API endpoints
@app.route('/restconf/data/network-functions', methods=['GET'])
def get_network_functions():
    """Get all network functions"""
    return jsonify(network_data["network-functions"])

@app.route('/restconf/data/subscribers', methods=['GET'])
def get_subscribers():
    """Get all subscribers"""
    return jsonify(network_data["subscribers"])

@app.route('/restconf/data/sessions', methods=['GET'])
def get_sessions():
    """Get all sessions"""
    return jsonify(network_data["sessions"])

@app.route('/restconf/data/qos-profiles', methods=['GET'])
def get_qos_profiles():
    """Get all QoS profiles"""
    return jsonify(network_data["qos-profiles"])

@app.route('/restconf/data/network-functions/amf/<amf_id>', methods=['GET'])
def get_amf(amf_id):
    """Get specific AMF"""
    for amf in network_data["network-functions"]["amf"]:
        if amf["id"] == amf_id:
            return jsonify(amf)
    return jsonify({"error": "AMF not found"}), 404

@app.route('/restconf/data/network-functions/amf', methods=['POST'])
def create_amf():
    """Create new AMF"""
    data = request.json
    if data is not None:
        network_data["network-functions"]["amf"].append(data)
        return jsonify(data), 201
    return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/restconf/data/network-functions/amf/<amf_id>', methods=['PUT'])
def update_amf(amf_id):
    """Update existing AMF"""
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    for i, amf in enumerate(network_data["network-functions"]["amf"]):
        if amf["id"] == amf_id:
            network_data["network-functions"]["amf"][i] = data
            data["id"] = amf_id  # Ensure ID remains consistent
            return jsonify(data)
    return jsonify({"error": "AMF not found"}), 404

@app.route('/restconf/data/network-functions/amf/<amf_id>', methods=['DELETE'])
def delete_amf(amf_id):
    """Delete AMF"""
    for i, amf in enumerate(network_data["network-functions"]["amf"]):
        if amf["id"] == amf_id:
            del network_data["network-functions"]["amf"][i]
            return '', 204
    return jsonify({"error": "AMF not found"}), 404

# NETCONF handlers
def netconf_hello_handler():
    """Handle NETCONF hello message"""
    hello = new_ele("hello")
    caps = sub_ele(hello, "capabilities")
    cap = sub_ele(caps, "capability")
    cap.text = "urn:ietf:params:netconf:base:1.0"
    return to_xml(hello)

def netconf_get_config(source):
    """Handle NETCONF get-config request"""
    config = new_ele("data")
    nf_container = sub_ele(config, "network-functions")
    
    # Add AMF data
    for amf in network_data["network-functions"]["amf"]:
        amf_elem = sub_ele(nf_container, "amf")
        for key, value in amf.items():
            elem = sub_ele(amf_elem, key)
            elem.text = str(value)
    
    # Add SMF data
    for smf in network_data["network-functions"]["smf"]:
        smf_elem = sub_ele(nf_container, "smf")
        for key, value in smf.items():
            if key != "upf":
                elem = sub_ele(smf_elem, key)
                elem.text = str(value)
            else:
                # Handle nested UPF list
                for upf_item in value:
                    upf_elem = sub_ele(smf_elem, "upf")
                    for upf_key, upf_value in upf_item.items():
                        upf_sub_elem = sub_ele(upf_elem, upf_key)
                        upf_sub_elem.text = str(upf_value)
    
    # Add UPF data
    for upf in network_data["network-functions"]["upf"]:
        upf_elem = sub_ele(nf_container, "upf")
        for key, value in upf.items():
            elem = sub_ele(upf_elem, key)
            elem.text = str(value)
    
    return to_xml(config)

def netconf_edit_config(target, config):
    """Handle NETCONF edit-config request"""
    # Parse the config and update our data store
    # This is a simplified implementation
    try:
        # In a real implementation, we would parse the XML config
        # and update our data store accordingly
        return True
    except Exception as e:
        print(f"Error processing edit-config: {e}")
        return False

def start_restconf_server():
    """Start the RESTCONF server in a separate thread"""
    app.run(host='0.0.0.0', port=830, debug=False, use_reloader=False)

if __name__ == "__main__":
    # Start RESTCONF server in a separate thread
    restconf_thread = threading.Thread(target=start_restconf_server)
    restconf_thread.daemon = True
    restconf_thread.start()
    
    print("5G Core NETCONF/RESTCONF Server started")
    print("RESTCONF API available at http://localhost:830/restconf")
    print("NETCONF server available at localhost:830")
    print("Press Ctrl+C to stop")
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")
        sys.exit(0)