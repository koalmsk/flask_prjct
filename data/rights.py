import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class UserRights(SqlAlchemyBase):
    __tablename__ = 'user_rights'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"), nullable=False)
    right = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    user_rel = orm.relationship('User')
