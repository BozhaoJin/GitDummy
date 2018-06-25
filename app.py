def prompt(txt):
    """Text with prompt to enter."""
    INPUT_PROMPT_SYMB = '> '
    return '{}\n{}'.format(txt, INPUT_PROMPT_SYMB)

print("Hello world!")
user_name = input(prompt('What is your name?'))
