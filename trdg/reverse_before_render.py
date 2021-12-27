def reverse_before_render(strings):
    special_char1_small = [chr(390), chr(596), chr(7440),chr(8580)] #Character codes for small "ɔ"
    special_char1_big = [chr(1021), chr(8579)]  #Character codes for big "ɔ"
    special_char2_big = [chr(400)] #Character codes for big "ɛ"
    special_char2_small = [chr(603), chr(949)]  #Character codes for small "ɛ"
    special_chars = special_char1_small + special_char1_big + special_char2_small + special_char2_big
    for idx, string in enumerate(strings):
        string = string.lstrip().rstrip()
        strings[idx] = string
        if string == ' ':
            del string
        for _, char in enumerate(string):
            if char in special_char1_small:
                string = string.lstrip().rstrip().replace(char, 'c')
                strings[idx] = string
                continue
            if char in special_char1_big:
                string = string.lstrip().rstrip().replace(char, 'C')
                strings[idx] = string
                continue
            if char in special_char2_small:
                string = string.lstrip().rstrip().replace(char, 'j')
                strings[idx] = string
                continue
            if char in special_char2_big:
                string = string.lstrip().rstrip().replace(char, 'J')
                strings[idx] = string
                continue
             
    return strings