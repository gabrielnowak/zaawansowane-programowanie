from flask import Flask
from flask_restful import Resource, Api
import csv
import json
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Movie:
    def __init__(self, movieID, title, genres):
        self.movieID = movieID
        self.title = title
        self.genres = genres
    def __str__(self):
        return {self.movieID , self.title, self.genres}
class Movies(Resource):
    def get(self):
        json_string = json.dumps([ob.__dict__ for ob in movies])
        return json_string
with open('movies.csv',encoding = 'utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    movies = []
    for row in csvreader:
        movie = Movie(row[0], row[1], row[2])
        movies.append(movie)

for x in movies:
    print(x.__str__())

app = Flask(__name__)
api = Api(app)

api.add_resource(Movies, '/movies')
if __name__ == '__main__':
    app.run(debug=True)