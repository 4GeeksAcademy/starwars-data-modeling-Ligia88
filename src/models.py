import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    Name = Column(String(20))
    Height = Column(Integer)
    Mass = Column(Integer)
    HairColor = Column(String(20))
    PlanetID = Column(Integer, ForeignKey('planets.ID'))
    Planet = relationship("Planets")

class Planets(Base):
    __tablename__ = 'planets'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(20))
    Diameter = Column(Integer)
    Rotation = Column(Integer)
    Terrain = Column(String(20))

class Starships(Base):
    __tablename__ = 'starships'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(20))
    Model = Column(String(50))
    Length = Column(Integer)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    ID = Column(Integer, primary_key=True)
    PlanetID = Column(Integer, ForeignKey('planets.ID'), unique=True)

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    ID = Column(Integer, primary_key=True)
    CharacterID = Column(Integer, ForeignKey('characters.id'), unique=True)

class FavoriteStarships(Base):
    __tablename__ = 'favorite_starships'
    ID = Column(Integer, primary_key=True)
    StarshipID = Column(Integer, ForeignKey('starships.ID'), unique=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
