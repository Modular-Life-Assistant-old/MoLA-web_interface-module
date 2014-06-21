from core import Log

import bottle
import logging
import os

class Module:
    def add_home_page(self, name, handle):
        self.__home_page_available[name] = handle

    def load_configuration(self):
        self.__home_page_available = {}

        bottle.get('/')(self.__home_page)
        bottle.post('/')(self.__home_page)

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

    def thread_run(self):
        bottle.TEMPLATE_PATH[:0] = [
            '%s/views' % os.path.dirname(os.path.abspath(__file__)),
        ]

        if Log.get_logger().isEnabledFor(logging.DEBUG):
            bottle.debug()

        bottle.run(host='0.0.0.0', port=self.__config['port'], quiet=True)

    def __home_page(self):

        if self.__config['home_page'] in self.__home_page_available:
            return self.__home_page_available[self.__config['home_page']]

        if self.__home_page_available:
            return self.__home_page_available.itervalues().next()

        return 'Hello world'
