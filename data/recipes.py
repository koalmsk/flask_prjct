import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class Recipes(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'recipes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    servings = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    instructions = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    # link_rel = orm.relationship("Recipes_to_Ingredients", back_populates='recipes_rel')