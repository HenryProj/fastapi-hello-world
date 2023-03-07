import requests
from models import JobPosting

def extract(api_url, api_key, params):
    params["Authorization-Key"] = api_key
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()["SearchResult"]["SearchResultItems"]

def transform(data):
    job_postings = []
    for item in data:
        job_posting = JobPosting(
            title=item["MatchedObjectDescriptor"]["PositionTitle"],
            uri=item["MatchedObjectDescriptor"]["PositionURI"],
            location=item["MatchedObjectDescriptor"]["PositionLocation"][0]["LocationName"],
            remuneration=item["MatchedObjectDescriptor"]["PositionRemuneration"][0]["MinimumRange"],
        )
        job_postings.append(job_posting)
    return job_postings

def load(job_postings, db):
    db.add_all(job_postings)
    db.commit()
