from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from app.main import db


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    article = relationship("Article", backref="Category", lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
