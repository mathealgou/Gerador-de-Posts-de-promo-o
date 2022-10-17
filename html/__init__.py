class Html:
    def read():
        with open("./html/html.html", 'r') as f:
            return f.read()
    
    def read_css():
        with open("./html/css.css", 'r') as f:
            return f.read()