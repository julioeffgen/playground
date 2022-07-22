import re
from bs4 import BeautifulSoup
import unicodedata


def int_or_text(item):
    try:
        return int(item)
    except:
        return index + 1


f = open('dropdown.html')
soup = BeautifulSoup(f, "html.parser")
f.close()
all_options = soup.find_all('option')

global_messages = list()
enums = list()
index = 0


for option in all_options:
    if option['value']:
        if option['value'] == "":
            continue
        index = int_or_text(option['value'])
        value = option.text.strip()
        decoded_text = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode()
        decoded_text = re.sub(r'[^A-Za-z0-9 ]+', '', decoded_text).replace("  ", " ").replace(" ", "_")
        global_messages.append(f'<data name="{decoded_text.upper()}" xml:space="preserve">\n        <value>{value}</value>\n    </data>')
        decoded_enum = decoded_text.split("_")
        enum_name = ""
        replace_prep = False
        for name in decoded_enum:
            if replace_prep and name.upper() in {'A', 'E', 'I', 'O', 'U', 'DA', 'DE', 'DO', 'EM'}:
                continue
            enum_name = enum_name + name.capitalize()

        enums.append(f'[Display(Name = "{decoded_text.upper()}", ResourceType = typeof(GlobalMessages))]\n{enum_name} = {index},')

for message in global_messages:
    print(message)

print('\n\n')

for enum in enums:
    print(enum)
