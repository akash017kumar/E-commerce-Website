from flask import Flask, redirect
from api import api_bp
from database import insert_static_data
from flasgger import Swagger

app = Flask(__name__)

insert_static_data()

swagger = Swagger(app, template_file='swagger.yml')

app.register_blueprint(api_bp)

# Redirect root URL to Swagger UI
@app.route('/')
def redirect_to_docs():
    return redirect('/apidocs/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
