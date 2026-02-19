# importing necessary modules and functions
from custom_module import generate_time_travel_message as gttm
import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
# variable creation and bulk of processing
time_now = dt.datetime.now()
print("Your most recent date/time group is {}!".format(time_now))
destinations = ['Tokyo','London','New York','Dubai']

# creating travel cost and inflation consideration as years change
travel_cost = Decimal('1002.52')
random_year = randint(1970,2026)
#print("Your current travel cost for the year {} is ${}".format(dt.datetime.now().year,travel_cost))
#print("Target year is: {}".format(random_year))
year_difference = abs(dt.datetime.now().year - random_year)
inflation_factor = Decimal('3.56')
inflation = year_difference * inflation_factor
#print("Your inflation addition is: ${}".format(inflation))
final_cost = travel_cost + inflation
#print("Your final cost for traveling on the year {} is ${}".format(random_year,final_cost))
final_destination = choice(destinations)
#print("Your final destination is: {}".format(final_destination))
# generate_time_travel_message(year, destination, cost)

# using created function to generate the time travel message

gttm(random_year, final_destination, final_cost)
