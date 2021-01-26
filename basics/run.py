from flask import Flask
app = Flask(__name__)

@app.route("/<int:parameter>", methods=['GET','POST'])
def hello(parameter):
    return f'Hello World. {parameter}'

if __name__ == "__main__":
    app.run(debug=True)