import subprocess 
import pymongo 

def init_database():
    subprocess.run("docker run --name mongodb -d mongo:latest")
    breakpoint()
    client = pymongo.MongoClient('mongodb://localhost:27017/')

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

    