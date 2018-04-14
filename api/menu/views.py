import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from api import db, app
from api.models import Menu

menu = Blueprint('menu', __name__)


@menu.route('/')
@menu.route('/home')
def home():
    return "Welcome to the Menu Home."


class MenuView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            menus = Menu.query.paginate(page, 10).items
            res = {}
            for menu in menus:
                res[menu.id] = {
                    'name': menu.name,
                    'price': str(menu.price),
                }
        else:
            menu = Menu.query.filter_by(id=id).first()
            if not menu:
                abort(404)
            res = {
                'name': menu.name,
                'price': str(menu.price),
            }
        return jsonify(res)

    def post(self):
        # get the post data
        post_data = request.get_json()

        name = post_data.get('name')
        price = post_data.get('price')
        menu = Menu(name, price)
        db.session.add(menu)
        db.session.commit()
        return jsonify({menu.id: {
            'name': menu.name,
            'price': str(menu.price),
        }})

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id.
        return


menu_view = MenuView.as_view('menu_view')
app.add_url_rule(
    '/menu/', view_func=menu_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/menu/<int:id>', view_func=menu_view, methods=['GET']
)
