import panel as pn

pn.extension()

def say_hello(name="World"):
    return f"Hello, {name}!"

pn.interact(say_hello, name="World").servable()
