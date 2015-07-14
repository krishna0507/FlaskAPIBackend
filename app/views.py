from app import app, models, db, auth
from flask import jsonify, request, abort, make_response, url_for

@auth.get_password
def get_password(username):
    if username == 'python':
        return 'flask'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.route('/')
def index():
	return "Welcome to my API Back-end System!"

def getUri(user):
	return url_for('getuser', user_id = user.id, _external = True)

@app.route('/userlist', methods=['GET'])
@auth.login_required
def allusers():
	users = models.User.query.all()
	if len(users)==0:
		abort(404)
	Users = []
	temp_user = {}
	for u in users:
		temp_user = {}
		temp_user['id'] = u.id
		temp_user['nickname'] = u.nickname
		temp_user['email'] = u.email
		temp_user['uri'] = getUri(u)
		Users.append(temp_user)
	return jsonify({'Users':Users})

@app.route('/userlist/<int:user_id>', methods=['GET'])
@auth.login_required
def getuser(user_id):
	user = models.User.query.get(user_id)
	if not user:
		abort(404)
	temp_user = {}
	temp_user['id'] = user.id
        temp_user['nickname'] = user.nickname
        temp_user['email'] = user.email	
	return jsonify({'User':temp_user})

@app.route('/adduser', methods=['POST'])
@auth.login_required
def adduser():
	if not request.json or not 'nickname' in request.json or not 'email' in request.json:
		abort(400)
	u = models.User(nickname=request.json['nickname'],email=request.json['email'])
	db.session.add(u)
	db.session.commit()
	return jsonify(request.json)

@app.route('/deleteuser/<int:user_id>', methods=['DELETE'])
@auth.login_required
def deleteuser(user_id):
        user = models.User.query.get(user_id)
        if not user:
                abort(404)
        db.session.delete(user)
	db.session.commit()
        return jsonify( { 'result': True } )
	
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
