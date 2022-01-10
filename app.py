from prediction_service import prediction
from flask import Flask, render_template, request, jsonify
import os
import numpy as np

webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)


@app.route("/", methods=['GET', 'POST'])
def home():
    """
    :Method_Name: home
    :DESC: This Will Return The Home Page
    :param: None
    :return: index.html
    """

    try:
        return render_template('index.html')

    except Exception as e:
        raise Exception(f'(Home)- Something Went Wrong With The Method \n' + str(e))


@app.route("/predict", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        try:
            if request.form:
                dict_req = dict(request.form)
                response = prediction.form_response(dict_req)
                return render_template('result.html', prediction_text=" The Credit Risk Is {}".format(response))
            elif request.json:
                response = prediction.api_response(request.json)
                return jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}
            return render_template("404.html", error=error)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
