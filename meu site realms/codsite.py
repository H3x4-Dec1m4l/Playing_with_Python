from flask import Flask, render_template

app = Flask(__name__)
# primeira pag
@app.route("/home")
def homepage():
    return render_template("servidor realms")



# site no ar

if __name__ == '__main__':
    app.run(debug=True)

# servidor  


