from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

healthcare_data = pd.read_csv("healthcare_dataset.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input
        name = request.form["name"]
        gender = request.form["gender"]
        blood_group = request.form["blood_group"]

        # Filter healthcare data based on user input
        filtered_data = healthcare_data[(healthcare_data["Gender"] == gender) & (healthcare_data["Blood Group Type"] == blood_group)]

        # Find the most common medical condition
        most_common_condition = filtered_data["Medical Condition"].mode().iloc[0]

        # Store user data
        user_data = pd.DataFrame({"Name": [name], "Gender": [gender], "Blood Group": [blood_group]})
        user_data.to_csv("user_data.csv", mode="a", index=False, header=not bool(pd.read_csv("user_data.csv").shape[0]))

        return render_template("template/result.html", name=name, condition=most_common_condition)
    return render_template("template/index.html")

if __name__ == "__main__":
    app.run(debug=True)
