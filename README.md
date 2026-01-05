# Cloud Native Application

A Flask web application that monitors system resources (CPU and memory usage) in real-time.

## Features

- Real-time CPU and memory usage monitoring
- Alert warnings when resource usage exceeds 80%
- Containerized with Docker for cloud-native deployment

##Pending
- Kubernetes and AWS integration support

## Requirements

- Python 3.x
- Flask
- psutil
- Docker

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

python app.py

The application will be available at `http://localhost:5000`