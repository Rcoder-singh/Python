travel_log =[
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris","Lille","Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin","Hamburg","Stuttgart"]
    },
]
# 🚨 Don't change the code above 👆

#TODO: Write the function that will allow new country
#to be added to thr travel_log.
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

# 🚨 Don't change the code below 👇
add_new_country("Russia",2, ["Moscow","Saint Petersburg"])
print(travel_log)