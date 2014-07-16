import colorama
from levels import levels

class Player:
    def __init__(self):
        #a list of challenge names in the current level that the player has solved
        self.completed = []
        self.current_level_index = 0

    """
    Lists the challenges currently available to the player
    """
    def list_challenges(self, args):
        level_challenges = levels[self.current_level_index].Challenges
        column_width = max(len(c.Name) for c in level_challenges)
        for challenge in level_challenges:
            if challenge in self.completed:
                color = colorama.Fore.GREEN
            else:
                color = colorama.Fore.RED
            print(color + "%s\t%dXP" % (challenge.Name.ljust(column_width), challenge.XP))

    """
    Prints info about the challenge specified by the player
    """
    def challenge_info(self, args):
        for challenge in levels[self.current_level_index]:
            if challenge.Level == self.current_level and challenge.Name == args.challenge_name:
                #TODO prettier printing
                print(challenge.Story)
                break
        else:
            print("No challenge named ``%s'' on level %d" % (args.challenge_name, self.current_level))

    def solve_challenge(self, args):
        print("Hey")