from flask import Flask, url_for, render_template
import recommend as r

app = Flask(__name__)
db = r.DataBase(users_file='datasets/ml-100k/uhead.user',
              movies_file='datasets/ml-100k/u.item',
              ratings_file='datasets/ml-100k/uhead.data')
db.calculate_similarities()

@app.route('/')
def hello_world():
    return 'Hello World! ' + url_for('hello')

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<user>')
def show_user_profile(user):    # db=db):
    # show the user profile for that user
    db.users[user].sort_ratings()
    rec = db.recommend(user, n=20, mode='simple', num_users=5)
    print('Your favorite movies:\n', '*'*40)
    favs = db.translate(db.users[user].my_favorites(n=500), fn=db.get_title)
    print('Your recommending movies:\n', '*'*40)
    recs = db.translate(rec, fn=db.get_title) # TODO: Add decorator for translate?
    users = sorted([i for i in db.users], key=int)

    return render_template('user.html', user=user, db=db, favs=favs, recs=recs, users=users)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/bla')
def blabla():
    bla = 'blah..blah...'
    return render_template('template.html', bla=bla)


if __name__ == '__main__':

    app.run(debug=True)
