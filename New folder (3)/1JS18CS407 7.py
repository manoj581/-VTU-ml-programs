import numpy as np
import pandas as pd
import csv
from pgmpy.factors.discrete import DiscreteFactor
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
#Read the attributes
lines = list(csv.reader(open('71.csv','r')));
attributes = lines[0]

#Read Cleveland Heart dicease data
heartDisease = pd.read_csv('72.csv', names = attributes)
heartDisease = heartDisease.replace('?', np.nan)
# Display the data
print('Few examples from the dataset are given below')
print(heartDisease.head())
print('\nAttributes and datatypes')
print(heartDisease.dtypes)
# Model Baysian Network
model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'),
('exang', 'trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),
('heartdisease','restecg'),('heartdisease','thalach'),('heartdisease','chol')])
# Learning CPDs using Maximum Likelihood Estimators
print('\nLearning CPDs using Maximum Likelihood Estimators...');
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
# Inferencing with Bayesian Network
print('\nInferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)
# Computing the probability of bronc given smoke.
print('\n1.Probability of HeartDisease given trestbps and fbs')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'trestbps': 4,'fbs': 0})
print(q)#['heartdisease'])
print('\n2. Probability of HeartDisease given chol (Cholestoral) =100')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'fbs': 1})
print(q)#['heartdisease'])
