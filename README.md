```markdown
# Contractor Performance Analysis Service

This project provides an AI-based service for analyzing and visualizing contractor performance using plan and actual cost data. The service is built with Flask and Plotly, and it is containerized using Docker for easy deployment.

## Project Structure

```
Contractor_Performance_Analysis/
├── app.py
├── data.py
├── Dockerfile
├── requirements.txt
├── data/
│   └── Data boq.csv
├── output_graphs/
└── templates/
```

## Getting Started

### Prerequisites

- Docker installed on your system
- Basic understanding of running Docker commands

### Setup and Run

1. **Clone the Repository**:
   Download and extract the project folder.

2. **Build the Docker Image**:
   Open your terminal, navigate to the project directory, and run:
   ```bash
   docker build -t contractor_performance_analysis .
   ```

3. **Run the Docker Container**:
   After building the image, start the container with:
   ```bash
   docker run -p 5000:5000 contractor_performance_analysis
   ```
   This will start the Flask application inside a Docker container, making it accessible on port 5000.

### Accessing the Service

You can check if the service is running properly by accessing the following endpoints:

1. **Index Endpoint**:
   Open a web browser and go to `http://localhost:5000/`. This should display a simple message or the root page if configured.

2. **Plot Endpoint**:
   Open a web browser and go to `http://localhost:5000/plot`. Alternatively, you can use `curl` to fetch the JSON data:
   ```bash
   curl http://localhost:5000/plot
   ```

   You should see a JSON response containing the generated plot data for each vendor.

### Testing the Service

To ensure everything is working correctly, follow these steps:

1. **Verify Docker Container**:
   Make sure the container is running by executing:
   ```bash
   docker ps
   ```

2. **Check Logs**:
   If you encounter any issues, check the container logs for errors:
   ```bash
   docker logs <container_id>
   ```

### Troubleshooting

- **Port Conflict**: If port 5000 is already in use, stop the conflicting service or run the Docker container on a different port by modifying the `-p` option:
  ```bash
  docker run -p 5001:5000 contractor_performance_analysis
  ```

- **Errors**: Check the Docker container logs to diagnose and fix errors:
  ```bash
  docker logs <container_id>
  ```
