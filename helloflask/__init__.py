from flask import Flask, g, request , Response, make_response, render_template

app = Flask(__name__)
app.debug = True

@app.route("/tmpl")
def t():
    return render_template('1.html', title="yckim" , num = 1)

@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.getlist('q')
    return "q=%s"%str(q)



@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'),
                    ('Content-Length', str(len(body)))]
        start_response('200 OK', headers)
        return [body]
    
    return make_response(application)

@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 201, {'test': 'ttt'})
    return make_response(custom_res)

# @app.before_request
# def before_request():
#     print("before_request")
#     g.str = "한글"

# @app.route("/gg")
# def helloworld2():
#     return "Hello Flask Word!!!!!" + getattr(g, 'str', '111')  # 3번째 111은 default str 이 없으면 111

@app.route("/")
def helloworld():
    return "Hello Flask Word!!!!!"