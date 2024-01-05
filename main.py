#code was updated by NotBeexoul ## instagram @not_beexoul ##

from bs4 import BeautifulSoup
import requests
import random

VERSE_RANGES = {
    1: 47, 2: 72, 3: 43, 4: 42, 5: 29,
    6: 47, 7: 30, 8: 28, 9: 34, 10: 42,
    11: 55, 12: 20, 13: 35, 14: 27, 15: 20,
    16: 24, 17: 28, 18: 78
}

def get_verse_numbers(chapter):
    return random.randint(1, VERSE_RANGES.get(chapter, 1))

def random_chapter_verse():
    chapter = random.randint(1, 18)
    verse = get_verse_numbers(chapter)
    return chapter, verse

def generate_link(chapter, verse):
    return f"https://www.holy-bhagavad-gita.org/chapter/{chapter}/verse/{verse}"

def main():
    chapter, verse = random_chapter_verse()
    link = generate_link(chapter, verse)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    transliteration_wo_dia = soup.find("div", {"id": "transliteration_wo_dia"})
    formatted_transliteration = ""
    if transliteration_wo_dia:
        paragraphs = transliteration_wo_dia.find_all("p")
        formatted_transliteration = "\n".join(paragraph.text.strip() for paragraph in paragraphs)

    print(f"# Gita Shlok from chapter {chapter}, verse {verse}.\n")
    print(formatted_transliteration)

if __name__ == '__main__':
    main()
