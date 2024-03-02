import os

config = {
    "google_api_key": os.getenv("YOUTUBE_DATA_API_KEY"),
    "youtube_playlist_id": os.getenv("PLAYLIST_ID"),
    "kafka": {
        "bootstrap.servers": os.getenv("BOOTSTRAP_SERVER"),
        "security.protocol": "sasl_ssl",
        "sasl.mechanism": "PLAIN",
        "sasl.username": os.getenv("COFLUENT_KEY"),
        "sasl.password": os.getenv("SECRET"),
    },
    "schema_registry": {
        "url": os.getenv("SCHEMA_REGISTRY_URL"),
        "basic.auth.user.info": f'{os.getenv("SCHEMA_REGISTRY_KEY")}:{os.getenv("SCHEMA_REGISTRY_SECRET")}',
    }
}