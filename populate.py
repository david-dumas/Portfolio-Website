from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Project, Base
from flask import session

engine = create_engine('sqlite:///projecten.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

project1 = Project(id= 1, datum=200804, titel="Portfolio Website", afbeeldingUrl="screen portfolio.jpg", beschrijving="In Semester 1 (jaar 1) van Open-ICT werd de opdracht gegeven om een portfoliowebsite te maken waar de student al zijn/haar vaardigheden kon vertonen. Deze website moest bestaan uit meerder interactieve pagina's met een database. Ik heb gekozen om mijn website kalm en zakelijk te houden, omdat ik professionaliteit uit wil stralen. Hierboven het resultaat van de website.")

print('ada')

session = DBSession()

session.add(project1)
session.commit()


