text = "jarvis play music destiny"

# Extract text after "music"
music = text.split("music", 1)[1].strip()

print("Text after 'music':", music)


print(music)
from MusicPlayer import MusicPlayer
music=MusicPlayer(music)

    