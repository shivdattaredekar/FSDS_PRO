from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

Movie_list = ['Dhoom', 'KGF', 'KGF2', 'Bahubali', 'Pathaan', 'Jawan']

functions = ['/read', '/update/<string:movie_name>', '/delete/<string:movie_name>']

@app.route('/')
def Home():
    return f'Welcome to home page, choose from any of the options and start working {functions}'

@app.route('/read')
def movie_lists():
    return jsonify(Movie_list)

@app.route('/update/<string:movie_name>', methods=['GET'])
def update_movie_name(movie_name):
    if movie_name not in Movie_list:
        Movie_list.append(movie_name)
        return jsonify({"message": f'Updated the list with new addition of {movie_name}'}), 201
    else:
        return jsonify({"message": f'{movie_name} already exists in the list'})

@app.route('/delete/<string:movie_name>', methods=['GET'])
def delete_movie_name(movie_name):
    if movie_name in Movie_list:
        Movie_list.remove(movie_name)
        return jsonify({"message": f'Deleted {movie_name} from the list'})
    else:
        return jsonify({"message": f'{movie_name} does not exist in the list'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
