from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:PORTNUMBER/beerzy'
db = SQLAlchemy(app)

beer_brewery = db.Table('beer_brewery',
    db.Column('beer_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    db.Column('brewery_id', db.Integer, db.ForeignKey('post.id'), primary_key=True))

class Beer(db.Model):
    __tablename__ = 'beers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    style = db.Column(db.String, nullable=False)
    brewerys = db.relationship('Brewery',
        secondary=beer_brewery,
        lazy='subquery', #runs second query only if first one is successful
        backref=db.backref('posts', lazy=True)
        )
  
    def __repr__(self):
        return f'Beer(id={self.id}, name="{self.name}", style="{self.style}")'
    
    def as_dict(self):
	    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Post(db.Model):
    __tablename__ = 'brewerys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String, nullable=False)
    

def get_or_create(model, defaults=None, **kwargs):
    	instance = db.session.query(model).filter_by(**kwargs).first()
	if instance:
		return instance, False
	else:
		params = dict((k,v) for k, v in kwargs.items())
		params.update(defaults or {})
		instance = model(**params)
		db.session.add(instance)
		return instance, True