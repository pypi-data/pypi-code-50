
def classes_for_token(token):
    """This function returns a set of classes for a given token.
    Depending on its script, medium and rend attribute,
    appropriate css-class names are returned
    """

    medium2style = {
        #"Blei"   : "color: gray",
        #"STinte" : "color: black",
        #"BlTinte": "color: blue",
        #"BrTinte": "color: brown",
    }
    medium2class = {
        #"Blei"    : "tei-Blei",
        #"STinte"  : "tei-STinte",
        #"BlTinte" : "tei-BlTinte",
        #"BrTinte" : "tei-BrTinte",
    }
    rend2style = {
        "unterstr": "text-decoration: underline",
        "durchstr": "text-decoration: line-through",
        "überschr": "vertical-align: super",
        "hoch"    : "vertical-align: super",
        #"durchstr BlTinte": "text-decoration: line-through; text-decoration-color: blue",
        #"durchstr BrTinte": "text-decoration: line-through; text-decoration-color: brown",
        #"durchstr STinte" : "text-decoration: line-through; text-decoration-color: black",
        #"Blei"    : "color: gray",
        #"BrTinte" : "color: brown",
    }
    rend2class = {
        "unterstr": "tei-underline",
        "durchstr": "tei-line-through",
        "überschr": "tei-super",
        "hoch"    : "tei-super",
        #"durchstr BlTinte": "tei-line-through tei-line-through-blue",
        #"durchstr BrTinte": "tei-line-through tei-line-through-brown",
        #"durchstr STinte" : "tei-line-through",
        #"Blei"    : "tei-Blei",
        #"BrTinte" : "tei-BrTinte",
    }
    script2class = {
        #"Kurrent"   : "tei-Kurrent",
        #"Latein"    : "tei-Latein",
        #"Griechisch": "tei-Griechisch"
    }
    
    classes = []
    for script in script2class.keys():
        if script in token.get('script',''):
            classes.append(script2class[script])
    for medium in medium2class.keys():
        if medium in token.get('medium',''):
            classes.append(medium2class[medium])
    for rend in rend2class.keys():
        if rend in token.get('rend',''):
            classes.append(rend2class[rend])

    # add the labels themselves as classes
    classes += ["tei-{}".format(label) for label in token.labels]

    return set(classes)
