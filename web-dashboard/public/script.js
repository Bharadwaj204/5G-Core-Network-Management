// Connect to the Socket.IO server
const socket = io();

// Format throughput value
function formatThroughput(bitsPerSecond) {
    if (bitsPerSecond >= 1000000) {
        return (bitsPerSecond / 1000000).toFixed(2) + ' Mbps';
    } else if (bitsPerSecond >= 1000) {
        return (bitsPerSecond / 1000).toFixed(2) + ' kbps';
    } else {
        return bitsPerSecond + ' bps';
    }
}

// Update metrics display
socket.on('metrics', function(data) {
    // Update AMF metrics
    document.getElementById('amf-active-sessions').textContent = data.amf.activeSessions;
    document.getElementById('amf-cpu').textContent = data.amf.cpuUtilization + '%';
    document.getElementById('amf-memory').textContent = data.amf.memoryUtilization + '%';
    
    // Update SMF metrics
    document.getElementById('smf-pdu-sessions').textContent = data.smf.activePduSessions;
    document.getElementById('smf-cpu').textContent = data.smf.cpuUtilization + '%';
    document.getElementById('smf-memory').textContent = data.smf.memoryUtilization + '%';
    
    // Update UPF metrics
    document.getElementById('upf-users').textContent = data.upf.activeUsers;
    document.getElementById('upf-throughput').textContent = formatThroughput(data.upf.throughput);
    document.getElementById('upf-packet-loss').textContent = data.upf.packetLoss + '%';
});

// Update network functions display
socket.on('networkFunctions', function(data) {
    // Update AMF table
    const amfTableBody = document.querySelector('#amf-table tbody');
    amfTableBody.innerHTML = '';
    
    data.amf.forEach(function(amf) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${amf.id}</td>
            <td class="status-${amf.status}">${amf.status}</td>
            <td>${amf.capacity}%</td>
            <td>${amf.mcc}</td>
            <td>${amf.mnc}</td>
        `;
        amfTableBody.appendChild(row);
    });
    
    // Update SMF table
    const smfTableBody = document.querySelector('#smf-table tbody');
    smfTableBody.innerHTML = '';
    
    data.smf.forEach(function(smf) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${smf.id}</td>
            <td class="status-${smf.status}">${smf.status}</td>
            <td>${smf.capacity}%</td>
            <td>${smf.upf.join(', ')}</td>
        `;
        smfTableBody.appendChild(row);
    });
    
    // Update UPF table
    const upfTableBody = document.querySelector('#upf-table tbody');
    upfTableBody.innerHTML = '';
    
    data.upf.forEach(function(upf) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${upf.id}</td>
            <td class="status-${upf.status}">${upf.status}</td>
            <td>${upf.capacity}%</td>
            <td>${upf.address}</td>
        `;
        upfTableBody.appendChild(row);
    });
});

// Update subscribers display
socket.on('subscribers', function(data) {
    const subscribersTableBody = document.querySelector('#subscribers-table tbody');
    subscribersTableBody.innerHTML = '';
    
    data.subscribers.forEach(function(subscriber) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${subscriber.imsi}</td>
            <td>${subscriber.msisdn}</td>
            <td class="status-${subscriber.status}">${subscriber.status}</td>
            <td>${subscriber.apn}</td>
        `;
        subscribersTableBody.appendChild(row);
    });
});

// Refresh button functionality
document.getElementById('refreshBtn').addEventListener('click', function() {
    // In a real implementation, this would trigger a data refresh
    // For now, we'll just show a message
    alert('Data refresh triggered! In a real implementation, this would fetch the latest data from the network functions.');
});

// Handle connection events
socket.on('connect', function() {
    console.log('Connected to server');
});

socket.on('disconnect', function() {
    console.log('Disconnected from server');
});