from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def show_pics():
    return render_template('pratice2.html')


if __name__ == '__main__':
    app.run(debug=True)