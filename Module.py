from core import Log

from modules.web_interface.pages import home

from flask import Flask
import json
import logging
import os

class Module:
    def __init__(self):
        self.__flask = Flask(__name__)

    def add_home_page(self, *args, **kwargs):
        home.add_home_page(*args, **kwargs)

    def load_configuration(self):
        config = {}
        config_path = '%s/configs/web.json' % (
            os.path.dirname(os.path.abspath(__file__))
        )

        if os.path.isfile(config_path):
            with open(config_path) as config_file:
                config = json.load(config_file)

        self.__port = config['port'] if 'port' in config else 14212

    def get_app(self):
        return self.__flask

    def register_blueprint(self, app):
        self.__flask.register_blueprint(app)

    def thread_run(self):
        self.register_blueprint(home.app)

        self.__flask.run(
            host='0.0.0.0',
            port=self.__port,
            debug=Log.get_logger().isEnabledFor(logging.DEBUG),
            use_reloader=False,
        )
