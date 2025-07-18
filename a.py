from flask import Flask, request, render_template
from livereload import Server
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

app = Flask(__name__)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")



@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    user_input = ""
    if request.method == 'POST':
        user_input = request.form["prompt"]
        try:
            response = model.generate_content(user_input)
            response_text = response.text
        except Exception as e:
            response_text = f"An error occurred: {e}"
    return render_template('index.html', response=response_text, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
    # server = Server(app.wsgi_app)
    # server.watch("app.py")
    # server.watch("templates/")
    # server.serve(port=5000, debug=True)
