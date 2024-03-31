import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase



class Comments(SqlAlchemyBase):
    __tablename__ = 'comments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    
    recipe_id = sqlalchemy.Column(sqlalchemy.Integer)
    
    from_user_id = sqlalchemy.Column(sqlalchemy.Integer)
    
    text = sqlalchemy.Column(sqlalchemy.String)
