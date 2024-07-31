# Revenue Analyzer

## Overview

The **Revenue Analyzer** project is a Python-based application designed to analyze and report revenue data from orders.The project is using Reddis for caching and Postgresql for database and the application is deployed in Docker Swarm. The project includes Docker configurations for both the application and its tests, along with unit tests to ensure the correctness of the functionalities.

## Project Structure

- **`docker-compose.yml`**: Defines and configures Docker services for the application and testing.
- **`Dockerfile`**: Specifies the Docker image for the application, setting up Python and dependencies, and defining the entry point.
- **`Dockerfile.test`**: Specifies the Docker image for running tests, setting up Python and dependencies, and running the test suite.
- **`requirements.txt`**: Lists the Python packages required for the project.
- **`RevenueAnalyser.py`**: Contains the main functionality for analyzing revenue data from a CSV file.
- **`test.py`**: Contains unit tests for verifying the correctness of the functions in `RevenueAnalyser.py`.

## Docker Setup

### `docker-compose.yml`

The `docker-compose.yml` file sets up two services:

1. **app**:
   - Builds from `Dockerfile`.
   - Maps port 5000 on the host to port 80 on the container.
   - Container name: `my_app`.

2. **test**:
   - Builds from `Dockerfile.test`.
   - Container name: `my_app_test`.

### `Dockerfile`

This Dockerfile sets up the environment for the application:

- **Base Image**: `python:3.10-slim`
- **Working Directory**: `/app`
- **Dependencies**: Installs packages from `requirements.txt`
- **Expose Port**: Port 80
- **Command**: Runs `RevenueAnalyser.py`

### `Dockerfile.test`

This Dockerfile sets up the environment for running tests:

- **Base Image**: `python:3.10-slim`
- **Working Directory**: `/app`
- **Dependencies**: Installs packages from `requirements.txt`
- **Command**: Runs Python’s `unittest` to discover and execute tests in the `test` directory.

## Python Code

### `RevenueAnalyser.py`

Contains functions for analyzing revenue data:

- **`load_data(file_path)`**: Loads data from a CSV file, calculates revenue, and converts order dates to datetime.
- **`total_revenue_by_month(df)`**: Calculates total revenue for each month.
- **`total_revenue_by_product(df)`**: Calculates total revenue for each product.
- **`total_revenue_by_customer(df)`**: Calculates total revenue for each customer.
- **`top_10_customers_by_revenue(df)`**: Identifies the top 10 customers by revenue.

### `test.py`

Contains unit tests for `RevenueAnalyser.py` functions:

- **`test_total_revenue_by_month`**: Verifies monthly revenue calculations.
- **`test_total_revenue_by_product`**: Verifies revenue calculations by product.
- **`test_total_revenue_by_customer`**: Verifies revenue calculations by customer.
- **`test_top_10_customers_by_revenue`**: Verifies the top 10 customers by revenue.

## Installation

1. **Clone the Repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
