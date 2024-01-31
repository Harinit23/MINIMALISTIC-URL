from flask import Flask, render_template, request, redirect, url_for
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = shorten_url(original_url)
        return render_template('index.html', original_url=original_url, short_url=short_url)
    return render_template('index.html')

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

if __name__ == '__main__':
    app.run(debug=True)