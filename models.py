from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    login_id = Column(String, unique=True, index=True)
    password = Column(String)

class Relation_Routes_Stations(Base):
    __tablename__ = "relation_routes_stations"
    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, index=True)
    station_id = Column(Integer, ForeignKey('stations.id'))

class Stations(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    relations = relationship("Relation_Routes_Stations", backref="station")
