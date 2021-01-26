from flask import Flask

app = Flask(__name__)

desenvolvedores = [
    {
        "nome" : "Tiago",
        "habilidades" : ["Python", "React", ".NET"]
    },
    {
        "nome" : "Roberto",
        "habilidades" : ["Python", "Angular", ".NET"]
    }
]

@app.route('/dev/<int:id>')
def desenvolvedor(id):
    desenvolvedor = desenvolvedores[id]
    return desenvolvedor

if __name__ == "__main__":
    app.run()