import Parse
import Config
import Play
import tkinter.filedialog
import tkinter
import time



txtTypeFilter = [('txt' ,'.txt')]
window = tkinter.Tk()
window.withdraw()
Parser = Parse.Parse()
Player = Play.Play()
Enable = True

def OnEnd():
    global Enable
    Enable = True


def Main():
    stave = Parser.ParseFile(Config.MusicPath)
    Player.PlayStave(stave, onEnd=OnEnd)

def ShowInfo():
    print('10 seconds for ready')
    time.sleep(10)
    print('\nStart~\n')

if __name__ == '__main__':
    while Enable:
        try:
            input('\n Press Enter Start Choose Zither Score\n')
            dir = tkinter.filedialog.askopenfilename(initialdir = './琴谱', title = '选择琴谱', filetypes = txtTypeFilter)
            if dir == '':
                continue
            Enable = False
            Config.MusicPath = dir

            ShowInfo()
            Main()
        except KeyboardInterrupt:
            print('\nPlayInterrupt')
            Enable = True
        except Exception as e:
            print(e)
        finally:
            print("\nd--------------------------b!")
