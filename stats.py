from flask import Flask, render_template, request
import numpy as np
import statistics
import matplotlib.pyplot as plt

app = Flask(__name__)
NUM_PTS = 10000

@app.route("/")
def home():
    # mean = request.args.get('mean')
    # std = request.args.get('std')
    mean = 0.0
    std = 0.447213595

    create_normal(mean, std)
    
    return render_template("home.html")

# Generate a graph for the uniform distribution given the mean and standard deviation
def create_uniform(mean, std):
    print('todo')

# Generate a graph for the uniform distribution given the mean and standard deviation
def create_normal(mean, std):
    s = np.random.normal(mean, std, NUM_PTS)
    
    count, bins, ignored = plt.hist(s, 30, density=True)
    plot = plt.plot(bins, 1/(std * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mean)**2 / (2 * std**2) ),
            linewidth=2, color='r')
    
    

# Generate a graph for the uniform distribution given the mean and standard deviation
def create_binomial(mean, std):
    print('todo')

create_normal(0, 0.1)
