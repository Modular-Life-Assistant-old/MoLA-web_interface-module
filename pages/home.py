from core import ModuleManager


from flask import Flask, request

__app = ModuleManager.get('web_interface').get_app()
__home_page_available = {}
__home_page = ''

def add_home_page(name, url, description, logo=''):
    __home_page_available[name] = {
        'name':         name,
        'url':          url,
        'description':  description,
        'logo':         logo,
    }


@__app.route('/')
def home_page():
    if __home_page in __home_page_available:
        return bottle.redirect(__home_page_available[__home_page]['url'])

    return bottle.redirect('/menu')


@__app.route('/menu')
def menu_page():
    return __home_page_available