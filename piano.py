import keyboard
from pygame import mixer

mixer.init()

do = mixer.Sound('notes/do.wav')
re = mixer.Sound('notes/re.wav')
mi = mixer.Sound('notes/mi.wav')
fa = mixer.Sound('notes/fa.wav')
sol = mixer.Sound('notes/sol.wav')
lja = mixer.Sound('notes/lja.wav')
si = mixer.Sound('notes/si.wav')

keymap = {
    'q': do,
    'w': re,
    'e': mi,
    'r': fa,
    't': sol,
    'y': lja,
    'u': si
}

for key, note in keymap.items():
    keyboard.add_hotkey(key, note.play)

while True:
    pass
