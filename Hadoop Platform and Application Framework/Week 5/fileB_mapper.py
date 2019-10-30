def split_fileB(line):
    # split the input line into word, date and count_string
    line = line.strip()
    date, key_value = line.split(" ")
    word, count_string = key_value.split(",")
    
    return (word, date + " " + count_string)
