from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file:
            return 'Your file has been uploaded successfully'

    return '''
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file" accept=".csv,.xlsx,.pdf">
      <input type="submit" value="Upload">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=8000)
