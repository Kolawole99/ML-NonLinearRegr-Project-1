#=========================================IMPORTS========================================
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline #needed in jupyter 
import pandas as pd
from scipy.optimize import curve_fit



#===========================================DATA=======================================
df = pd.read_csv('china_gdp.csv')
print(df.head(10))  



#==================================PLOTTING THE DATASET==================================
plt.figure(figsize=(8,5))
x_data, y_data = (df["Year"].values, df["Value"].values)
plt.plot(x_data, y_data, 'ro')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()



#======================================CHOOSING A MODEL===================================
#We choose a sigmoid or logistic curve to train the model because of its shape.
def sigmoid(x, Beta_1, Beta_2):
     y = 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))
     return y

#Lets look at a sample sigmoid line that might fit with the data:
beta_1 = 0.10
beta_2 = 1990.0
#logistic function
Y_pred = sigmoid(x_data, beta_1 , beta_2)
#plot initial prediction against datapoints
plt.plot(x_data, Y_pred*15000000000000.)
plt.plot(x_data, y_data, 'ro')
plt.show()


# Lets normalize our data to be able to find the best parameters to fit the data with
xdata =x_data/max(x_data)
ydata =y_data/max(y_data)
#use curve_fit to find the best line thast fits the data well
popt, pcov = curve_fit(sigmoid, xdata, ydata)
#print the final parameters
print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))
#we plot our optimized data and fitted line
x = np.linspace(1960, 2015, 55)
x = x/max(x)
plt.figure(figsize=(8,5))
y = sigmoid(x, *popt)
plt.plot(xdata, ydata, 'ro', label='data')
plt.plot(x,y, linewidth=3.0, label='fit')
plt.legend(loc='best')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()



#=========================================EVALUATE ACCURACY=================================
# split data into train/test
msk = np.random.rand(len(df)) < 0.8
train_x = xdata[msk]
test_x = xdata[~msk]
train_y = ydata[msk]
test_y = ydata[~msk]

# build the model using train set
popt, pcov = curve_fit(sigmoid, train_x, train_y)

# predict using test set
y_hat = sigmoid(test_x, *popt)

# evaluation
print("Mean absolute error: %.2f" % np.mean(np.absolute(y_hat - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((y_hat - test_y) ** 2))
from sklearn.metrics import r2_score
print("R2-score: %.2f" % r2_score(y_hat , test_y) )








#===============================TYPES OF NON LINEAR REGRESSION=================================
# Cubic
# x = np.arange(-5.0, 5.0, 0.1)
# #You can adjust the slope and intercept to verify the changes in the graph
# y = 1*(x**3) + 1*(x**2) + 1*x + 3
# y_noise = 20 * np.random.normal(size=x.size)
# ydata = y + y_noise
# plt.plot(x, ydata,  'bo')
# plt.plot(x,y, 'r') 
# plt.ylabel('Dependent Variable')
# plt.xlabel('Indepdendent Variable')
# plt.show()


# Quadratic 𝑌=𝑋2
# x = np.arange(-5.0, 5.0, 0.1)
# #You can adjust the slope and intercept to verify the changes in the graph
# y = np.power(x,2)
# y_noise = 2 * np.random.normal(size=x.size)
# ydata = y + y_noise
# plt.plot(x, ydata,  'bo')
# plt.plot(x,y, 'r') 
# plt.ylabel('Dependent Variable')
# plt.xlabel('Indepdendent Variable')
# plt.show()


# Exponential 𝑌=𝑎+𝑏𝑐𝑋
# X = np.arange(-5.0, 5.0, 0.1)
# ##You can adjust the slope and intercept to verify the changes in the graph
# Y= np.exp(X)
# plt.plot(X,Y) 
# plt.ylabel('Dependent Variable')
# plt.xlabel('Indepdendent Variable')
# plt.show()



# Logarithmic 𝑦=log(𝑥) or 𝑦=log(𝑋)
# X = np.arange(-5.0, 5.0, 0.1)
# Y = np.log(X)
# plt.plot(X,Y) 
# plt.ylabel('Dependent Variable')
# plt.xlabel('Indepdendent Variable')
# plt.show()



# Sigmoidal/Logistic 𝑌=𝑎+𝑏1+𝑐(𝑋−𝑑) 
# X = np.arange(-5.0, 5.0, 0.1)
# Y = 1-4/(1+np.power(3, X-2))
# plt.plot(X,Y) 
# plt.ylabel('Dependent Variable')
# plt.xlabel('Indepdendent Variable')
# plt.show()

"""
Pure plot of the Logistic function
    X = np.arange(-5.0, 5.0, 0.1)
    Y = 1.0 / (1.0 + np.exp(-X))

    plt.plot(X,Y) 
    plt.ylabel('Dependent Variable')
    plt.xlabel('Indepdendent Variable')
    plt.show()
"""