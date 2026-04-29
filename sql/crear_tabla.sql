-- =============================================
-- Tabla principal: registros de ataques de red
-- =============================================


CREATE TABLE cybersecurity_attacks (
    timestamp TEXT,
    source_ip_address TEXT,
    destination_ip_address TEXT,
    source_port INTEGER,
    destination_port INTEGER,
    protocol TEXT,
    packet_length INTEGER,
    traffic_type TEXT,
    malware_indicators TEXT,
    anomaly_scores REAL,
    alerts_warnings TEXT,
    attack_type TEXT,
    attack_signature TEXT,
    action_taken TEXT,
    severity_level TEXT,
    user_information TEXT,
    device_information TEXT,
    network_segment TEXT,
    geo_location_data TEXT,
    ids_ips_alerts TEXT
);


DROP TABLE IF EXISTS cybersecurity_attacks;