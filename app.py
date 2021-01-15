#!/usr/bin/env python3

"""A website to house my coding portfolio."""

from flask import Flask, render_template, request

app = Flask(__name__, static_folder='./assets')


@app.route('/')
def index():
    return render_template('index.html')