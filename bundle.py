import os
with open('raw_bundle.txt', 'r+', encoding='utf-8') as bundle:
    better = []
    cleaner = []
    dashless = []
    new_bundle = []
    artless = []
    articles = ['A ', 'An ', 'The ']
    divider = '|'
    suffix = '~en'
    messy = 'â€™'
    dash = 'â€“'
    for line in bundle:
        # print(f'{type(line)}: {line}')
        old_string = line.strip()
        if suffix in old_string:
            better_string = old_string.replace(suffix, '', 5)
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
            clean_string = rtl.replace(messy, "'", 5)
        else:
            clean_string = rtl
        cleaner.append(clean_string)
    for cl in cleaner:
        if dash in cl:
            dashless_string = cl.replace(dash, '-', 5)      
        else:
            dashless_string = cl
        dashless.append(dashless_string)
    for di in dashless:
        if divider in di:
            for i in range(len(di)):
                if di[i] != divider:
                    continue
                else:
                    new_string = di[i+1:]
                    break                   
        else:
            new_string = di
        new_bundle.append(new_string)
    new_bundle.sort()
with open('BundleContents.txt', 'w+', encoding='utf-8') as new_file:
    for i in new_bundle:
        new_file.write(f'{i}\n')
os.startfile('BundleContents.txt')

