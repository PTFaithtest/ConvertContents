import os
from pathlib import Path

ignore = ['Top Title (Value ~ Language)', 'Titles (Value ~ Language)']
raw = Path.home().joinpath('ConvertContents', 'raw_bundle.txt')

def replace_chars(title, sub_string, new_char):
    if sub_string in title:
        new_string = title.replace(sub_string, new_char)
        return new_string
    else:
        return title

with open(raw, 'r+', encoding='utf-8') as bundle:
    better = []
    articles = ['A ', 'An ', 'The ']
    messy = 'â€™'
    dash = 'â€“'
    quote = 'â€œ'
    nuther = 'â€\x9d'
    divider = '| '


    for line in bundle:
        old_string = line.strip()
        if old_string in ignore:
            continue
        if len(old_string) > 2 and old_string[-3] == '~':
            truncated = slice(0, -3)
            better_string = old_string[truncated]
        else:
            better_string = old_string
        if better_string.startswith('Automatic') and better_string.endswith('Update') or better_string.endswith('Marker Resource'):
            continue
        else:
            real_title = better_string
        clean_string = replace_chars(real_title, messy, '\'')
        dashless_string = replace_chars(clean_string, dash, '-')
        quote_string = replace_chars(dashless_string, quote, '')
        nuther_string = replace_chars(quote_string, nuther, '')
        undivided_string = replace_chars(nuther_string, divider, '')
        for art in articles:
            untouched = True
            if undivided_string.startswith(art):
                artless_string = undivided_string.replace(art, '')
                untouched = False
                break
            else:
                continue
        if untouched:
            artless_string = undivided_string
        if len(artless_string) > 0:
            better.append(artless_string)       
    better.sort()
contents = Path.home().joinpath('ConvertContents', 'BundleContents.txt')
with open(contents, 'w+', encoding='utf-8') as new_file:
    for i in better:
        new_file.write(f'{i}\n')
os.startfile(contents)   
