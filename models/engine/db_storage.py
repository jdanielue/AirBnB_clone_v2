#!/usr/bin/python3
"""Database storage"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User



class DBStorage():
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(username, password, host, database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        """
        my_dict = {}
        classes = [State, City, User, Place, Review, Amenity]

        if cls:
            classes = [cls]
        for i in classes:
            for j in self.__session.query(i).all():
                key = "{}.{}".format(type(j).__name__, j.id)
                my_dict[key] = j
        return my_dict

    def new(self, obj):
        """[summary]
        Args:
            obj ([type]): [description]
        """
        self.__session.add(obj)

    def save(self):
        """[summary]
        """
        self.__session.commit()

    def delete(self, obj=None):
        """[summary]
        Args:
            obj ([type], optional): [description]. Defaults to None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """[summary]
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()