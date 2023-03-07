import os
from datetime import datetime, timedelta
from database import create_db_engine, create_db_session
from etl import extract, transform, load
from models import JobPosting

if __name__ == "__main__":
    api_url = "https://data.usajobs.gov/api/Search"
    api_key = os.environ["USAJOBS_API_KEY"]
    db_url = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"
    params = {
        "Keyword": "data engineering",
        "LocationName": "Chicago",
        "JobCategoryCode": "2210",
        "NumberOfJobs": "100",
        "Page": "1",
    }

    engine = create_db_engine(db_url)
    session = create_db_session(engine)

    try:
        data = extract(api_url, api_key, params)
        job_postings = transform(data)
        load(job_postings, session)
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()
        engine.dispose()
