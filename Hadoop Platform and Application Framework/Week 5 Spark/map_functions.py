def split_show_views(line):
    line = line.strip()
    show, views = line.split(",")
    views = int(views)
    return (show, views)
    
    
def split_show_channel(line):
    line = line.strip()
    show, channel = line.split(",")
    return (show, channel)
    
def extract_channel_views(show_views_channel): 
    channel = show_views_channel[1][1]
    views = show_views_channel[1][0]
    return (channel, views)
