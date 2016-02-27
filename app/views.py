__author__ = 'IfCheung'

@app.route('/user/<string:username>')
def show_user_profile(username):
    return 'User %s' % username






