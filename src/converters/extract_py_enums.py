import re

from bs4 import BeautifulSoup
import unicodedata

f = open('dropdown.html')
soup = BeautifulSoup(f, "html.parser")
f.close()
all_options = soup.find_all('option')

index = 1
global_messages = list()
enums = list()
type_select = soup.find('select')['name']
value_convert = 'f"{value}"'
func_name = f"tipo_{type_select}_to_enum"
print(f'def {func_name}(value: str):\n    if value is None:\n        return None\n    to_comp = {value_convert}')
for option in all_options:
    if option['value']:
        if option['value'] == "":
            continue
        value = f"{option['value']}".strip().upper()
        print(f'    if to_comp.upper() == "{value}":\n        return {index}')
        index = index + 1
print('\n    return None')
print(f'\n{func_name}(dropdown_value)')
print(f'\ndropdown_value, dropdown_text = extract_selected_dropdown_value(chrome.find_element(By.NAME, "{type_select}"))')
