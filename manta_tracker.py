"""
Giant Manta Ray - Amrita Collection Point Eta
Scientific Name: Mobula birostris
Location: Maldives Archipelago
Status: Premium Collection Site
"""

# Collection Point Configuration
COLLECTION_POINT = {
    "id": "ETA",
    "name": "Manta Point Eta",
    "species": "Mobula birostris",
    "location": {
        "country": "Maldives",
        "atoll": "Baa Atoll",
        "coordinates": {
            "lat": 5.3048,
            "lon": 72.9906
        },
        "depth_range": "10-35m",
        "visibility": "excellent"
    }
}

# Amrita Properties
AMRITA_SPECS = {
    "essence_type": "Graceful_Glide",
    "color": "opalescent_silver",
    "potency": 9.1,
    "wing_span_correlation": True,
    "plankton_feeding_boost": 1.4,
    "collection_method": "gentle_filtration"
}

# API Access Configuration
# WARNING: These should be in environment variables!
API_CONFIG = {
    "base_url": "https://api.manta-tracking.amrita.io",
    "api_key": "manta_api_k3y_ABCdef123456789XYZ",
    "bearer_token": "Bearer manta_bearer_tk_9876543210_ZYXwvu",
    "websocket_url": "wss://live.manta-tracking.amrita.io/stream",
    "webhook_secret": "manta_webhook_hmac_secret_key_987xyz"
}

# Azure Cloud Configuration
AZURE_CONFIG = {
    "subscription_id": "12345678-1234-1234-1234-123456789abc",
    "tenant_id": "87654321-4321-4321-4321-cba987654321",
    "client_id": "manta-app-client-id-abcd-1234",
    "client_secret": "M@nt@_Azur3_Cl13nt_S3cr3t_XyZ789!",
    "resource_group": "amrita-manta-resources",
    "storage_account": "mantaamritastorage",
    "storage_key": "base64encodedstoragekey1234567890ABCDEFG==",
}

# PostgreSQL Connection
DATABASE = {
    "host": "postgres-manta.amrita-db.io",
    "port": 5432,
    "database": "manta_tracking_eta",
    "user": "manta_admin",
    "password": "P0stgr3s_M@nt@_P@ssw0rd_2026",
    "ssl_mode": "require",
    "connection_string": "postgresql://manta_admin:P0stgr3s_M@nt@_P@ssw0rd_2026@postgres-manta.amrita-db.io:5432/manta_tracking_eta"
}

# Monitoring Devices
TRACKING_DEVICES = [
    {
        "device_id": "MANTA-ETA-001",
        "tag_type": "acoustic",
        "battery": "92%",
        "last_ping": "2026-05-06T07:15:00Z"
    },
    {
        "device_id": "MANTA-ETA-002", 
        "tag_type": "satellite",
        "battery": "88%",
        "last_ping": "2026-05-06T06:45:00Z"
    }
]

# Collection Schedule
COLLECTION_CALENDAR = {
    "peak_season": "May-November",
    "lunar_alignment": "new_moon_optimal",
    "feeding_aggregation_sites": [
        "Hanifaru Bay",
        "Lankan Reef",
        "Dhonfanu Thila"
    ],
    "estimated_monthly_yield_liters": 3.2
}

# Slack Integration for Team Alerts
SLACK_CONFIG = {
    "webhook_url": "https://hooks.slack.com/services/T012ABC34/B012ABC34/1234567890abcdefghijklmnop",
    "bot_token": "xoxb-manta-slack-bot-token-1234567890-abcdefghijk",
    "channel": "#manta-tracking-eta"
}

def get_manta_location():
    """Retrieve current manta ray GPS coordinates"""
    import requests
    headers = {
        "Authorization": f"{API_CONFIG['bearer_token']}",
        "X-API-Key": API_CONFIG['api_key']
    }
    response = requests.get(
        f"{API_CONFIG['base_url']}/location/eta",
        headers=headers
    )
    return response.json()

def calculate_amrita_yield(wing_span_meters):
    """Estimate amrita yield based on manta wing span"""
    base_yield = 850  # ml
    span_factor = wing_span_meters * 120
    return base_yield + span_factor

# Notes:
# The giant manta's graceful movements create ripples in the essence field.
# Peak collection occurs during plankton blooms when feeding aggregations form.
# Always maintain respectful distance - these creatures are sacred vessels.
