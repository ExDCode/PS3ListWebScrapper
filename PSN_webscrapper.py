
from bs4 import BeautifulSoup
import requests

#   3 lines to find number of pages to go through
html_text = requests.get('https://dlpsgame.org/category/ps3/page/3/').text
soup = BeautifulSoup(html_text, 'lxml')
numberOfPages = int(soup.find_all(attrs={"class": "pages"})[0].string[-3:])

#Write all the data into a local file
with open('ListOfPS3Games.txt', 'w') as file:
    for page in range(numberOfPages+1):
        #Requesting pages from 1 to "page range"
        html_text = requests.get('https://dlpsgame.org/category/ps3/page/' + str(page) +'/').text
        soup = BeautifulSoup(html_text, 'lxml')

        #Find the all the elements with game links
        gameLinkSoup = soup.find_all(attrs = {"class" : "post bar hentry"})

        #Go over all of the games on the page
        for i in range(len(gameLinkSoup)):
            #This variable contains a extracted link of the game's poster image
            imagePosterURL = gameLinkSoup[i].find_all('img')[0]['src']

            #Write into a file a name of the game || a link to it || a link to the image Poster
            try:    #in case some weird names pop up, we can bypass it
                file.write(gameLinkSoup[i].h2.a.string)
                file.write(" || " + gameLinkSoup[i].h2.a['href'] + " || ")
                file.write(imagePosterURL + "\n")
            except:
                #Takes a link and extracts the name straight from it
                file.write(str(gameLinkSoup[i].h2.a['href']).rsplit("/")[-2])
                file.write(" || " + gameLinkSoup[i].h2.a['href'] + " || ")
                file.write(imagePosterURL + "\n")

