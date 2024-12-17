def merge_dicts(dict1, dict2):
    merge = {}
    for k, v in dict1.items():
        merge[k] = v
    for k, v in dict2.items():
        if k in merge:
            merge[k] = [merge[k], v]
        else:
            merge[k] = v
    return merge

dict1 = {'yra': 123, 'da': 321, 'kas': 111}
dict2 = {'kas': '3', 'ma': 'g', 'sdf': 'lan'}
print(merge_dicts(dict1, dict2))
