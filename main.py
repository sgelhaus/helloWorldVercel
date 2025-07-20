# api/hello.py

def handler(request, response):
    return response.send("Hello World")
