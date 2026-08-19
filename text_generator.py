

def read_html_data():
    """read the template.html code, format it and returns it as str"""

    with open('index_template.html', 'r', encoding='utf-8') as textobj:
        text = textobj.read()
        return text

def replace_text(html_code, movie, website_title):
    """replace the website title and the new body to the template HTML Code"""

    title_new_text = html_code.replace("__TEMPLATE_TITLE__", website_title)
    new_text = title_new_text.replace('__TEMPLATE_MOVIE_GRID__', movie)
    return new_text

def write_a_html_code(new_text):
    """write the HTML code"""

    with open('movie.html', 'w', encoding='utf-8') as fileobj:
        fileobj.write(new_text)