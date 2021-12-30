from flask import Flask, render_template, request
import joblib
import yaml
import os

params_path = "params.yaml"

templates = os.path.join("webapp", "templates")

app = Flask(__name__, template_folder=templates)


def read_params(config_path=params_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


config = read_params(params_path)
model_dir_path = config["webapp_model_dir"]
model = joblib.load(model_dir_path)


@app.route("/", methods=['GET', 'POST'])
def home():
    """
    Method_Name: home
    :DESC: This Will Return The Home Page
    :param: None
    :return: index.html
    """
    try:
        return render_template('index.html')

    except Exception as e:
        raise Exception(f'(Home)- Something Went Wrong With The Method \n' + str(e))


@app.route("/predict", methods=['POST'])
def predict():
    """
    Method_Name: predict
    :DESC: This Will Return The Credit Risk Is Bad or Good
    :param: None
    :return: The Risk Is Bad or Good
    """
    try:
        if request.method == "POST":
            try:
                status = int(request.form['status'])

                duration = int(request.form['duration'])

                credit_history = int(request.form['credit_history'])

                purpose = int(request.form['purpose'])

                amount = int(request.form['amount'])

                savings = int(request.form['savings'])

                employment_duration = int(request.form['employment_duration'])

                personal_status_sex = int(request.form['personal_status_sex'])

                installment_rate = int(request.form['installment_rate'])

                present_residence = int(request.form['present_residence'])

                property = int(request.form['property'])

                age = int(request.form['age'])

                number_credits = int(request.form['number_credits'])

                telephone = int(request.form['telephone'])

                value = model.predict([[status, duration, credit_history, purpose, amount, savings,
                                        employment_duration, personal_status_sex, installment_rate,
                                        present_residence, property, age, number_credits, telephone]])

                if value == 0:
                    label = 'Bad'
                else:
                    label = 'Good'

                return render_template('result.html', prediction_text=" The Credit Risk Is {}".format(label))

            except Exception as e:
                raise Exception(f'(Predict)- Something Went Wrong With The Method \n' + str(e))

        else:
            return render_template('index.html')

    except Exception as e:
        raise Exception(f'(Predict)- Something Went Wrong With The Method \n' + str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
