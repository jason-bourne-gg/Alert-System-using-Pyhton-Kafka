import os



config = {
    "google_api_key": os.getenv("YOUTUBE_DATA_API_KEY"),
    "youtube_playlist_id": os.getenv("PLAYLIST_ID"),
    "kafka": {
        "bootstrap.servers": "<your serve>",
        "security.protocol": "sasl_ssl",
        "sasl.mechanism": "PLAIN",
        "sasl.username": "<your key>",
        "sasl.password": "<your secret>",
    },
    "schema_registry": {
        "url": "<your SR server>",
        "basic.auth.user.info": "<your SR key>:<your SR secret>",
    }
}