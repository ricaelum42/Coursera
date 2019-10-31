def split_show_views(line):
    line = line.strip()
    show, views = line.split(",")
    views = int(views)
    return (show, views)
    
    
def split_show_channel(line):
    line = line.strip()
    show, channel = line.split(",")
    return (show, channel)
    
