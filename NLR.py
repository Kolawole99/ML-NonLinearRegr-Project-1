#=========================================IMPORTS========================================
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline #needed in jupyter 
import pandas as pd



#===========================================DATA=======================================
df = pd.read_csv('china_gdp.csv')
print(df.head(10))  





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