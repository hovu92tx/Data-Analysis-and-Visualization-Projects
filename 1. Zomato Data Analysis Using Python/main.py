import pandas as pd 
import seaborn as sns
import numpy as np 
from matplotlib import pyplot as plt

def rateHandle(value):
    value = str(value).split('/')[0]
    return float(value)


if __name__ == '__main__':

    # Access data
    df = pd.read_csv('1. Zomato Data Analysis Using Python\Zomato data .csv')
    # Remove '/' from rate value
    df['rate'] = df['rate'].apply(rateHandle)
    # Explore data structure
    print(df.head())
    print('*'*80)
    # Check Null/Empty values in the dataframe
    df.info()

    print('*'*80)
    # Count Restaurant based on type.
    sns.countplot(x=df['listed_in(type)'])
    plt.xlabel('Type of restaurant')
    # plt.savefig('1. Zomato Data Analysis Using Python\graphs\listed_in(type) count.jpg')
    plt.show()
    # Conclusion: The majority of the restaurants fall into the dining category.

    #Visualize Type of restaurant based on Votes
    type_vote_group = df.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes':type_vote_group})
    plt.figure(figsize=(10,6))
    plt.plot(result, c='red', marker='o')
    plt.xlabel('type of restauant', c='green', size =20)
    plt.ylabel('Votes', c='red', size=20) 
    # plt.savefig('1. Zomato Data Analysis Using Python\graphs\Type_Votes_graph.jpg')
    plt.show()
    #Conclusion: Dining restaurants are preferred by a larger number of individuals.

    # Determine the restaurant’s name that received the most votes
    restaurant = df.loc[df['votes']==df['votes'].max(), 'name']
    print("Restaurant(s) with the most votes:", restaurant," Number of Votes: ", df['votes'].max())
    
    # Explore online_order column
    plt.figure(figsize=(10,6))
    sns.countplot(x = df['online_order'])
    plt.xlabel('Online Order',c='red', size=20)
    plt.ylabel('Counts', c= 'red', size=20)
    # plt.savefig('1. Zomato Data Analysis Using Python\graphs\online_order_column.jpg')
    plt.show()
    # Conclusion: This suggests that a majority of the restaurants do not accept online orders.

    # Explore the rate column
    plt.figure(figsize=(10,6))
    plt.hist(df['rate'], bins=5)
    plt.title('Ratings Distribution')
    # plt.savefig('1. Zomato Data Analysis Using Python\graphs\explore_rate_column.jpg')
    plt.show()
    # Conclusion: The majority of restaurants received ratings ranging from 3.5 to 4.

    # Explore the approx_cost(for two people) column
    plt.figure(figsize=(10,6))
    sns.countplot(x=df['approx_cost(for two people)'])
    plt.title('Cost for two people')
    plt.savefig('1. Zomato Data Analysis Using Python\graphs\cost_for_two_people.jpg')
    plt.show()
    # Conclusion: The majority of couples prefer restaurants with an approximate cost of 300 rupees.

    # Examine whether online orders receive higher ratings than offline orders
    plt.figure(figsize= (10,6))
    sns.boxplot(x= 'online_order', y = 'rate', data=df)    
    # plt.savefig('1. Zomato Data Analysis Using Python\graphs\online_offline_order_comparation.jpg')
    plt.show()
    # Conclusion: Offline orders received lower ratings in comparison to online orders, which obtained excellent ratings.

    #
    pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
    plt.title("Heatmap")
    plt.xlabel("Online Order")
    plt.ylabel("Listed In (Type)")
    plt.show()
    # Conclusion: Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders. This suggests that clients prefer to place orders in person at restaurants, but prefer online ordering at cafes.
