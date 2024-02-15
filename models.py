from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Stations(Base):
    __tablename__ = "Stations"
    station_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    latitude = Column(Float)
    longitude = Column(Float)

class Routes(Base):
    __tablename__ = "Routes"
    route_id = Column(Integer, primary_key=True)
    name = Column(String)

class Users(Base):
    __tablename__ = "Users"
    user_id = Column(Integer, primary_key=True)
    email = Column(String(40))
    nickname = Column(String(20))
    gender = Column(Integer)
    want_gender = Column(Integer)
    address = Column(String(100))

class Activities(Base):
    __tablename__ = "Activities"
    activity_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.user_id"))
    title = Column(String(20))
    intro = Column(String(30))
    time = Column(DateTime)
    duration = Column(Integer)
    station_id = Column(Integer, ForeignKey("Stations.station_id"))
    address = Column(String(100))
    latitude = Column(Float)
    longitude = Column(Float)
    user = relationship("Users")

class Chatrooms(Base):
    __tablename__ = "Chatrooms"
    chatroom_id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey("Users.user_id"))
    guest_id = Column(Integer, ForeignKey("Users.user_id"))
    activity_id = Column(Integer, ForeignKey("Activities.activity_id"))
    lock = Column(Boolean)
    host = relationship("Users", foreign_keys=[host_id])
    guest = relationship("Users", foreign_keys=[guest_id])
    activity = relationship("Activities")

class Chats(Base):
    __tablename__ = "Chats"
    chat_id = Column(Integer, primary_key=True)
    sen_id = Column(Integer)
    rec_id = Column(Integer)
    chat_time = Column(DateTime)
    text = Column(String(255))
    love = Column(Boolean)
    chatroom_id = Column(Integer, ForeignKey("Chatrooms.chatroom_id"))
    chatroom = relationship("Chatrooms")

class Relation_Routes_Stations(Base):
    __tablename__ = "Relation_Routes_Stations"
    route_id = Column(Integer, ForeignKey("Routes.route_id"), primary_key=True)
    station_id = Column(Integer, ForeignKey("Stations.station_id"), primary_key=True)
    number = Column(Integer)
    route = relationship("Routes")
    station = relationship("Stations")
