from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

url_history = []

keys = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def uniqueid():
    uni_id = ''
    for i in range(6):
        uni_id += keys[random.randint(0,35)]
    return uni_id

# shortlink = 'www.myshortlink.'

@app.route('/',methods = ['GET','POST'])
def index():

    if request.method == 'POST':

        og_url = request.form.get('long_url')

        if not og_url.startswith(('http://', 'https://')):
            og_url = 'https://' + og_url

        while True:

            uni_id = uniqueid()

            exist = False

            for url in url_history:
                if uni_id == url['uni_id']:
                    exist = True
                    break

            if not exist:
                url_history.append({
                    'uni_id': uni_id,
                    'og_url': og_url
                })
                break

        short_url = f"http://localhost:5000/{uni_id}"

        return render_template(
            'index.html',
            short_url=short_url
            ,url_history=url_history
        )

    return render_template('index.html', url_history=url_history)

@app.route('/<uni_id>')
def shorturl(uni_id):

    for url in url_history:
        if url['uni_id'] == uni_id:
            return redirect(url['og_url'])

    return "URL Not Found"

if __name__ == "__main__":
    app.run(debug=True)
