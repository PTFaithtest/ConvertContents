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

with open(raw, 'r+', encoding='utf-8') as bundle:
    better = []
    articles = ['A ', 'An ', 'The ', 'Un ', 'Una ', 'Unos ', 'Unas ', 'El ', 'Los ', 'La ', 'Las ', 'Lo ']
    messy = 'â€™'
    dash = 'â€“'
    quote = 'â€œ'
    nuther = 'â€\x9d'
    divider = '| '
    accented_o = 'Ã³'
    accented_n = 'Ã±'


    for line in bundle:
        old_string = line.strip()
        # print(f'old: {old_string}')
        # for art in articles:
            # untouched = True
            # if old_string.startswith(art):
                # artless_string = old_string.replace(art, '')
                # untouched = False
                # break
            # else:
                # continue
        # if untouched:
            # artless_string = old_string
        artless_string = remove_articles(old_string, articles)
        # print(f'new: {artless_string}')
        if len(artless_string) > 2 and artless_string[-3] == '~':
            truncated = slice(0, -3)
            better_string = artless_string[truncated]
        else:
            continue
        if better_string.startswith('Automatic') and better_string.endswith('Update') or better_string.endswith('Marker Resource') or better_string.endswith('Mobile Ed Bonus Offer'):
            continue
        else:
            real_title = better_string
        clean_string = replace_chars(real_title, messy, '\'')
        dashless_string = replace_chars(clean_string, dash, '-')
        quote_string = replace_chars(dashless_string, quote, '')
        nuther_string = replace_chars(quote_string, nuther, '')
        undivided_string = replace_chars(nuther_string, divider, '')
        accento_string = replace_chars(undivided_string, accented_o, 'ó')
        accentn_string = replace_chars(accento_string, accented_n, 'ñ')
        capitalized_string = accentn_string.title()
        if len(capitalized_string) > 0:
            better.append(capitalized_string)       
    better.sort()
contents = Path.home().joinpath('ConvertContents', 'BundleContents.txt')
with open(contents, 'w+', encoding='utf-8') as new_file:
    for i in better:
        new_file.write(f'{i}\n')
os.startfile(contents)   
