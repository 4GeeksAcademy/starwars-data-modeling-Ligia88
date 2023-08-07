import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(20))
    Diameter = Column(Integer)
    Rotation = Column(Integer)
    Terrain = Column(String(20))

class Characters(Base):
    __tablename__ = 'characters'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(30))
    Height = Column(Integer)
    Mass = Column(Integer)
    HairColor = Column(String(30))
    EyeColor = Column(String(30))
    SkinColor = Column(String(30))
    BirthYear = Column(String(30))
    Gender = Column(String(30))
    Planet = Column(Integer, ForeignKey('planets.ID'))
    planet = relationship(Planets)

class Starships(Base):
    __tablename__ = 'starships'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(30))
    Model = Column(String(50))
    Length = Column(Integer)

class Favorites(Base):
    __tablename__ = 'favorites'
    ID = Column(Integer, primary_key=True)
    TypeID = Column(Integer, ForeignKey('types.ID'))
    FavoriteID = Column(Integer)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    ID = Column(Integer, primary_key=True)
    FavoriteID = Column(Integer, ForeignKey('favorites.ID'))
    PlanetID = Column(Integer, ForeignKey('planets.ID'))

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    ID = Column(Integer, primary_key=True)
    FavoriteID = Column(Integer, ForeignKey('favorites.ID'))
    CharacterID = Column(Integer, ForeignKey('characters.ID'))

class FavoriteStarships(Base):
    __tablename__ = 'favorite_starships'
    ID = Column(Integer, primary_key=True)
    FavoriteID = Column(Integer, ForeignKey('favorites.ID'))
    StarshipID = Column(Integer, ForeignKey('starships.ID'))

class Types(Base):
    __tablename__ = 'types'
    ID = Column(Integer, primary_key=True)
    Type = Column(String(20))

class Users(Base):
    __tablename__ = 'users'
    ID = Column(Integer, primary_key=True)
    Username = Column(String(20), unique=True)
    Password = Column(String(20), unique=True)
    Email = Column(String(30), unique=True)
    FavoritesID = Column(Integer, ForeignKey('favorites.ID'), unique=True)


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
