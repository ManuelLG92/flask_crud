from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from app.main import db
from app.category.category_model import Category


class Article(db.Model):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, default=0)
    tax = Column(Integer, default=21)
    description = Column(String(255))
    image = Column(String(255))
    stock = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship(Category, backref="Article")

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'tax': self.tax,
            'stock': self.stock,
            'category': self.category.name
        }

    def final_price(self):
        return self.precio * self.iva / 100

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
