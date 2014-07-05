from core import Log

from modules.web_interface.pages import home

from flask import Flask
import logging
import os

class Module:
    def __init__(self):
        self.__flask = Flask(__name__)

    def add_home_page(self, *args, **kwargs):
        home.add_home_page(*args, **kwargs)

    def load_configuration(self):
        try:
            module_path = os.path.dirname(os.path.abspath(__file__))
            with open('%slog.conf' % module_path) as config_file:
                self.__config = json.load(config_file)

        except EnvironmentError:
            # default config
            self.__config = {
                'port':         14212,
                'home_page':    '',
            }

    def get_app(self):
        return self.__flask

    def register_blueprint(self, app):
        self.__flask.register_blueprint(app)

    def thread_run(self):
        self.register_blueprint(home.app)

        self.__flask.run(
            host='0.0.0.0',
            port=self.__config['port'],
            debug=Log.get_logger().isEnabledFor(logging.DEBUG),
            use_reloader=False,
        )
