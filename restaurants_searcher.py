import csv
import json
import requests


def write_date_to_csv():
    restaurants = "[]"
    response = "hugahuga"
    if "error" in response["results"]:
       return print("エラーが発生しました！")
    for restaurant in response["rest"]:
        restaurant_name = restaurant["name"]
        restaurants.append(restaurant_name)
            
    return print(restaurants)
    
write_date_to_csv()
