import pandas as pd
import numpy as np
import json as js

data = [{"Gender":"Male", "HeightCm": 171, "WeightKg": 96},
{"Gender":"Male", "HeightCm": 161, "WeightKg": 85},
{"Gender":"Male", "HeightCm": 180, "WeightKg": 77},
{"Gender":"Female", "HeightCm": 166, "WeightKg": 62},
{"Gender":"Female", "HeightCm": 150, "WeightKg": 70},
{"Gender":"Female", "HeightCm": 167, "WeightKg": 82}]

print(data)
data2 = pd.DataFrame(data)
print(data2)

data2['HeightM'] = data2.HeightCm/100
data2['BMI'] = data2.WeightKg/data2.HeightM**2
print(data2)

bmi_cat = []
for i in data2['BMI']:
	if i < 18.4: bmi_cat.append('Underweight')
	elif i < 24.9: bmi_cat.append('Normal weight')
	elif i < 29.9: bmi_cat.append('Overweight')
	elif i < 34.9: bmi_cat.append('Moderately obese')
	elif i < 39.9: bmi_cat.append('Severaly obese')

	else: bmi.cat.append('Very severely obese')

h_risk = []
for i in data2['BMI']:
	if i < 18.4: h_risk.append('Malnutritian risk')
	elif i < 24.9: h_risk.append('Low risk')
	elif i < 29.9: h_risk.append('Enhanced risk')
	elif i < 34.9: h_risk.append('Medium risk')
	elif i < 39.9: h_risk.append('High risk')

	else: h_risk.append('Very high risk')

data2['BMI_Category'] = bmi_cat
data2['Healt risk'] = h_risk
print(data2)

### 2 ###

N_OW = data2["BMI_Category"][data2.BMI_Category=='Overweight'].count()
print(data2.groupby(['BMI_Category'])['BMI_Category'].count()) # There is one Overweight
print('\nThe total of person with Overweight are: ',N_OW)


