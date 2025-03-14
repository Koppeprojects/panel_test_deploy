import panel as pn

pn.extension()

def say_hello(name="World"):
    return f"Hello, {name}!"
    
button = pn.widgets.Button(name="Click Me", button_type="primary")

def on_click(event):
    button.name = "Clicked!"

button.on_click(on_click)

interact=pn.interact(say_hello, name="World")
pn.Row(button,interact).servable()
