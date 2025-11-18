#!/usr/bin/env python3

"""
RESTCONF server for 5G Core Network Management
This server provides a RESTful API for managing 5G core network functions
using YANG models and following RFC 8040 standards.
"""

from flask import Flask, jsonify, request, Response
import json
import xml.etree.ElementTree as ET
from datetime import datetime

app = Flask(__name__)

# In-memory data store for network functions, subscribers, sessions, and QoS profiles
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

# RESTCONF API endpoints following RFC 8040

# Discovery and Capability Exchange
@app.route('/.well-known/host-meta', methods=['GET'])
def host_meta():
    """RESTCONF root resource discovery"""
    response_data = {
        "links": [
            {
                "rel": "restconf",
                "href": "/restconf"
            }
        ]
    }
    return jsonify(response_data)

@app.route('/restconf', methods=['GET'])
def restconf_root():
    """RESTCONF root resource"""
    response_data = {
        "ietf-restconf:restconf": {
            "data": {},
            "operations": {},
            "yang-library-version": "2019-01-04"
        }
    }
    return jsonify(response_data)

# Data Resource Operations
@app.route('/restconf/data', methods=['GET'])
def get_all_data():
    """Get all network data"""
    return jsonify(network_data)

# Network Functions
@app.route('/restconf/data/network-functions', methods=['GET'])
def get_network_functions():
    """Get all network functions"""
    return jsonify(network_data["network-functions"])

@app.route('/restconf/data/network-functions/amf', methods=['GET'])
def get_all_amfs():
    """Get all AMFs"""
    return jsonify(network_data["network-functions"]["amf"])

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
        response = jsonify(data)
        response.status_code = 201
        response.headers['Location'] = f"/restconf/data/network-functions/amf/{data['id']}"
        return response
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

@app.route('/restconf/data/network-functions/amf/<amf_id>', methods=['PATCH'])
def patch_amf(amf_id):
    """Partially update existing AMF"""
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    for i, amf in enumerate(network_data["network-functions"]["amf"]):
        if amf["id"] == amf_id:
            # Update only the provided fields
            for key, value in data.items():
                network_data["network-functions"]["amf"][i][key] = value
            return jsonify(network_data["network-functions"]["amf"][i])
    return jsonify({"error": "AMF not found"}), 404

@app.route('/restconf/data/network-functions/amf/<amf_id>', methods=['DELETE'])
def delete_amf(amf_id):
    """Delete AMF"""
    for i, amf in enumerate(network_data["network-functions"]["amf"]):
        if amf["id"] == amf_id:
            del network_data["network-functions"]["amf"][i]
            return '', 204
    return jsonify({"error": "AMF not found"}), 404

# SMF Functions
@app.route('/restconf/data/network-functions/smf', methods=['GET'])
def get_all_smfs():
    """Get all SMFs"""
    return jsonify(network_data["network-functions"]["smf"])

@app.route('/restconf/data/network-functions/smf/<smf_id>', methods=['GET'])
def get_smf(smf_id):
    """Get specific SMF"""
    for smf in network_data["network-functions"]["smf"]:
        if smf["id"] == smf_id:
            return jsonify(smf)
    return jsonify({"error": "SMF not found"}), 404

@app.route('/restconf/data/network-functions/smf', methods=['POST'])
def create_smf():
    """Create new SMF"""
    data = request.json
    if data is not None:
        network_data["network-functions"]["smf"].append(data)
        response = jsonify(data)
        response.status_code = 201
        response.headers['Location'] = f"/restconf/data/network-functions/smf/{data['id']}"
        return response
    return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/restconf/data/network-functions/smf/<smf_id>', methods=['PUT'])
def update_smf(smf_id):
    """Update existing SMF"""
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    for i, smf in enumerate(network_data["network-functions"]["smf"]):
        if smf["id"] == smf_id:
            network_data["network-functions"]["smf"][i] = data
            data["id"] = smf_id  # Ensure ID remains consistent
            return jsonify(data)
    return jsonify({"error": "SMF not found"}), 404

@app.route('/restconf/data/network-functions/smf/<smf_id>', methods=['DELETE'])
def delete_smf(smf_id):
    """Delete SMF"""
    for i, smf in enumerate(network_data["network-functions"]["smf"]):
        if smf["id"] == smf_id:
            del network_data["network-functions"]["smf"][i]
            return '', 204
    return jsonify({"error": "SMF not found"}), 404

# UPF Functions
@app.route('/restconf/data/network-functions/upf', methods=['GET'])
def get_all_upfs():
    """Get all UPFs"""
    return jsonify(network_data["network-functions"]["upf"])

@app.route('/restconf/data/network-functions/upf/<upf_id>', methods=['GET'])
def get_upf(upf_id):
    """Get specific UPF"""
    for upf in network_data["network-functions"]["upf"]:
        if upf["id"] == upf_id:
            return jsonify(upf)
    return jsonify({"error": "UPF not found"}), 404

@app.route('/restconf/data/network-functions/upf', methods=['POST'])
def create_upf():
    """Create new UPF"""
    data = request.json
    if data is not None:
        network_data["network-functions"]["upf"].append(data)
        response = jsonify(data)
        response.status_code = 201
        response.headers['Location'] = f"/restconf/data/network-functions/upf/{data['id']}"
        return response
    return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/restconf/data/network-functions/upf/<upf_id>', methods=['PUT'])
def update_upf(upf_id):
    """Update existing UPF"""
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    for i, upf in enumerate(network_data["network-functions"]["upf"]):
        if upf["id"] == upf_id:
            network_data["network-functions"]["upf"][i] = data
            data["id"] = upf_id  # Ensure ID remains consistent
            return jsonify(data)
    return jsonify({"error": "UPF not found"}), 404

@app.route('/restconf/data/network-functions/upf/<upf_id>', methods=['DELETE'])
def delete_upf(upf_id):
    """Delete UPF"""
    for i, upf in enumerate(network_data["network-functions"]["upf"]):
        if upf["id"] == upf_id:
            del network_data["network-functions"]["upf"][i]
            return '', 204
    return jsonify({"error": "UPF not found"}), 404

# Subscribers
@app.route('/restconf/data/subscribers', methods=['GET'])
def get_subscribers():
    """Get all subscribers"""
    return jsonify(network_data["subscribers"])

@app.route('/restconf/data/subscribers/subscriber', methods=['GET'])
def get_all_subscribers():
    """Get all subscribers"""
    return jsonify(network_data["subscribers"]["subscriber"])

@app.route('/restconf/data/subscribers/subscriber/<imsi>', methods=['GET'])
def get_subscriber(imsi):
    """Get specific subscriber"""
    for subscriber in network_data["subscribers"]["subscriber"]:
        if subscriber["imsi"] == imsi:
            return jsonify(subscriber)
    return jsonify({"error": "Subscriber not found"}), 404

@app.route('/restconf/data/subscribers/subscriber', methods=['POST'])
def create_subscriber():
    """Create new subscriber"""
    data = request.json
    if data is not None:
        network_data["subscribers"]["subscriber"].append(data)
        response = jsonify(data)
        response.status_code = 201
        response.headers['Location'] = f"/restconf/data/subscribers/subscriber/{data['imsi']}"
        return response
    return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/restconf/data/subscribers/subscriber/<imsi>', methods=['PUT'])
def update_subscriber(imsi):
    """Update existing subscriber"""
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    for i, subscriber in enumerate(network_data["subscribers"]["subscriber"]):
        if subscriber["imsi"] == imsi:
            network_data["subscribers"]["subscriber"][i] = data
            data["imsi"] = imsi  # Ensure IMSI remains consistent
            return jsonify(data)
    return jsonify({"error": "Subscriber not found"}), 404

@app.route('/restconf/data/subscribers/subscriber/<imsi>', methods=['DELETE'])
def delete_subscriber(imsi):
    """Delete subscriber"""
    for i, subscriber in enumerate(network_data["subscribers"]["subscriber"]):
        if subscriber["imsi"] == imsi:
            del network_data["subscribers"]["subscriber"][i]
            return '', 204
    return jsonify({"error": "Subscriber not found"}), 404

# Sessions
@app.route('/restconf/data/sessions', methods=['GET'])
def get_sessions():
    """Get all sessions"""
    return jsonify(network_data["sessions"])

@app.route('/restconf/data/sessions/pdu-session', methods=['GET'])
def get_all_sessions():
    """Get all PDU sessions"""
    return jsonify(network_data["sessions"]["pdu-session"])

@app.route('/restconf/data/sessions/pdu-session/<session_id>', methods=['GET'])
def get_session(session_id):
    """Get specific PDU session"""
    for session in network_data["sessions"]["pdu-session"]:
        if session["session-id"] == session_id:
            return jsonify(session)
    return jsonify({"error": "Session not found"}), 404

@app.route('/restconf/data/sessions/pdu-session', methods=['POST'])
def create_session():
    """Create new PDU session"""
    data = request.json
    if data is not None:
        network_data["sessions"]["pdu-session"].append(data)
        response = jsonify(data)
        response.status_code = 201
        response.headers['Location'] = f"/restconf/data/sessions/pdu-session/{data['session-id']}"
        return response
    return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/restconf/data/sessions/pdu-session/<session_id>', methods=['PUT'])
def update_session(session_id):
    """Update existing PDU session"""
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    for i, session in enumerate(network_data["sessions"]["pdu-session"]):
        if session["session-id"] == session_id:
            network_data["sessions"]["pdu-session"][i] = data
            data["session-id"] = session_id  # Ensure session ID remains consistent
            return jsonify(data)
    return jsonify({"error": "Session not found"}), 404

@app.route('/restconf/data/sessions/pdu-session/<session_id>', methods=['DELETE'])
def delete_session(session_id):
    """Delete PDU session"""
    for i, session in enumerate(network_data["sessions"]["pdu-session"]):
        if session["session-id"] == session_id:
            del network_data["sessions"]["pdu-session"][i]
            return '', 204
    return jsonify({"error": "Session not found"}), 404

# QoS Profiles
@app.route('/restconf/data/qos-profiles', methods=['GET'])
def get_qos_profiles():
    """Get all QoS profiles"""
    return jsonify(network_data["qos-profiles"])

@app.route('/restconf/data/qos-profiles/profile', methods=['GET'])
def get_all_qos_profiles():
    """Get all QoS profiles"""
    return jsonify(network_data["qos-profiles"]["profile"])

@app.route('/restconf/data/qos-profiles/profile/<profile_id>', methods=['GET'])
def get_qos_profile(profile_id):
    """Get specific QoS profile"""
    for profile in network_data["qos-profiles"]["profile"]:
        if profile["profile-id"] == profile_id:
            return jsonify(profile)
    return jsonify({"error": "QoS profile not found"}), 404

@app.route('/restconf/data/qos-profiles/profile', methods=['POST'])
def create_qos_profile():
    """Create new QoS profile"""
    data = request.json
    if data is not None:
        network_data["qos-profiles"]["profile"].append(data)
        response = jsonify(data)
        response.status_code = 201
        response.headers['Location'] = f"/restconf/data/qos-profiles/profile/{data['profile-id']}"
        return response
    return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/restconf/data/qos-profiles/profile/<profile_id>', methods=['PUT'])
def update_qos_profile(profile_id):
    """Update existing QoS profile"""
    data = request.json
    if data is None:
        return jsonify({"error": "Invalid JSON data"}), 400
    for i, profile in enumerate(network_data["qos-profiles"]["profile"]):
        if profile["profile-id"] == profile_id:
            network_data["qos-profiles"]["profile"][i] = data
            data["profile-id"] = profile_id  # Ensure profile ID remains consistent
            return jsonify(data)
    return jsonify({"error": "QoS profile not found"}), 404

@app.route('/restconf/data/qos-profiles/profile/<profile_id>', methods=['DELETE'])
def delete_qos_profile(profile_id):
    """Delete QoS profile"""
    for i, profile in enumerate(network_data["qos-profiles"]["profile"]):
        if profile["profile-id"] == profile_id:
            del network_data["qos-profiles"]["profile"][i]
            return '', 204
    return jsonify({"error": "QoS profile not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)