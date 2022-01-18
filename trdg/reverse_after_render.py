def reverse_after_render(strings):
    '''
    Replace the special characters in the strings with the characters that are used in the rendering
    process.
    
    :param strings: a list of strings to be rendered
    :return: The strings with the special characters replaced.
    '''
    special_char1_small = [chr(390), chr(596), chr(7440),chr(8580)] #Character codes for small "ɔ"
    special_char1_big = [chr(1021), chr(8579)]  #Character codes for big "ɔ"
    special_char2_big = [chr(400)] #Character codes for big "ɛ"
    special_char2_small = [chr(603), chr(949)]  #Character codes for small "ɛ"
    special_chars = special_char1_small + special_char1_big + special_char2_small + special_char2_big
    for idx, string in enumerate(strings):
        for _, char in enumerate(string):
            if char == 'c':
                string = string.replace('c', special_char1_small[1])
                strings[idx] = string
                continue
            if char == 'C':
                string = string.replace('C', special_char1_big[0])
                strings[idx] = string
                continue
            if char == 'j':
                string = string.replace('j', special_char2_small[0])
                strings[idx] = string
                continue
            if char == 'J':
                string = string.replace('J', special_char2_small[0])
                strings[idx] = string
                continue
            
    return strings