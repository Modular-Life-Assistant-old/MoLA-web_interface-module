from core import ModuleManager

from flask import Blueprint, redirect

app = Blueprint('home', __name__)

__home_page_available = {}
__home_page = ''

def add_home_page(name, url, description, logo=''):
    __home_page_available[name] = {
        'name':         name,
        'url':          url,
        'description':  description,
        'logo':         logo,
    }


@app.route('/')
def home_page():
    if __home_page in __home_page_available:
        return redirect(__home_page_available[__home_page]['url'])

    return redirect('/menu')


@app.route('/menu')
def home_list():
    return str(__home_page_available)
