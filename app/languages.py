import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_programming_languages"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

# Find all list items with language names
language_items = soup.find_all("li")  # Target all <li> tags

# Extract language names
programming_languages = [item.text.strip() for item in language_items]  # Remove whitespaces

programming_languages = programming_languages[124:814]

# for language in programming_languages:
#     print(language)

temp_lang_list=[]
languages_dict={}

for language in range(len(programming_languages)):
    if programming_languages[language][1:]==programming_languages[language+1][1:]:
        temp_lang_list.append(programming_languages[language])
    else:
        " implement line 31 logic "
    pass

'''
language_dict={
    'A': [''],
    'B': ['B','Babbage','Ballerina','Bash','BASIC','Batch file','bc','BCPL','BeanShell','BETA','BLISS','Blocky','BlooP','Boo','Boomerang','Bosque'],
    'C': []
}
'''