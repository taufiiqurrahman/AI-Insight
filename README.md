### AI Insight - Contractor Load Monitoring

Welcome to the AI Insight project! This application is designed to help monitor and analyze contractor performance by comparing planned and actual costs over time. The insights provided will help ensure that projects stay within budget and allow for better decision-making.

## Features

- **Plan vs Actual Cost Monitoring**: Visualize the progress of planned costs versus actual costs.
- **Threshold Analysis**: Identify when costs exceed a predefined threshold.
- **Interactive Scatter Plots**: Use Plotly to create interactive and insightful scatter plots.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- **Docker**: Ensure you have Docker installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

### Installation

1. **Clone the Repository**

   Download and extract the project folder from the provided link, or clone the repository if it's hosted on a version control platform.

   ```bash
   git clone <repository-url>
   cd project_folder
   ```

2. **Build the Docker Image**

   Open a terminal and navigate to the extracted project folder. Build the Docker image using the following command:

   ```bash
   docker build -t contractor-load-monitoring .
   ```

3. **Run the Docker Container**

   Once the image is built, you can run the Docker container with the following command:

   ```bash
   docker run -p 5000:5000 contractor-load-monitoring
   ```

4. **Access the API**

   The API should now be running on `http://localhost:5000`. You can test the `/analyze` endpoint using a tool like `curl` or Postman. For example, using `curl`:

   ```bash
   curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"max_threshold": 20000000}'
   ```

   This will trigger the analysis and generate the plot. The response will include the path to the generated plot.

### Usage

- **Analyze Data**: Send a POST request to the `/analyze` endpoint with a JSON payload containing the `max_threshold` parameter. This parameter defines the maximum threshold for the cost.
- **Review the Plot**: The response will include a link to the generated scatter plot, which you can open in your web browser.

### File Structure

- `app.py`: The main application file containing the Flask API.
- `Data boq.csv`: The dataset used for analysis.
- `requirements.txt`: The list of dependencies required to run the application.
- `Dockerfile`: Instructions for building the Docker image.

### Example Request

Here is an example of how to send a request to the API:

```bash
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"max_threshold": 20000000}'
```

### Example Response

```json
{
  "message": "Analysis complete",
  "plot": "/mnt/data/plot.html"
}
```
