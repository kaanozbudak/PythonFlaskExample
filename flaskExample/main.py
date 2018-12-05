from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'this is the homepage and method used : %s' % request.method
#
#
# @app.route('/tuna', methods=['GET', 'POST'])
# def tuna():
#     if request.method == 'POST':
#         return 'you are using post'
#     else:
#         return 'this is tuna page and you are using get method'
#
#
# @app.route('/profile/<username>', methods=['GET','POST'])
# def profile(username):
#     if request.method == 'POST':
#         return "<h1>Hey post method :  %s</h1>" % username
#     else:
#         return 'this is a get method : %s' %username
#
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     return '<h1>Post id is %s</h1>' % post_id

# @app.route("/profile/<username>", methods=['GET', 'POST'])
# def profile(username):
#     if request.method == 'GET':
#         return render_template("profile.html", username=username, met='get')
#     else:
#         return render_template("profile.html", username=username, met='post')
#

@app.route('/profile/')
@app.route('/profile/<user>')
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Tuna', 'Beef', 'Sheep']
    return render_template("shopping.html", food=food)


if __name__ == "__main__":
    app.run(debug=True)
