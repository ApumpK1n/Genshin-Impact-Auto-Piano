import time
import Config
import pyautogui


class Play:
    def __init__(self):
        pass

    def PlayStave(self, stave):

        bitTime = 60.0 / stave.Bpm 

        for node in stave.GetNodes():
            if node.type == Config.Single:
                pyautogui.press(node.value)
            elif node.type == Config.ChordType:
                pyautogui.press(node.value, presses=len(node.value))
            elif node.type == Config.Arpeggio:
                pyautogui.press(node.value, presses=len(node.value), interval=0.05)
            elif node.type == Config.Space:
                time.sleep(bitTime)