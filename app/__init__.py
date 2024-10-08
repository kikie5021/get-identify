# -*- coding: utf-8 -*-

from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy

from app import constants as C

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

from app import views

app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.globals['C'] = C
