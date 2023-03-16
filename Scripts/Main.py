import Parse
import Config
import Play

def Main():
    Parser = Parse.Parse()
    stave = Parser.ParseFile(Config.MusicPath)

    Player = Play.Play()
    Player.PlayStave(stave)

    pass



if __name__ == '__main__':
    Main()
