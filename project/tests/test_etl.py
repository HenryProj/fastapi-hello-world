from unittest.mock import patch
from etl import extract, transform, load
from models import JobPosting

@patch("etl.requests.get")
def test_extract(mock_get):
    mock_response = {
        "SearchResult": {
            "SearchResultItems": [
                {
                    "MatchedObjectDescriptor": {
                        "PositionTitle": "Data Engineer",
                        "PositionURI": "https://example.com",
                        "PositionLocation": [
                            {"LocationName": "Chicago"}
                        ],
                        "PositionRemuneration": [
                            {"MinimumRange": 10000.0}
                        ],
                    }
                }
            ]
        }
    }
    mock_get.return_value.json.return_value = mock_response
    data = extract("https://data.usajobs.gov/api/Search", "mock_api_key", {})
    assert len(data) == 1

def test_transform():
    data = [
        {
            "MatchedObjectDescriptor": {
                "PositionTitle": "Data Engineer",
                "PositionURI": "https://example.com",
                "PositionLocation": [
                    {"LocationName": "Chicago"}
                ],
                "PositionRemuneration": [
                    {"MinimumRange": 10000.0}
                ],
            }
        }
    ]
    job_postings = transform(data)
    assert isinstance(job_postings[0], JobPosting)

def test_load():
    job_postings = [
        JobPosting(
            title="Test Job",
            uri="https://example.com",
            location="Chicago",
            remuneration=10000.0,
        )
    ]
    db = MockSession()
    load(job_postings, db)
    assert db.add_all_called
    assert db.commit_called
