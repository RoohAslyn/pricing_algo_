# Pricing Algo Using ML

Building an ML Pricing Algorithm in Python/Django like this:

## Features


## Part 1 - Find lowest local price
1. Get the name, address, open/close times, menu items, and prices for Village restaurant:   https://www.yelp.com/biz/village-the-soul-of-india-hicksville
2. Find top-rated 5 restaurants within 2 km serving similar items on their menu (using Yelp or Google Maps.)
3. List their menu items and prices
4. Find the lowest price of each item that Village restaurant could set based on that.

##  Part 2 - Adjust prices in busy times and bad weather
5. Get Village busy times from GMaps:  https://maps.app.goo.gl/AbLBny2kZBek65Xm7
6. Get the current temperature and rain near Village using:  https://openweathermap.org/current

### Show the Village menu with the final predicted prices for each item using any ML algorithm as follows:

-- IF
7.1 The temperature is below 45 degrees Fahrenheit (note that the API returns data in Kelvin, so you will have to convert)
7.2 There is either a chance of moderate or heavier rain or snow
7.3 Village is busier than usual
-- THEN
Price should be higher than the lowest competitive price
-- ELSE
Price should be lowest competitive price

## Installation
-Navigate to the project directory in your terminal:
     cd pricing_demo

-Run the server: python manage.py runserver 

 -Visit the following endpoint in your browser: http://127.0.0.1:8000/api/adjust-prices/
