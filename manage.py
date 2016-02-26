from flask import Flask, jsonify
from app.views import *
from sqlalchemy import *
from flask.ext.admin import Admin, BaseView, expose
from app.algorithms import *
from app.models import *

app = Flask(__name__)
admin = Admin(app)

@app.route('/')
def index():
    return "hello world"

@app.route('/lott/api/v1.0/douballs/top/<int:count>')
def get_douball_list(count):
    result = Doublechrom.get_top_list(count)
    lastlist = result.tolist()
    print(type(result))
    return jsonify({'the top '+ str(count) : str(lastlist),'and ordered' : str(sorted(lastlist))})

@app.route('/lott/api/v1.0/douballs/random/<int:count>')
def get_douball_random(count):
    result = Doublechrom.get_random_list(count)
    print(type(result))
    return jsonify({'return random result' : str(result)})

@app.route('/user/<string:username>')
def show_user_profile(username):
    return 'User %s' % username


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


admin.add_view(MyView(name='momocha'))

if __name__ == '__main__':
    app.run(debug=True)

# class Person(object):
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
