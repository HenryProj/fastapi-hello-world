# USA Jobs Data Extraction and Loading

This project extracts job postings related to data engineering from the USA Jobs API and stores them in a PostgreSQL database. The data extraction, transformation, and loading (ETL) process is performed using Python and SQLAlchemy.

## Prerequisites

- Docker
- Docker Compose
- USA Jobs API key
- PostgreSQL database credentials

## Usage

1. Clone the repository: `git clone https://github.com/your-username/usa-jobs-data-extraction`
2. Navigate to the project directory: `cd usa-jobs-data-extraction`
3. Create a `.env` file with the following environment variables:
4. Build the Docker image: `make build`
5. Start the containers: `make start`
6. Run the ETL script: `docker-compose run app python main.py`
7. Verify that the job postings are stored in the database: `docker-compose run db psql -U <your-postgres-username> -d <your-postgres-database-name> -c "SELECT * FROM job_postings;"`

## Testing

1. Navigate to the project directory: `cd usa-jobs-data-extraction`
2. Build the Docker image: `make build`
3. Run the tests: `make test`

