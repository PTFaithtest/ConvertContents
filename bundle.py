import os
from pathlib import Path

raw = Path.home().joinpath('ConvertContents', 'raw_bundle.txt')

def remove_articles(current_line, art_fam):
    for art in art_fam:
        if current_line.startswith(art):
            chopped_string = current_line.replace(art, '', 1)
            return chopped_string
        else:
            continue
    return current_line

def replace_chars(title, sub_string, new_char):
    if sub_string in title:
        new_string = title.replace(sub_string, new_char)
        return new_string
    else:
        return title
    
def convert_process(current_line, convert_dict):
    print(f'before: {current_line}')
    for key, val in convert_dict.items():
        if key in current_line:
            current_line = current_line.replace(key, val)
            print(f'mod: {current_line}')
    print(f'final: {current_line}') 
    return current_line

with open(raw, 'r+', encoding='utf-8') as bundle:
    better = []
    articles = ['A ', 'An ', 'The ', 'Un ', 'Una ', 'Unos ', 'Unas ', 'El ', 'Los ', 'La ', 'Las ', 'Lo ', 'Der ', 'Die ', 'Das ', 'Ein ', 'Eine ']
    char_dict = {
        'â€™': '\'', 'â€“': '-', 'â€œ': '', 'â€\x9d': '', '| ': '', 'Ã³': 'ó', 'Ã±': 'ñ', 'â€¦': '…', 'Ã­': 'í', 'Ã“': 'Ó', 'Ã©': 'é', 'Ã¡': 'á', 'Â¿': '¿', 'â€”': '—', 'Ã¼': 'ü',
        'ãº': 'ú', 'Ã‰': 'É', 'Â¡': '¡'
        }
    for line in bundle:
        old_string = line.strip()
        if len(old_string) > 2 and old_string[-3] == '~':
            truncated = slice(0, -3)
            better_string = old_string[truncated]
        else:
            continue
        if better_string.startswith('Automatic') and better_string.endswith('Update') or better_string.endswith('Marker Resource'): 
            continue
        elif better_string.startswith('Mobile Ed Course (You Choose)') or better_string.endswith('Mobile Ed Bonus Offer'):
            continue
        else:
            real_title = better_string
        if real_title.startswith('Â¿'):
            real_title = real_title.replace('Â¿', '')
            real_title = real_title.replace('?', '')
        elif real_title.startswith('Â¡'):
            real_title = real_title.replace('Â¡', '')
            real_title = real_title.replace('!', '')
        artless_string = remove_articles(real_title, articles)
        converted_string = convert_process(artless_string, char_dict)      
        capitalized_string = converted_string.title()
        if '\'S' in capitalized_string:
            capitalized_string = capitalized_string.replace('\'S', '\'s')
        if len(capitalized_string) > 0:
            better.append(capitalized_string)       
    better.sort()
contents = Path.home().joinpath('ConvertContents', 'BundleContents.txt')
with open(contents, 'w+', encoding='utf-8') as new_file:
    for i in better:
        new_file.write(f'{i}\n')
os.startfile(contents)   
