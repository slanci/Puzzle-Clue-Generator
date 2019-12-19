from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from datetime import datetime
import os
import subprocess
import time
from selenium.webdriver.common.keys import Keys
import wordninja


def init():
    now = datetime.now()
    desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
    fileStr = os.path.join(desktopPath, "Puzzle-{month}-{day}.txt".format(month=now.month, day=now.day))
    values = get_puzzle_information(fileStr)

    return values


def getGoogle(driver):
    driver.get("https://www.google.com/")


def getWordnet(driver):
    driver.get("http://wordnetweb.princeton.edu/perl/webwn")


def getThesaurus(driver):
    driver.get("https://www.thesaurus.com/")


def GetMerriam(driver):
    driver.get("https://www.merriam-webster.com/")


def get_chrome_driver():
    options = Options()
    options.add_argument("--mute-audio")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-GB")
    options.add_argument("log-level=2")
    driver = webdriver.Chrome(options=options)
    return driver


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
    time.sleep(2)
    driver.find_element_by_class_name('buttons-modalButton--1REsR').click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/ul/li[3]").click()
    time.sleep(2)
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


def googleSearch(word, driver):
    text_field = driver.find_element_by_css_selector(".gLFyf.gsfi")
    text_field.clear()
    text_field.send_keys(word + " meaning")
    text_field.send_keys(Keys.ENTER)
    search_list = []

    # getting the first dictionary meaning from google
    try:
        element = driver.find_element_by_css_selector('.mQo3nc.hsL7ld')
        driver.execute_script("""
            var element = arguments[0];
            element.innerHTML = "";
            """, element)
    except Exception as e:
        pass

    meanings = driver.find_elements_by_css_selector('.QIclbb.XpoqFe span')
    if (len(meanings) != 0):
        res_str = ""
        for x in range(0, len(meanings)):
            #print(meanings[x].get_attribute("class"))
            try:
                temp_str = meanings[x].text
                res_str += "" + temp_str[:1].upper() + temp_str[1:]
            except Exception as e:
                pass
        # return meanings[0].text
        return res_str


def wordnetSearch(word, driver):
    text_field = driver.find_element_by_name("s")
    submit_button = driver.find_element_by_name("sub")
    text_field.clear()
    text_field.send_keys(word)
    submit_button.click()

    search_list = []

    all_ul = driver.find_elements_by_tag_name("ul")
    for ul in all_ul:
        # priority_li = []
        all_li = ul.find_elements_by_tag_name("li")
        for li in all_li:
            text = li.get_attribute("innerText")
            ## Substring -> whether it is a verb or noun
            firstLP = text.index("(")
            firstRP = text.index(")")

            ## Substring -> find what it means
            secondLP = text.index("(", firstLP + 1)
            secondRP = text.rindex(")", firstRP + 1)

            ## If the search key doesn't exist as part of the found words, skip
            loc = text[firstRP + 1:secondLP].lower().find(word)
            if (loc == -1):
                continue

            ## If the search key is not contained in the result, return it
            if (text[secondLP + 1:secondRP].find(word) == -1):
                search_list.append(text[secondLP + 1:secondRP])
                # priority_li.append(loc)
    if (len(search_list) != 0):
        return search_list[0]


# def thesaurusSearch(word, driver):
#     text_field = driver.find_element_by_id("searchbar_input")
#     submit_button = driver.find_element_by_id("search-submit")
#     text_field.clear()
#     text_field.send_keys(word)
#     submit_button.click()
#
#     search_list = []
#
#     a = driver.find_elements_by_css_selector(".css-1twju98.e9i53te7")
#     if (len(a) != 0):
#         em = a[0].find_element_by_tag_name("em")
#         if (em.get_attribute("innerText") == "as in"):
#             strong = a[0].find_element_by_tag_name("strong")
#             search_list.append("as in '" + strong.get_attribute("innerText") + "'")
#     return search_list


def merriamSearch(word, driver):
    text_field = driver.find_element_by_id("s-term")
    text_field.clear()
    text_field.send_keys(word)
    text_field.send_keys(Keys.ENTER)

    search_list = []
    beginning = ""
    plural = ""

    changed = driver.find_elements_by_class_name("hword")
    alternatives = driver.find_elements_by_class_name("vg-ins")

    ## check if search key was changed by the dictionary
    if (len(changed) != 0):
        if (word != changed[0]):
            if (len(alternatives) != 0):
                if (word == "media"):
                    return search_list
                if (word not in alternatives[0].get_attribute("innerText")):
                    return search_list

    # check if it is plural
    if (len(alternatives) != 0):
        pl = alternatives[0].find_elements_by_css_selector(".il.plural")
        ifs = alternatives[0].find_elements_by_css_selector(".if")

        if (len(pl) != 0):
            if (len(ifs) != 0):
                if (ifs[0].get_attribute("innerText").lower() != word.lower()):
                    if (re.search(r"plural", pl[0].get_attribute("innerText"))):
                        plural = "Plural"

    # check if the search key is from a foreign language etc
    form = driver.find_elements_by_class_name("fl")
    if (len(form) != 0):
        beginning = form[0].get_attribute("innerText").strip()

    results = driver.find_elements_by_class_name("dtText")
    for result in results:
        # find the size of children (the text content is separated among them)
        children_size = driver.execute_script("return arguments[0].childNodes.length", result)

        # if there are more than 1 child, take the contents of #text
        # else, get the contents of the first child
        text = driver.execute_script(
            'str = ""; arguments[0].childNodes.forEach( (item) => { if (item.nodeName != "SPAN" && item.nodeName != "STRONG" && item.nodeName != "P") { str = str + item.textContent; } } ); return str;',
            result).strip()

        if (text != ""):
            if (text[0] == ";"):
                text = text[2:]

            if (beginning != "" and re.search(r"\bnoun\b", beginning) == None and re.search(r"\bverb\b",
                                                                                            beginning) == None and re.search(
                    r"\binterjection\b", beginning) == None):
                text = beginning + ", " + text

            if (plural != ""):
                text = plural + ", " + text

            # print(text)
            search_list.append(text)

    if (word == "clark"):
        search_list.pop(0)
        search_list.pop(0)
    if (len(search_list) != 0):
        return search_list[0]


def searchAll(word):
    desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
    fileString = os.path.join(desktopPath, "outputFile.txt")
    fileString = os.path.join("outputFile.txt")
    file2 = open(fileString, "w+", encoding="utf-8")

    browser = get_chrome_driver()
    synonyms = []
    getGoogle(browser)

    # getThesaurus(browser3)

    for x in range(0, 10):
        synonyms.append((googleSearch(word[x], browser)))
        try:
            """
            synonym_sentences = synonyms[x].split('.')
            min_syn_len = len(synonym_sentences[0])
            shortest_synonym = synonym_sentences[0]
            for sentence in synonym_sentences:
                if len(sentence) < min_syn_len and len(sentence) > 0:
                    shortest_synonym = sentence
                    break
            synonyms[x] = str(x+1)+". "+ str(word[x]) + ":\t" + shortest_synonym + "\n"
            """
            synonyms[x] = str(x + 1) + ". " + str(word[x]) + ":\t" + synonyms[x].split('.')[0][:1].upper() + synonyms[x].split('.')[0][1:]+ ".\n"
        except Exception as e:
            print(e)
    for y in range(0, 10):
        try:
            if (synonyms[y] is None):
                GetMerriam(browser)
                synonyms[y] = merriamSearch(word[y], browser)
                if (not (synonyms[y] is None)):
                    synonyms[y] = str(y + 1) + ". " + str(word[y]) + ":\t" + synonyms[y][:1].upper() + synonyms[y][1:] + ".\n"
            if (synonyms[y] is None):
                getWordnet(browser)
                synonyms[y] = wordnetSearch(word[y], browser)
                if (not (synonyms[y] is None)):
                    synonyms[y] = str(y + 1) + ". " + str(word[y]) + ":\t" + synonyms[y][:1].upper() + synonyms[y][1:] + ".\n"
        except Exception as e:
            pass

    for z in range(0, 10):
        if (not (synonyms[z] is None)):
            try:
                file2.write(synonyms[z])
            except Exception as e:
                pass


def display():
    proc = subprocess.Popen(['javac', 'fetchData.java'])
    proc = subprocess.Popen(['javac', 'Grid.java'])
    subprocess.Popen('java Grid')


def main():
    init()
    word = words()
    searchAll(word)
    display()


if __name__ == '__main__':
    main()
