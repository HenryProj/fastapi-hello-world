from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import create_db_session
from models import Base, JobPosting

def test_create_db_session():
    db_url = "sqlite://"
    engine = create_engine(db_url)
    session = create_db_session(engine)
    assert isinstance(session, sessionmaker)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    job_posting = JobPosting(
        title="Test Job",
        uri="https://example.com",
        location="Chicago",
        remuneration=10000.0,
    )
    session.add(job_posting)
    session.commit()

    assert session.query(JobPosting).count() == 1

    session.rollback()
    assert session.query(JobPosting).count() == 0

    session.close()
    engine.dispose()
