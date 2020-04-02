from models import app, Beer
from flask import jsonify, request
from crud.beer_crud import get_all_beer, get_beer, create_beer, destroy_beer, update_beer, update_beer_brewery, show_beer_brewery
from crud.brewery_crud import get_brewery

@app.errorhandler(Exception)
def unhandled_exception(e):
  app.logger.error('Unhandled Exception: %s', (e))
  message_str = e.__str__()
  return jsonify(message=message_str.split(':')[0])

@app.route('/beers', methods=['GET', 'POST'])
def user_index_and_create():
	if request.method == 'GET':
		return get_all_beer()
	if request.method == 'POST':
		return create_beer(
			name=request.form['name'],
			style=request.form['style'],			
		)

@app.route('/beers/<int:id>', methods=['GET','PUT', 'DELETE'])
def beer_show_update_delete(id):
	if request.method == 'GET':
		return get_beer(id)
	if request.method == 'PUT':
		return update_beer(
			id=id,
			name=request.form['name'],
			style=request.form['style'],
		)
	if request.method == 'DELETE':
		return destroy_beer(id)
@app.route('/users/food/<int:id>', methods=['GET', 'PUT'])
def beer_show_update_brewery(id):
	if request.method == 'PUT':
		return update_beer_brewery(
			id=id,
			name=request.form['name'],
			city=request.form['city']
		)
	if request.method == 'GET':
		return show_beer_brewery(id=id)