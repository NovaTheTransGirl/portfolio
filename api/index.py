from flask import Flask, render_template, redirect, url_for, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/home")
def home():
    return render_template("home.html", page="home")

@app.route("/")
def redir():
    return redirect("/home")

@app.route("/meow/<page>")
def meow_page(page):
    try:
        html = render_template(f"{page}.html", page=page)
        return html.replace(">", ">meow ").replace("</", "meow</")
    except:
        return redirect(url_for("home"))

@app.route('/static/data/projects.json')
def projects_json():
    return send_from_directory('../static/data', 'projects.json')

# Required for Vercel Python runtime
def handler(environ, start_response):
    return app(environ, start_response)
