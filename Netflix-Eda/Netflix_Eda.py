# Exploratory Data Analysis on Netflix Data

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# import dataset
data  = pd.read_csv("C:\\Users\\Acer\\Documents\\netflix_titles.csv")

# data columns information
data.columns

# Top rows of data 
data.head()

# all information of data
data.info()

# Creating function to get all basic information
def all(data):
    print("Total number of show and movies: ",data.shape[0])
    print("data set variable: ",data.shape[1])
    print("-"*60)
    print("Data type of each variable(column): ",data.dtypes)
all(data)

# missing value in each column
print("missing value in each column: ",data.isna().sum())

# deleting unwanted column from data
data = data.drop('show_id',axis =1)

# find duplicate data
dupli = data.duplicated(["title","type",'country','release_year'])
data[dupli]
# droping duplicate data
data = data.drop_duplicates(["title","type",'country','release_year'])

# filling missing value of rating column by mode
data['rating'] = data['rating'].fillna(data['rating'].mode()[0])

# filling missing value of data_added column by mode of year
data['date_added'] = data['date_added'].fillna('january 1, {}'.format(str(data['release_year'].mode()[0]
                                                                          
# replacing all null values 
data.director.fillna("No Director", inplace=True)
data.cast.fillna("No cast",inplace =True)
data.country.fillna("No country",inplace = True)  
                                                                          
# now we don't have missing value in given data
data.isnull().sum()
                                                                          
#As we know about rating colum "UR" and "NR" both are same so we will change it and keep NR only
 for i in data.index:
    if data.loc[i,"rating"] == "UR":
        data.loc[i,"rating"] = "NR"

# Movie and Tv Show frequency by ploting Pie chart
plt.figure(figsize=(12,8))
data['type'].value_counts().plot(kind='pie')
                                                                          
# Distribution of rating categories
sns.set(style='whitegrid')
plt.figure(figsize=(12,8))
sns.countplot(x="rating",data= data)
plt.title("Distribution of rating categories")
plt.xlabel("Rating")
plt.ylabel("Frequency")
                                                                          
# Distribution of rating categories based on type
sns.set(style='whitegrid')
plt.figure(figsize =(12,8))
sns.countplot(x ="rating",hue = "type",data=data)
plt.title("comparing frequecy between type and rating")
                                                                          
 # productive countries in ascending order
data["country"].value_counts().sort_values(ascending =False).head(10)
                                                                          
# extracting the top productive countries in another dataframe
top_productive_countries = data[(data["country"]== "United States") |(data["country"]== "India")|
                               (data["country"]== "United Kingdom")|(data["country"]== "Japan")|(data["country"]== "Canada")|
                               (data["country"]== "South Korea")]
plt.figure(figsize=(12,9))
sns.countplot(x="country",hue ="type",data=top_productive_countries)
plt.title("Comparing between the types of top productive countries")
                                                                          
# yearwise Tvshow and  Movie productions
data1 = data.groupby("release_year")['type'].value_counts()
data1
                                                                          
# top 20 Genres on netflix
filtered_genres = data.set_index('title').listed_in.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
plt.figure(figsize=(12,9))
g = sns.countplot(y = filtered_genres, order=filtered_genres.value_counts().index[:20])
plt.title('Top 20 Genres on Netflix')
plt.xlabel('Titles')
plt.ylabel('Genres')
plt.show()
                                                                          
# datatype of date_added
type(data.date_added[0])
                                                                          
 # converting date_added which is str data type in date data type
data['date_added'] = pd.to_datetime(data['date_added'])
type(data.date_added[0])
                                                                          
# extracting Added year and Day of week
data['added_year'] = data['date_added'].apply(lambda time: time.year)
data['Day of Week'] = data['date_added'].apply(lambda time: time.dayofweek)
data.columns
                                                                          
# mapping days of week
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
data['Day of Week'] = data['Day of Week'].map(dmap)
                                                                          
# Frequecy adding  movies and tv show day wise
plt.figure(figsize=(12,9))
data['Day of Week'].value_counts().plot(kind="pie")
                                                                          
# daywise production of movies and Tv show
plt.figure(figsize=(15,9))
sns.countplot(x="Day of Week",hue ="type",data=data)
                                                                          
 # let see in which year more movies added
plt.figure(figsize=(15,9))
sns.countplot(x = "added_year",data=data)
plt.title("Distribution of year added")
plt.show()
                                                                          
 # which Actor have more cast in movies
filtered_cast_movie = data[data.cast != 'No cast'].set_index('title').cast.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13,7))
plt.title('Top 10 Actor Movies Based on The Number of Titles')
sns.countplot(x = filtered_cast_movie, order=filtered_cast_movie.value_counts().index[:10], palette='pastel')
plt.xticks(rotation =45)
plt.show()
                                                                          
plt.show()
                                                                          
                                                                        
