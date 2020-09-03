destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(dest):
    index = destinations.index(dest)
    return index


# print (get_destination_index("Los Angeles,USA"))
# print (get_destination_index("Paris,France"))

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler[0])

# print (test_destination_index)

# 25
attractions = []
for destination in destinations:
    attractions.append([])


# 26,27

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
    except ValueError:
        print(f"{destination} name is not available")
        return


add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

"""
Write a function called find_attractions() that takes two parameters: destination, 
the name of the destination and interests, a list of interests.
"""


def find_attractions(destination, interests):
    #print(f"we are looking {interests} in {destination}")
    destination_index = get_destination_index(destination)
    #print(destination_index)
    attractions_in_city = attractions[destination_index]
    #print(attractions_in_city)
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attractions = attraction
        attraction_tags = attraction[1]
        #print (f"we got attraction tag as {attraction_tags}")

        for intrest in interests:
            #print(f"User is looking  for {intrest}")
            if intrest in attraction_tags:
                #print(f"appending {possible_attractions[0]}")
                attractions_with_interest.append(possible_attractions[0])
    #print (f"attractions_with_interest --> {attractions_with_interest}")
    return attractions_with_interest


#la_arts = find_attractions('Paris, France', ['monument'])
#print(la_arts)

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    #print(traveler_destination)
    #print (traveler_interests)
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    #print (traveler_attractions)
    interests_string = "Hi "
    interests_string += traveler[0]
    interests_string += ", we think you'll like these places around " + traveler[1]
    for traveler_attraction in traveler_attractions:
        #print (f"traveler_attraction---> {traveler_attraction}")
        interests_string=interests_string + ", " + traveler_attraction + ", "

    return interests_string


smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)




