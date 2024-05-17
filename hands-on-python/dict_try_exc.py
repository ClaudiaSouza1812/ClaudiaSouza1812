

# Create a dictionary with 6 key-value pairs
def main():
    # create a dictionary
    dicts = {
        'name': 'Claudia',
        'age': 'Secret ;)',
        'sign': 'Saggitarious',
        'birth': 'December 18th',
        'city': 'São Paulo',
        'country': 'Brazil',
        'hobby': 'sing',
        'profession': 'software engineer, project developer, project manager',
        'job': 'software engineer',
        'food': 'japanese, italian, brazilian, barbecue, chinese, arabic',
        'color': 'blue, black, magenta, gold, bronze, red, yellow, white',
        'animal': 'dog, owl',
        'car': 'Porche, Mercedes, BMW, Volvo, Audi, Maserati, Jaguar, Land Rover, Tesla',
        'singer': 'Renato Russo, Caetano Veloso',
        'movie': 'Cinema Paradiso',
        'book': 'Sapiens',
        'sport': 'tennis',
        'team': 'São Paulo FC',
        'language': 'Python, C, C#, JavaScrip, HTML, CSS, SQL, Scratch, Portuguese, English, Spanish',
        'drink': 'coffee, beer, wine, water, bayles, amarula, vodka, caipirinha, martini, whisky',
        'dessert': 'ice cream',
        'flower': 'rose',
        'fruit': 'strawberry',
        'number': 7,
        'letter': 'C',
        'day': 'Friday',
        'month': 'July',
        'season': 'summer',
        'continent': 'Europe',
        'planet': 'Earth',
        'element': 'water'}

    # call the key_value function
    key_value(dicts)



# define the function to get the value of a key
def key_value(dic):

    # get the key from the user
    key = input("Enter a key to get to know Claudia better:"'\n')

    # try to get the value of the key
    try:
        # print the value of the key
        print(f"{dic[key]}")
    # handle the KeyError exception
    except KeyError:
        # print a message
        print(f"The key {key} does not exist in the dictionary.")



# call the main function
main()
