from pynput import keyboard
from pynput.keyboard import Key, Controller

kb = Controller()
buffer = []
expansions = {
    "!test": "This is a test!"
}


def expand(buf, expansion, key):
    print(expansion)
    backspaces = len(buf) + 1
    for x in range(backspaces):
        kb.press(Key.backspace)
        kb.release(Key.backspace)
    kb.type(expansion)
    kb.press(key)
    kb.release(key)


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        buffer.append(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))

    if key == Key.space or key == Key.enter:
        print(buffer)
        if "".join(buffer) in expansions:
            expand(buffer, expansions["".join(buffer)], key)
        buffer.clear()
    if key == Key.backspace:
        if buffer:
            buffer.pop()
            print(buffer)


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
