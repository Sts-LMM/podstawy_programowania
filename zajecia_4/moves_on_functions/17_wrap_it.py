def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

def make_underline(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@make_bold
@make_italic
@make_underline
def hello():
    return "hello"

print(hello())
# Output: <b><i><u>hello</u></i></b>
