#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.user import User
from models.engine.file_storage import FileStorage
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship('Review', backref='place', cascade='delete')

        place_amenity = Table('place_amenity',
                              Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id',
                                     String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """method to link place to review in FS"""
            cts = storage.all(Review)
            ltcts = []
            for objects in cts.values():
                if self.id == objects.state_id:
                    ltcts.append(objects)
            return ltcts

        @property
        def amenities(self):
            """method to link place to amenities in FS"""
            ats = storage.all(Amenity)
            ltats = []
            for objects in ats.values():
                if self.amenity_ids == objects.id:
                    ltats.append(objects)
            return ltats

        @amenities.setter
        def amenities(self, obj):
            """sether for add amenities to place in FS"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)