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
    articles = [
        'A ', 'An ', 'Der ', 'Die ', 'Das ', 'Ein ', 'Eine ', 'El ', 'L\'', 'La ', 'Las ', 'Le ', 'Les ', 'Lo ',  'Los ', 'The ', 'Un ', 'Una ', 'Unas ', 'Une ', 'Unos ' 
        ]
    char_dict = {
        'â€™': '\'', 'â€“': '-', 'â€œ': '“', 'â€\x9d': '”', '| ': '', 'Ã³': 'ó', 'Ã±': 'ñ', 'â€¦': '…', 'Ã­': 'í', 'Ã“': 'Ó', 'Ã©': 'é', 'Ã¡': 'á', 'Â¿': '¿', 'â€”': '—', 'Ã¼': 'ü',
        'ãº': 'ú', 'Ã‰': 'É', 'Â¡': '¡', 'Ã¶': 'ö', 'Ã¤': 'ä', 'â€ž': '„', 'Â»': '»', 'â«': '«', 'Ã„': 'Ä', 'Ãœ': 'Ü', 'Ã–': 'Ö', 'uÌˆ': 'ü','Å™': 'ř', 'Ã§': 'ç', 'Ãª': 'ê', 'Ã¨': 'è',
        'Ã': 'à'
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
        artless_string = remove_articles(real_title, articles)
        if artless_string.startswith('â€œ'):
            artless_string = artless_string.replace('â€œ', '', 1)
            artless_string = artless_string.replace('â€\x9d', '', 1)
        elif artless_string.startswith('Â¿'):
            artless_string = artless_string.replace('Â¿', '', 1)
            artless_string = artless_string.replace('?', '', 1)
        elif artless_string.startswith('Â¡'):
            artless_string = artless_string.replace('Â¡', '', 1)
            artless_string = artless_string.replace('!', '', 1)
        elif artless_string.startswith('('):
            artless_string = artless_string.replace('(', '', 1)
            artless_string = artless_string.replace(')', '', 1)
        elif artless_string.startswith('Ãœ'):
            artless_string = artless_string.replace('Ãœ', 'U', 1)
        elif artless_string.startswith('Ã'):
            artless_string = artless_string.replace('Ã', 'A', 1)
        elif artless_string.startswith('Ö'):
            artless_string = artless_string.replace('Ö', 'O', 1)
        elif 'Ð¡Ð¸Ð½Ð¾Ð´Ð°Ð»ÑŒÐ½Ñ‹Ð¹ ÐŸÐµÑ€ÐµÐ²Ð¾Ð´ (1876/1956)' in artless_string:
            artless_string = 'Русский Синодальный Перевод (1876/1956)'
        converted_string = convert_process(artless_string, char_dict)      
        capitalized_string = converted_string[0].upper() + converted_string[1:]   
        better.append(capitalized_string)       
    better.sort()
contents = Path.home().joinpath('ConvertContents', 'BundleContents.txt')
with open(contents, 'w+', encoding='utf-8') as new_file:
    for i in better:
        new_file.write(f'{i}\n')
os.startfile(contents)   
