"""
This script web scrapes 100 Greatest of All Time English Movie from the website Empireonline
(https://www.empireonline.com/movies/features/best-movies-2/) saves the output to a text file.
"""

from bs4 import BeautifulSoup
import requests
import json
import re
import ftfy


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.content

soup = BeautifulSoup(movies, "html.parser")
# in this case, the data in the webpage is probably generated using javascript, so usual
# way of web scrapping isn't working like the way we do using selector (class or id)
# so we r loading the whole json object from this specific id #__NEXT_DATA__
data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])


def find_images_key(data: dict):
    """
    this is a generator funcion which recieves a python dictionary object and 
    yields the value of specific key "titleText" from that dictionary.

    Here data is the dict object that we got from the webpage
    """
    if isinstance(data, dict):
        if "__typename" in data and "titleText" in data:
            yield data.get("titleText")
        else:
            for k, v in data.items():
                yield from find_images_key(v)
    elif isinstance(data, list):
        for i in data:
            yield from find_images_key(i)


gen = find_images_key(data) # creating generator object
next(gen) # skips the 1st titleText since it is repeated

movie_list = []
for a in gen:
    movie_list.append(re.sub("\d+[\):] ", "", a)) # strip off the ranking numbers from the title
    if len(movie_list) == 100:
        break # for avoiding repeatation
    
# writng the movie name in a text file
with open("greatest_movie_of_all_time.txt", "w", encoding="utf-8") as file:
    row = 0
    for movie in movie_list[::-1]:
        movie = ftfy.fix_text(movie) # correctly convert the unicode character for example: 85) Léon
        ranked = f"{row + 1}) {movie}\n" # adding the ranking from top 1 to 100
        file.write(ranked)
        row += 1



# --------------------------------------- EXTRA --------------------------------------
# saving the output in a file to explore the content since the output is too large to 
# serach in the command
# with open('json.txt', "w") as f:
#     print(json.dumps(data, indent=4), file=f)

# this function works but it does not scrapes from the right place. So theres some 
# discrepency in the ouput

# def find_title(data):
#     if isinstance(data, dict):
#         for k, v in data.items():
#             if k.startswith("ImageMeta:"):
#                 yield v.get("titleText")
#             else:
#                 yield from find_title(v)
#     elif isinstance(data, list):
#         for i in  data:
#             yield from find_title(i)


# for a in find_title(data):
#     print(a)



