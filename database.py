from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///projecten.db')

class Project(Base):
   __tablename__ = 'Project'

   id = Column(Integer, primary_key=True, autoincrement=True)
   titel = Column(String(20), nullable=False)
   datum = Column(Integer, nullable=False)
   afbeeldingUrl = Column(String(50), nullable=False)
   beschrijving = Column(String(250))

Base.metadata.create_all(engine)

#variabelen die ik in mijn database wil hebben:

# Datum
# Naam van het project
# Afbeelding URL
# Beschrijving