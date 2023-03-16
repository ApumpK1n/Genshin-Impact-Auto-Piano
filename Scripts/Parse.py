import Config
import Stave


class Parse:

    def __init__ (self):
        pass

    def ParseFile(self, filePath):
        with open(filePath, 'r', encoding='utf-8') as file:
            stave = Stave.Stave()

            lines = file.readlines()
            for index, line in enumerate(lines):
                if (index) == 0:
                    if line[0:4] == 'bpm=':
                        stave.Bpm = int(line[4:])
                    else:
                        stave.Bpm = Config.DefaultBpm
                if (line == ''): continue
                line = line.lower().replace('0', ' ').replace('\n', '')
                self.ParseLine(line, stave)

            return stave

    def ParseLine(self, line, stave):
        inBucket = False
        notesInBucket = []
        for note in line:
            if inBucket:
                if note == ')':
                    inBucket = False
                    stave.AddNode(Stave.Node(Config.ChordType, notesInBucket))
                    notesInBucket = []
                elif note == ']':
                    inBucket = False
                    stave.AddNode(Stave.Node(Config.Arpeggio, notesInBucket))
                    notesInBucket = []
                elif note.isalpha():
                    notesInBucket.append(note)
            else:
                if note == '(' or note == '[':
                    inBucket = True
                elif note == ' ':
                    stave.AddNode(Stave.Node(Config.Space, note))
                elif note.isalpha():
                    stave.AddNode(Stave.Node(Config.Single, note))

