
# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# import dataset
insurance_data = pd.read_csv('C:\\Users\\Acer\\Downloads\\insurance.csv')

# head of dataset
insurance_data.head()

# information of data
insurance_data.info()

# lets describe the data
insurance_data.describe()

#convert sex column in 0 and 1
def convert_sex(x):
    if x == "male":
        return 1
    if x == "female":
        return 0
  
# column converted in 0 and 1
insurance_data.sex.unique()

#convert smoker column in 0 and 1
def convert_smoker(x):
    if x == "yes":
        return 1
    if x == "no":
        return 0

insurance_data['smoker']=insurance_data['smoker'].apply(convert_smoker)
# let do EDA for getting idea of dataset
# jointplot of bmi and charges
sns.jointplot(x ="bmi",y ='charges',data =insurance_data)

# joinplot of age and charges 
sns.jointplot(x ="age",y ='charges',data =insurance_data)

# pair plot for getting idea of data
sns.pairplot(data=insurance_data)


# distribution plot of charges
sns.distplot(insurance_data['charges'])


# adding dummy variable
insurance_data = pd.get_dummies(insurance_data, prefix_sep='', 
                            columns=['region'])

# data with dummy variable
insurance_data.head()

# Assigning data to regressor (x) and response(y) variable
x = insurance_data[['age','sex','bmi','children','smoker','regionnortheast','regionnorthwest','regionsoutheast']]

y = insurance_data['charges']

# spliting data in training and testing 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y)

# get number of observation in training data testing data
print('number of data in training',x_train.shape[0])
print('number of data in testing',x_test.shape[0])

# import the Regresionmodel and fit the model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

# predictive the data
y_pred = regressor.predict(x_test)

plt.scatter(y_test,y_pred)
plt.xlabel("y_test")
plt.ylabel('y_pred')

# The coefficients
print('Coefficients: \n', regressor.coef_)

# calculate these metrics by hand!
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
print('MSE:', metrics.mean_squared_error(y_test, y_pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# distribution of residual 
sns.distplot((y_test-y_pred),bins=50)

# coeffecients
coeffecients = pd.DataFrame(regressor.coef_,x.columns)
coeffecients.columns = ['Coeffecient']
coeffecients



# Interpreting the coefficients:

# Holding all other features fixed, a 1 unit increase in age is associated with an increase of 268.128362 total charges.
# Holding all other features fixed, a 1 unit increase in sex is associated with an increase of -290.1749688.59 total charges.
# Holding all other features fixed, a 1 unit increase in bmi is associated with an increase of 358.206361 total charges.
# Holding all other features fixed, a 1 unit increase in smoker is associated with an increase of 24266.861719total charges.
# region also play important role in charges northeast and northwest have more charges 

