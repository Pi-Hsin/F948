"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from F948 import app

@app.route("/")
def home():
    return "Hello 948, Just Buy!"


@app.errorhandler(404)
def page_not_found(e):
    return "404: Sorry, there is not such page!"


@app.errorhandler(500)
def page_not_found(e):
    return "500: Sorry, some bug happend!!!"

if app.debug:
    @app.route("/test")
    def test():
        target_menu = menu.get_menu(u'-1')
        return json.dumps(target_menu)


#@app.route('/')
#@app.route('/home')
#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
