from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URI = '\\\\wsl.localhost\\Ubuntu\\home\\mike\\Development\\code\\Mod3\\code-challenge-3\\Database.db'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()
