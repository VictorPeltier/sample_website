# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Happycal
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/happycals/', methods=['POST', 'GET'])
    def happycals():
        if request.method == "POST":
            name = str(request.data.get('name',''))
            if name:
                happycal = Happycal(name=name)
                happycal.save()
                response = jsonify({
                    'id':happycal.id,
                    'name':happycal.name,
                    'date_created':happycal.date_created,
                    'date_modified':happycal.date_modified
                })
                response.status_code = 201
                return response
        else:
            #GET
            happycals = Happycal.get_all()
            results = []

            for happycal in happycals : 
                obj = {
                    'id':happycal.id,
                    'name':happycal.name,
                    'date_created':happycal.date_created,
                    'date_modified':happycal.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response
    @app.route('/happycals/<int:id>', methods=['GET','PUT','DELETE'])
    def happycal_manipulation(id, **kwargs):
        #retrieve a bucketlist using its ID
        happycal = Happycal.query.filter_by(id=id).first()
        if not happycal:
            #Raise a 404 not found status code
            abort(404)
        if request.method == 'DELETE':
            happycal.delete()
            return {"message":"happycal {} deleted successfully".format(happycal.id)},200

        elif request.method =='PUT':
            name = str(request.data.get('name',''))
            happycal.name = name
            happycal.save()
            response = jsonify({
                'id':happycal.id,
                'name':happycal.name,
                'date_created':happycal.date_created,
                'date_modified':happycal.date_modified
            })
            response.status_code = 200
            return response

        else: 
            #GET
            response = jsonify({
                'id':happycal.id,
                'name':happycal.name,
                'date_created':happycal.date_created,
                'date_modified':happycal.date_modified
            })
            response.status_code=200
            return response

    return app