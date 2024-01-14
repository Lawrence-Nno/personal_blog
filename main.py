from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)
blog_url = "https://api.npoint.io/e3c6f44ee275f65fb30e"
response = requests.get(blog_url)
all_posts = response.json()

current_time = datetime.now()
current_year = current_time.year


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts, year=current_year)


@app.route('/about')
def about():
    return render_template('about.html', year=current_year)


@app.route('/contact')
def contact():
    return render_template('contact.html', year=current_year)


@app.route('/post')
def post():
    return render_template('post.html', year=current_year)


@app.route('/post/<int:num>')
def get_post(num):
    for blog_post in all_posts:
        if blog_post['id'] == num:
            requested_post = blog_post
    return render_template('post.html', num=num, post=requested_post, year=current_year)


if __name__ == '__main__':
    app.run(debug=True)