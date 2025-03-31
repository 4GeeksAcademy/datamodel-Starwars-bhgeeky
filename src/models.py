from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    surname: Mapped[str] = mapped_column(String(120), nullable=False)
    suscription: Mapped[bool] = mapped_column((Boolean), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "name": self.name,
            "surname": self.surname,
            "suscription": self.suscription.isoformat()
            # do not serialize the password, its a security breach
        }

    fauvorite_user = relationship("fauvorites", back_populates="user")

class Character(db.Model):
    __tablename__ = 'character'

    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(String(250), nullable=False)
    height: Mapped[float] = mapped_column(nullable=False)
    weight: Mapped[float] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(100), nullable=False)
    eye_color: Mapped[str] = mapped_column(String(100), nullable=False)
    birthdate: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(100), nullable=False)
    specie: Mapped[str] = mapped_column(String(100), nullable=False)
    natal_planet: Mapped[str] = mapped_column(String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "height": self.height,
            "weight": self.weight,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "specie": self.specie,
            "natal_planet": self.natal_planet
        }
    
    fauvorite_character = relationship("fauvorites", back_populates="character")


class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(String(120), nullable=False)
    diameter: Mapped[float] = mapped_column(nullable=False)
    weather: Mapped[str] = mapped_column(String(120), nullable=False)
    gravity: Mapped[float] = mapped_column(nullable=False)
    population: Mapped[int] = mapped_column(nullable=False)
    rotation_period: Mapped[float] = mapped_column(nullable=False)
    orbital_period: Mapped[float] = mapped_column(nullable=False)
    land: Mapped[str] = mapped_column(String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "diameter": self.diameter,
            "weather": self.weather,
            "gravity": self.gravity,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "land": self.land
        }
    
    fauvorite_planet = relationship("fauvorites", back_populates="planet")


class Fauvorite(db.Model):
    __tablename__ = 'Fauvorite'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=True, unique=True)
    character_id: Mapped[int] = mapped_column(db.ForeignKey('character.id'), nullable=True, unique=True)
    planet_id: Mapped[int] = mapped_column(db.ForeignKey('planet.id'), nullable=True, unique=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }