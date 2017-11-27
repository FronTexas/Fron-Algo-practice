def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns): return False 
    string_to_pattern = {}
    pattern_to_string = {}

    for i in range(len(strings)):
        has_pattern_missmatch = strings[i] in string_to_pattern and string_to_pattern[strings[i]] != patterns[i] 
        has_string_missmatch = patterns[i] in pattern_to_string and pattern_to_string[patterns[i]] != strings[i]
        if has_pattern_missmatch or has_string_missmatch: 
            return False 
        string_to_pattern[strings[i]] = patterns[i]
        pattern_to_string[patterns[i]] = strings[i]
    return True
