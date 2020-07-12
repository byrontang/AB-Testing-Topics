# From the course: Bayesin Machine Learning in Python: A/B Testing
# https://deeplearningcourses.com/c/bayesian-machine-learning-in-python-ab-testing
# https://www.udemy.com/bayesian-machine-learning-in-python-ab-testing
from __future__ import print_function, division
from builtins import range
# Note: you may need to update your version of future
# sudo pip install -U future


import numpy as np
from flask import Flask, jsonify, request
from scipy.stats import beta

# create an app
app = Flask(__name__)


# define bandits
# there's no "pull arm" here
# since that's technically now the user/client
class Bandit:
    def __init__(self, name):
        self.name = name
        self.a = 1
        self.b = 1

    def sample(self):
        # TODO
        return np.random.beta(self.a, self.b)

    # TODO - what else does the Bandit need to do?
    def update(self):
        self.a += x
        self.b += 1-x

# initialize bandits
banditA = Bandit('A')
banditB = Bandit('B')



@app.route('/get_ad')
def get_ad():
    # TODO
    if banditA.sample() > banditB.sample():
        return jsonify({'advertisement_id': 'A'})
    else:
        return jsonify({'advertisement_id': 'B'})


@app.route('/click_ad', methods=['POST'])
def click_ad():
    result = 'OK'
    if request.form['advertisement_id'] == 'A':
        # TODO
        banditA.update(1)
        banditB.update(0)
        pass
    elif request.form['advertisement_id'] == 'B':
        # TODO
        banditA.update(0)
        banditB.update(1)
        pass
    else:
        result = 'Invalid Input.'

    # nothing to return really
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8889')