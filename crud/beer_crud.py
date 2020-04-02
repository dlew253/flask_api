from flask import jsonify, redirect
from models import db, Beer, Brewery, get_or_create, beer_brewery
from crud.brewery_crud import create_brewery

def get_all_beers():
	all_beers = Beer.query.all()
	if all_beers:
		results = [beer.as_dict() for beer in all_beers]
		return jsonify(results)
	else:
		raise Exception('Error getting all beers')
def get_beer(id):
	beer = Beer.query.get(id)
	if beer:
		return jsonify(beer.as_dict())
	else:
		raise Exception('Error getting beer at id {}'.format(id))
def create_beer(name, style):
	new_beer = Beer(name=name, style=style or None)
	if new_beer:
		db.session.add(new_beer)
		db.session.commit()
		return jsonify(new_beer.as_dict())
	else:
		raise Exception('Error in creating new beer')
def destroy_beer(id):
	beer = Beer.query.get(id)
	if beer:
		db.session.delete(beer)
		db.session.commit()
		return redirect('/beers')
	else:
		raise Exception('Error deleting user at id {}'.format(id))
def update_beer(id, name, style):
	beer = Beer.query.get(id)
	if beer:
		beer.name = name or beer.name
		beer.style = style or beer.style
		db.session.commit()
		return redirect('/beers/{}'.format(id))
	else:
		raise Exception('Error updating beer at id {}'.format(id))

def update_beer_brewery(id, beer, brewery):
	beer = Beer.query.get(id)
	brewery = None
	if beer:
		try:
			with db.session.begin_nested():
				brewery = create_brewery(name, city)
		except Exception as error:
			search_name = '%' + name + '%'
			brewery = Brewery.query.filter(Brewery.name.ilike(search_name)).one()			
		beer.brewerys.append(brewery)
		db.session.commit()		
		return redirect('/beers/{}'.format(id))
	else:
		raise Exception('Error adding Brewery to beer at id {}'.format(id))
def show_beer_brewery(id):
	beer = Beer.query.get(id)
	curr_brewerys = beer.brewerys
	results = [brewery.as_dict() for brewery in curr_brewerys]
	return jsonify(results)
