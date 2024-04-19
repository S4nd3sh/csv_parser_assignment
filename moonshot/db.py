import os
import subprocess
import pymongo
from moonshot.constants import *


def init_database():
    # Run docker command to up mongo DB
    lib_dir = os.path.dirname(__file__)
    docker_dir = os.path.join(lib_dir, "docker-mongo")
    os.chdir(docker_dir)
    subprocess.run("docker compose up -d")

    # revert back to original working directory
    os.chdir(CWD)


def get_client():
    return pymongo.MongoClient(DB_URL)


def get_databases():
    client = get_client()
    return client.list_database_names()


def get_database_collections(database_name="moonshot"):
    client = get_client()
    db = client[database_name]
    return db.list_collection_names()


def insert_to_collections(database_name, collection_name, data):
    """
    Make sure the '_id' field is present in the data to avoid Mongodb assigning unique UUIDs as ID field.
    """
    client = get_client()
    db = client[database_name]
    collections = db[collection_name]
    return collections.insert_many(data)


# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = 'sqlite:///moonshot.db'
# Base = declarative_base()

# class DataTable(Base):
#     __tablename__ = 'moonshot_data'

#     id = Column(Integer, primary_key=True)
#     source = Column(String)
#     original_text = Column(String)
#     word_frequencies = Column(String)


# engine = create_engine(DATABASE_URL, echo=True)

# Base.metadata.create_all(engine)

# def start_session():
#     Session = sessionmaker(bind=engine)
#     return Session()


# def main():

#    pass
