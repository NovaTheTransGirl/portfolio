from flask import Flask, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)

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
    return send_from_directory('static/data', 'projects.json')

if __name__ == "__main__":
    app.run(debug=True)
