from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def root():
    return "in the root!!"

@app.route("/webhook", methods=['POST'])
def webHook():
    print(request.json)
    return Response(status=200)

if __name__ == '__main__':
    app.run()