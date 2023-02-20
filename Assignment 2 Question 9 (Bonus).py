#COMPLETED
#TESTED

"""
You can work in groups of 2 (or 3 max), i.e. all students can submit the same code - 
at the top of the code have a comment stating names of all students who worked together.

Write an interesting application using some public APIs. 
The application should be interactive - i.e. gives the user some query options, 
and gives the result of the query after fetching the data using APIs and processing it. 
There should be more than one API call in this application, preferably from 
different base APIs (i.e. APIs from different organizations).

A suggested mini/project - if you have a good working application for this, let the Instructor know 
by email (he wants to use it).
Using the music sites' APIs, develop an application that can get the list of songs that were sung 
by some <singer> whose lyrics were written by some <poet/lyrics_writer>. Either of the fields, if 
not specified, should give songs for all singers/poets. Give this list as a CSV specifying the 
song (generally by its name or the starting lines - whatever the site uses), the singer, the 
lyrics_writers/poet, the year it was sung, and whatever other info is there. (It will be good if 
songs from multiple sites are in this list - will make it more complete.) (It will be nice if you 
can also give a YouTube link for listening/viewing this song).
"""

#collaboration with Surat Sathi Samanta 2022517

import requests

def meme():
    message = input("Enter a subreddit name (or leave it blank to get a random meme): ")
    req = requests.get("https://meme-api.com/gimme/"+message)
    try:
        print(req.json()['preview'][-1])
    except:
        print("Error, meme not found")

def define():   
    message = input("Enter a word to check it's definition: ")
    if message == None:
        print("Please enter a word to be defined.")
    else:
        check_word_validity = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+message)
        if len(check_word_validity.json()) == 3:
            print("Word not valid, try again.")
        else:
            definition_stuff = check_word_validity.json()[0]
            print(f"Word: {definition_stuff['word']}")
            i = 0

            while True:
                try:
                    print(f"Meaning: {definition_stuff['meanings'][i]['definitions'][0]['definition']}\n")
                    i += 1
                except:
                    break
        
def chuck():
    joke = requests.get("https://api.chucknorris.io/jokes/random").json()['value']
    print(joke)

def yt():
    message = input("Enter a search query term: ")
    if message == "":
        print("Please enter something to be searched for.")
    else:
        count = 1
        b = 0
        try:
            count = int(input("How many video results do you want? Enter a number less than 20: "))
        except:
            print("Please enter a valid number.")
            b = 1
        req = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={message}&type=video&key=AIzaSyDpxLwFxhiKNVRbRgID808zGSOv9JnXMmw")
        if b == 0:
            if req.json()['pageInfo']['totalResults'] == 0:
                print("No results found")
            else:
                url = "https://www.youtube.com/watch?v="
                for i in range(count):
                    final = url+req.json()['items'][i]['id']['videoId']
                    print(final)


while True:
    q = input("Enter\n1. To get a meme from reddit using a subreddit\n2. To get a random Chuck Norris joke\n3. To search for videos on youtube\n4. To search for a word definition\n Any other key to exit menu.\n")
    if q == '1':
        meme()
    elif q == '2':
        chuck()
    elif q == '3':
        yt()
    elif q == '4':
        define()
    else:
        break