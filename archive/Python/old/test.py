def hello(text):
    return f"Hello {text}!"
    
def capitalize(text):
    modified_text = str(text).capitalize()
    return modified_text

def do_something_to_text(text, action):
    modified_text = action(text)
    return modified_text

def reverse(text):
    text = text[::-1]
    return text

def main():
    print("Welcome to the functional programming demonstration!")
    # TODO: Capitalize a name
    print (do_something_to_text("john", capitalize))
    print (reverse("Hello World!"))
    print ("Hello World!")
    
    # TODO: Greet a name
    print (do_something_to_text("john", hello))

if __name__ == "__main__":
    main()