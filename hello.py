def application(environ, start_response):
    start_response('200 0k', [('Content-Type', 'text/html')])
    return '<h1>Hello,Web!</h1>'

