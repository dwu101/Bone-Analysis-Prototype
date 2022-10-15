from flask import Flask
import SlopeOfBoneCalculator

app = Flask(__name__)


@app.route('/')
def wandrea():
    angle = SlopeOfBoneCalculator.run_code()
    return str(angle)


if __name__ == "__main__":
    app.run()


# run by typing     python bucketapp.py     in terminal, but first change cd to backend
#  flask --app app run
