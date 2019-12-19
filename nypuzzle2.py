from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from datetime import datetime
import os
import subprocess
import time
from selenium.webdriver.common.keys import Keys


def get_puzzle_information(file_dir, url="https://www.nytimes.com/crosswords/game/mini"):
    # opening a file for the current puzzle information
    file = open(file_dir, "w+", encoding="utf-8")

    # getting reveals and puzzle canvas
    options = Options()
    options.headless = True
    options.add_argument("--mute-audio")
    options.add_argument("--disable-gpu")
    # options=options
    driver = webdriver.Chrome()
    driver.get('https://www.nytimes.com/crosswords/game/mini')
    # browser = webdriver.Chrome()
    print("Current Page Title is : %s" % driver.title)
    print("Retrieving the puzzle data")
    # time.sleep(2)
    driver.find_element_by_class_name('buttons-modalButton--1REsR').click()
    # time.sleep(2)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]").click()
    # time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/ul/li[3]").click()
    # time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div[2]/article/div[2]/button[2]").click()
    # time.sleep(2)

    hint_list = {}  # fill later
    keywords = ("Across", "Down")
    index = 0
    prev_no = 0
    clues = driver.find_elements_by_class_name("Clue-text--3lZl7")
    numbers = driver.find_elements_by_class_name("Clue-label--2IdMY")
    for number, clue in zip(numbers, clues):
        no = number.get_property("textContent")
        content = clue.get_property("textContent")
        if (int(no) < prev_no):
            index = 1
        s = keywords[index] + ":\t" + no + " " + content + "\n"
        file.write(s)
        prev_no = int(no)

    reveals = {}
    for i in range(25):
        reveal = driver.find_element_by_id("cell-id-{i}".format(i=i))
        reveal_sibs = reveal.get_property("parentNode").get_property("childElementCount")
        if reveal_sibs == 1:
            s = str(i + 1) + ":\tblack" + "\n"
            file.write(s)
            reveals[i + 1] = "black"
        elif reveal_sibs == 3:
            value = reveal.get_property("parentNode").get_property("childNodes")[1].get_property("textContent")
            s = str(i + 1) + ":\twhite " + value + "\n"
            file.write(s)
            reveals[i + 1] = ("white", value)
        elif reveal_sibs == 4:
            number = reveal.get_property("parentNode").get_property("childNodes")[1].get_property("textContent")
            value = reveal.get_property("parentNode").get_property("childNodes")[2].get_property("textContent")
            s = str(i + 1) + ":\twhite " + value + " " + number + "\n"
            file.write(s)
            reveals[i + 1] = ("white", number, value)
    file.close()
    print(".txt file created!")

    return hint_list, reveals


def init():
    now = datetime.now()
    desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
    fileStr = os.path.join(desktopPath, "Puzzle-{month}-{day}.txt".format(month=now.month, day=now.day))
    values = get_puzzle_information(fileStr)

    return values


def words():
    now = datetime.now()
    desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
    fileName = os.path.join(desktopPath, "Puzzle-{month}-{day}.txt".format(month=now.month, day=now.day))
    file = open(fileName, "r", encoding="utf-8")
    letterArr = []
    count = 0
    for line in file:
        count += 1
        if (str(line[0]).isdigit()):
            if (line[3] == 'w'):
                letterArr.append("0{count}-{data}".format(count=count - 10, data=line[9]))
            elif (line[4] == 'w'):
                letterArr.append("{count}-{data}".format(count=count - 10, data=line[10]))
            elif (count - 10 > 9):
                letterArr.append("{count}-{data}".format(count=count - 10, data=' '))
            else:
                letterArr.append("0{count}-{data}".format(count=count - 10, data=' '))
    wordArr = []
    word = ""
    for y in range(1, 6):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(6, 11):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(11, 16):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(16, 21):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(21, 26):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(1, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(2, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(3, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(4, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(5, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    return wordArr


def get_chrome_driver():
    options = Options()
    #options.headless = True
    options.add_argument("--mute-audio")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-GB")
    options.add_argument("log-level=2")
    #options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    return driver


def connect_to_google(driver):
    driver.get("https://www.google.com/")


def search_google(search_key, driver):
    text_field = driver.find_element_by_css_selector(".gLFyf.gsfi")
    text_field.clear()
    text_field.send_keys(search_key + " meaning")
    text_field.send_keys(Keys.ENTER)
    search_list = []

    # getting the first dictionary meaning from google
    meanings = driver.find_elements_by_css_selector('.QIclbb.XpoqFe span')
    if (len(meanings) != 0):
        res_str = ""
        for x in range(0, len(meanings)):

            res_str += " " + meanings[x].text
        #return meanings[0].text
        return res_str


def connect_to_thesaurus(driver):
    driver.get("https://www.thesaurus.com/")


def search_thesaurus(search_key, driver):
    text_field = driver.find_element_by_id("searchbar_input")
    submit_button = driver.find_element_by_id("search-submit")
    text_field.clear()
    text_field.send_keys(search_key)
    submit_button.click()

    thesaurus = driver.find_elements_by_css_selector(".css-u7frk4.e9i53te8")
    print(len(thesaurus))
    if (len(thesaurus) != 0):
        strong = thesaurus[0].find_element_by_tag_name("strong")
        return strong.getAttribute("innerText")


def main():
    #desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
    #fileString = os.path.join(desktopPath, "outputFile.txt")
    fileString = os.path.join("outputFile.txt")
    file2 = open(fileString, "w+", encoding="utf-8")

    init()
    word = words()
    synonyms = []
    driver1 = get_chrome_driver()
    connect_to_google(driver1)
    for x in range(0, 10):
        synonyms.append((search_google(word[x], driver1)))
        try:
            """
            synonym_sentences = synonyms[x].split('.')
            min_syn_len = len(synonym_sentences[0])
            shortest_synonym = synonym_sentences[0]
            for sentence in synonym_sentences:
                if len(sentence) < min_syn_len and len(sentence) > 0:
                    shortest_synonym = sentence
                    break
            s = str(word[x]) + ":\t" + shortest_synonym + "\n"
            """
            s = str(word[x]) + ":\t" + synonyms[x].split('.')[0] + ".\n"
            file2.write(s)
        except Exception as e:
            print(e)



    # connect_to_thesaurus(driver1)
    # for x in range (0,10):
    #     print(search_thesaurus(word[x], driver1))
    #     time.sleep(3)


    proc = subprocess.Popen(['javac', 'fetchData.java'])
    proc = subprocess.Popen(['javac', 'Grid.java'])
    subprocess.Popen('java Grid')


if __name__ == '__main__':
    main()
