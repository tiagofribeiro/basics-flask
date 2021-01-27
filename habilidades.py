from flask_restful import Resource

habilidades = ["Python", "C#", "Angular", ".NET", "PHP"]

class Habilidades(Resource):
    def get(self):
        return habilidades