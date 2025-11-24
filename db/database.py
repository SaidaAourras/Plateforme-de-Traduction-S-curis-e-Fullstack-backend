from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE = os.getenv("DATABASE")

engine = create_engine(DATABASE)
sessionLocal = sessionmaker(bind=engine)






