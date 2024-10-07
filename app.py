from flask import Flask,render_template,request
import google.generativeai as genai
import os
import numpy as np
from textblob import TextBlob

model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key="AIzaSyCluRjLkwn6IOe4f-dNTlusyuAkDUI7fQo")

app = Flask(__name__)
user_name = ""
flag = 1

@app.route("/", methods=["GET", "POST"])
def index():
    global flag
    flag = 1
    return render_template("index.html")

