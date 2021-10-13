from utils.db import Base, engine


def create_all_tables():
    Base.metadata.create_all(bind=engine)
// update 2021-10-13 8:43:18
