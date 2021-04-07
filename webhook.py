from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def root():
    return "in the root!!"

@app.route("/webhook", method=['POST'])
def webHook():
    print(request.json)
    return Response(status=200)