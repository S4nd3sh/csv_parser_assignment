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