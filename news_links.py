# A library that allows us to request & get the content from the website.
import requests 
# A library that allows us to find the links of the website.
from bs4 import BeautifulSoup

# Create the variable URL
url = "https://news.ycombinator.com/news"

# Create an empty list links to store links
links = []
# Use the request library to get the content & store that into a variable response
response = requests.get(url)
# Create a new variable website text
website_text = response.text
# Run text through the BeautifulSoup library & store the output in a variable bsoup
bsoup = BeautifulSoup(website_text, features="html.parser")

# Create for loop to retrieve all the href
for link in bsoup.find_all("a"):
    print("\n",link.get("href"), link.get("title"))

# Create an external text file called parsed_data and save to variable file.
file = open("parsed_data.txt", "w")
for link in bsoup.find_all("a"):
    bsoup_link = link.get("href")
    file.write(bsoup_link)
    file.write("\n")
file.flush()
file.close()