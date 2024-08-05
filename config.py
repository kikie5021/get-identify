import os

_basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    #: Basic config
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD = False

    #: Security
    SECRET_KEY = '\xd9\xbe\x06\xd4\xeaG\x11\xa1\xd4\xa8E\xd9Q`\x84\x1eHzr5\xc1\xe2\x86\xe5'
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SESSION_KEY = '\xbf\nr$\x1e\x0e\x8e*B\x84\xe0\x16\xfb_\xb2\x0ft\xf3\x0bhbD\xbc\xea'

    #: Database connection
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #: Asset files
    CSS_ALL = [
        'css/vendor/animate.css', 'css/vendor/fontawesome-all.min.css',
        'css/vendor/milligram.min.css', 'css/vendor/normalize.css',
        'css/vendor/notosans.css', 'css/main.css']
    JS_ALL = [
        'js/vendor/jquery-3.2.1.min.js', 'js/vendor/jquery.placeholder.js',
        'js/vendor/wow.min.js', 'js/main.js']


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD = False


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    TESTING = True
