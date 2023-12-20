# Flask imports.
from flask import Flask, request, Response, render_template
from openai import OpenAI

# Our modules.
from question import *
import utils as utils


# Set OpenAI API key.
aiClient = OpenAI(
    api_key = utils.get_env_value("OPENAI_API_KEY")
)

# Make the Flask app.
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/question")
def question():
    return render_template("question.html")


@app.route("/craft", methods = ["POST"])
def craft():
    if request.method == "POST":
        # Create a question object from the form data.
        question = Question(
            request.form["variable1"],
            request.form["variable2"],
            request.form["context"],
            request.form["concept"],
            request.form["ai"]
        )

        # Craft the question via the `OpenAI` API.
        question.craftQuestion(aiClient)

        # Return the question template.
        return render_template("craft.html", question = question)
