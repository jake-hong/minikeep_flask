from flask import Flask

def create_app():
    print('run:create_app()')
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'hello world!'
    
    """routing practice"""
    from flask import jsonify, redirect, url_for 
    from markupsafe import escape

    @app.route('/test/name/<name>')
    def name(name):
        return f"name is {name},{escape(type(name))}"
    
    @app.route('/test/id/<int:id>')
    def id(id):
        return 'Id: %d' % id

    @app.route('/test/path/<path:subpath>')
    def path(subpath):
        return subpath

    @app.route('/test/json')
    def json():
        return jsonify({'hello':'world'}) 

    @app.route('/test/redirect/<path:subpath>')
    def redirect_url(subpath):
        return redirect(subpath)

    @app.route('/test/urlfor/<path:subpath>')
    def urlfor(subpath):
        return redirect(url_for('path',subpath=subpath))    
    
    """Method""" 
    from flask import request

    @app.route('/test/method/<id>', methods=['GET','POST'])
    def method(id):
        return jsonify({
            'request.args':request.args,
            'request.form':request.form,
            'request.json':request.json,
            'request.method':request.method
        })
        
    return app 