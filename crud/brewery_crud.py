from flask import jsonify, redirect
from models import db, Beer, Brewery
def get_all_brewery():
	all_brewery = Brewery.query.all()
	if all_brewery:
		result = [brewery.as_dict() for brewery in all_brewery]
		return jsonify(results)
	else:
		raise Expection('Error getting all brewery')
def get_brewery(id):
	brewery = Brewery.query.get(id)
	if brewery:
		return jsonify(brewery.as_dict())
	else:
		raise Expection('Error getting brewery at id {}'.format(id))
def create_brewery(name, city):
	new_brewery = Food(name=name, city=city)
	if new_brewery:
		db.session.add(new_brewery)
		db.session.commit()
		return jsonify(new_brewery.as_dict())
	else:
		raise Expection('Error in creating new brewery')