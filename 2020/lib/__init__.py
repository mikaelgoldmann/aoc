
def paragraphs(data):
    '''
    data is sys.stdin or an open text file or similar
    Yields a list of lines (stripped) for each paragraph.
    Paragraphs are separated by empty lines.
    '''
    lines = []
    for x in data:
        x = x.strip()
        if not x:
            yield lines
            lines = []
        else:
            lines.append(x)
    if lines:
        yield lines
