def greet(greeting, name):
    """Returns a greeting

    Args:
        greeting (string): A greet word
        name (string): A person's name

    Returns:
        string: A greeting with a person's name
    """
    return f"{greeting} {name.title()}"


print(greet("Hello", "dima"))
