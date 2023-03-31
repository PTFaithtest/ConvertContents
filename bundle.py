# TO DO
# fix quoteless use this product to test so that it gets rid of every instance: https://librarymanager.faithlife.com/metadata/%7b13CFFC11-9C19-450C-82FE-2E61378531A3%7d
# code for divider has been modified but not tested, can be compared with code on github
# replace only works on first instance, so better way needs to be used
# code needs to be worked out for 'nuther" which was previously overlooked
# consolidate code so it is not makeing so many lists that get replaced by subsequent lists
# get rid of blank lines in the beginning
# perhaps disallow marketing tags like automatic updates


import os
from pathlib import Path

ignore = ['Top Title (Value ~ Language)', 'Titles (Value ~ Language)']

raw = Path.home().joinpath('ConvertContents', 'raw_bundle.txt')
with open(raw, 'r+', encoding='utf-8') as bundle:
    better = []
    cleaner = []
    quoteless = []
    dashless = []
    new_bundle = []
    artless = []
    articles = ['A ', 'An ', 'The ']
    divider = '|'
    messy = 'â€™'
    dash = 'â€“'
    quote = 'â€œ'
    nuther = 'â€'
    for line in bundle:
        old_string = line.strip()
        if old_string in ignore:
            continue
        elif len(old_string) > 2 and old_string[-3] == '~':
            truncated = slice(0, -3)
            better_string = old_string[truncated]
        else: 
            better_string = old_string
        better.append(better_string)
    for bet in better:
        untouched = True
        for art in articles:
            if bet.startswith(art):
                artless_string = bet.replace(art, '')
                untouched = False
                artless.append(artless_string)
                break
            else:
                continue
        if untouched:
            artless.append(bet)   
    for rtl in artless:
        if messy in rtl:
            clean_string = rtl.replace(messy, "'")
        else:
            clean_string = rtl
        cleaner.append(clean_string)
    for cl in cleaner:
        if dash in cl:
            dashless_string = cl.replace(dash, '-')      
        else:
            dashless_string = cl
        dashless.append(dashless_string)
    for da in dashless:
        if quote in da:
            quote_string = da.replace(quote, '')
        else:
            quote_string = da
        quoteless.append(quote_string)   
    for qu in quoteless:      
        if divider in qu:
            new_string = qu.translate(divider, '')              
        else:
            new_string = qu
        new_bundle.append(new_string)
    new_bundle.sort()
contents = Path.home().joinpath('ConvertContents', 'BundleContents.txt')    
with open(contents, 'w+', encoding='utf-8') as new_file:
    for i in new_bundle:
        new_file.write(f'{i}\n')
os.startfile(contents)

