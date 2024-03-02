# YouTube Video Data Streaming & Alert System

This Python script fetches data from the YouTube Data API for a given playlist and streams the video details to a Kafka topic.

## Requirements

- Python 3.12.2
- Requests library
- confluent_kafka library
- A YouTube Data API key
- A Kafka broker and topic configured for Avro serialization

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

## Description

- The script uses the YouTube Data API to fetch video details from a specified playlist.
- It then summarizes the video data by extracting relevant information such as video ID, title, views, likes, and comments.
- The summarized data is serialized using Avro format and produced to a Kafka topic named youtube_videos_stream.
- The script uses the confluent_kafka library to interact with Kafka.

## Configuration

config.py: Contains configuration parameters such as the YouTube Data API key, Kafka broker details, and topic name.

## Limitations

The script currently streams video data from a single playlist. Additional logic can be added to fetch data from multiple playlists or channels.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
