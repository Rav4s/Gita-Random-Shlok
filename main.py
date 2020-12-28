from bs4 import BeautifulSoup
import requests
import random

def get_p(transliteration):
    j = 0
    for i in transliteration:
        j = j+1
        i = str(i)
        new_string = i.replace("<p>","").replace("</p>","").replace("<br/>","\n")
        if j == 2:
            return new_string
        else:
            continue

def get_verse_numbers(chapter):
    if chapter == 1:
        verse = random.randint(1, 47)
    elif chapter == 2:
        verse = random.randint(1, 72)
    elif chapter == 3:
        verse = random.randint(1, 43)
    elif chapter == 4:
        verse = random.randint(1, 42)
    elif chapter == 5:
        verse = random.randint(1, 29)
    elif chapter == 6:
        verse = random.randint(1, 47)
    elif chapter == 7:
        verse = random.randint(1, 30)
    elif chapter == 8:
        verse = random.randint(1, 28)
    elif chapter == 9:
        verse = random.randint(1, 34)
    elif chapter == 10:
        verse = random.randint(1, 42)
    elif chapter == 11:
        verse = random.randint(1, 55)
    elif chapter == 12:
        verse = random.randint(1, 20)
    elif chapter == 13:
        verse = random.randint(1, 35)
    elif chapter == 14:
        verse = random.randint(1, 27)
    elif chapter == 15:
        verse = random.randint(1, 20)
    elif chapter == 16:
        verse = random.randint(1, 24)
    elif chapter == 17:
        verse = random.randint(1, 28)
    elif chapter == 18:
        verse = random.randint(1, 78)
    else:
        print("Invalid chapter number. Quitting...")
        quit()
    return verse

def random_chapter_verse():
    chapter = random.randint(1, 18)
    verse = get_verse_numbers(chapter)
    return chapter, verse

def generate_link(chapter, verse):
    link = "https://www.holy-bhagavad-gita.org/chapter/" + str(chapter) + "/verse/" + str(verse)
    return link

def main():
    chapter, verse = random_chapter_verse()
    link = generate_link(chapter, verse)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    transliteration = soup.find("div", {"id": "transliteration"})
    formatted_transliteration = get_p(transliteration)
    print("Gita Shlok from chapter " + str(chapter) + ", verse " + str(verse) + ".")
    print("")
    print(formatted_transliteration)

if __name__ == '__main__':
    main()
