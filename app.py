from flask import Flask, render_template

app = Flask(__name__)

@app.route('/kvadrat/<int:son>')
def kvadrat(son):
    return render_template('kvadrat.html', son=son, natija=son**2)

if __name__ == "__main__":
    app.run(debug=True)
