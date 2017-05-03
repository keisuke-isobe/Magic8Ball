from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    page1 = """
    <h1>Hello World</h1>
    <ul>
      <li>
        <a href="/whoareyou">About</a>
      </li><li>
        <a href="/calculate">Calculator</a>
      </li>
    </ul>
    """
    return page1

@app.route('/whoareyou')
def r1():
    return 'I am Groot'

@app.route('/greeting/<name>')
def greeting(name):
        return 'How are you, '+name

@app.route('/calculate',methods=['GET','POST'])
def r2():
    page2 = """
    <form method="post" action="calculate">
      x <input type="text" name="x"> <br>
      <input type="submit">
      </form>
    """
    if request.method == 'POST':
        z = int(request.form['x'])
        return str(z*z)
    else:
        return page2;



if __name__ == '__main__':
    app.run('0.0.0.0')
