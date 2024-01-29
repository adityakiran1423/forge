import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_programming_languages"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

# Find all list items with language names
language_items = soup.find_all("li")  # Target all <li> tags

# Extract language names
programming_languages = [item.text.strip() for item in language_items]  # Remove whitespaces

# Extract relevant languages
programming_languages = programming_languages[124:814]

# for number, language in enumerate(programming_languages):
#     print(number+1, language)

# temp_lang_list = []
# languages_dict = {}

# for language in range(len(programming_languages)):
#     if programming_languages[language][1:] == programming_languages[language + 1][1:]:
#         temp_lang_list.append(programming_languages[language])
#     else:
#         "implement line 31 logic"
#     pass
