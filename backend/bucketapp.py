from flask import Flask 
app = Flask(__name__)

@app.route('/')
def wandrea():
    return "hello world"


if __name__ == "__main__":
    app.run()


#run by typing     python bucketapp.py     in terminal, but first change cd to backend 