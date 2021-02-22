# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/<operation>')
def operate(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    ops = {
        'mult': operations.mult(a,b),
        'sub': operations.sub(a,b),
        'add': operations.add(a,b),
        'div': operations.div(a,b)
    }

    return f'<h1>{ops[operation]}</h1>'


# @app.route('/add')
# def add():
#     a = request.args['a']
#     b = request.args['b']
#     return f'<h1>{operations.add(a, b)}</h1>'

# @app.route('/sub')
# def subtract():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     return f'<h1>{operations.sub(a, b)}</h1>'

# @app.route('/mult')
# def mult():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     return f'<h1>{operations.mult(a, b)}</h1>'
    
# @app.route('/div')
# def div():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     return f'<h1>{operations.div(a, b)}</h1>'