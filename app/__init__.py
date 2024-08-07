from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
config = ('config.TestingConfig',
          'config.DevelopmentConfig',
          'config.ProductionConfig')[0 if app.testing else 1 if app.debug else 2]
app.config.from_object(config)

assets = Environment(app)
db = SQLAlchemy(app)

css = Bundle(*app.config['CSS_ALL'], output='gen/packed.css')
js = Bundle(*app.config['JS_ALL'], output='gen/packed.js')

assets.register('css_all', css)
assets.register('js_all', js)

logger.info("Flask app created")

from app import views  # นำเข้า views ที่นี่
from app.views import main as main_blueprint  # นำเข้า Blueprint

app.register
