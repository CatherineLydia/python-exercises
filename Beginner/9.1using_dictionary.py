test_dict={
    "Key1":"Value1",
    "Key2":"Value2",
    "Key3":"Value3",
}
print(test_dict["Key1"])

# print(test_dict["Key4"])  #Key Error
#print(test_dict[Key4])  #Data type Error

#Adding new items to dictionary
test_dict["Key4"]="Value4"
print(test_dict)

#EMPTY DICTIONARY
new_dict={}

#Wipe an existing dictionary
# test_dict={}
# print(test_dict)

# Edit an item in dictionary
test_dict["Key1"]="New Value1"
print(test_dict)

# Loop through a dictionary
for key in test_dict:
    print(key)
    print(test_dict[key])

# Nesting

capitals={
    "France":"Paris",
    "Germany":"Berlin"
}

# Nesting a list in a dictionary
travel_log={
    "France":["Paris","Little","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}

# Nesting a dictionary in a dictionary
new_travel_log={
    "France":{
        "cities_visited": ["Paris", "Little", "Dijon"],
        "total_visits":10
    }
}

# Nesting dictionary in a list
travel_log_list=[
        {"country":"France",
        "cities_visited":["Paris", "Little", "Dijon"],
        "total_visits":10
        },
        {"country": "Germany",
        "cities_visited": ["Paris", "Little", "Dijon"],
        "total_visits":10
        }
]
print(travel_log_list)
