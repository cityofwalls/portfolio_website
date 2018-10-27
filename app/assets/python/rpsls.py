import random
    
class Graph:
    """
    Constructs a directed graph represented as a dictionary of
    strings (vertices) to lists of strings (edge lists).
    """
    def __init__(self):
        self.V = {}
    
    # Adds a vertex to the graph with string identifier
    def add_vertex(self, name):
        self.V[name] = []
        
    def add_edge(self, v, w):
        self.V[v].append(w)
        

"""
For rpsls, the vertices will be the strategies and the edges represent
a victory over another strategy.
The size of the graph will be V = 5 and E = 10, since each strategy
conquers two others.
"""
G = Graph()

G.add_vertex("rock")
G.add_vertex("paper")
G.add_vertex("scissors")
G.add_vertex("lizard")
G.add_vertex("Spock")

G.add_edge("rock", "scissors")
G.add_edge("rock", "lizard")

G.add_edge("paper", "Spock")
G.add_edge("paper", "rock")

G.add_edge("scissors", "paper")
G.add_edge("scissors", "lizard")

G.add_edge("lizard", "paper")
G.add_edge("lizard", "Spock")

G.add_edge("Spock", "scissors")
G.add_edge("Spock", "rock")

# -------------------------

def rpsls(player_choice):
    legal_strats = ["rock", "paper", "scissors", "lizard", "Spock"]
    if not player_choice == str(player_choice) or (not player_choice in legal_strats):
        print("Oops, not a legal choice.")
        print()
        return
        
    print("Player chose " + player_choice)
    
    conversions = { 0:"rock", 1:"paper", 2:"scissors", 3:"lizard", 4:"Spock" }
    comp_num = random.randrange(0, 5)
    comp_choice = conversions[comp_num]
    
    print("Computer chose " + comp_choice)
    
    if player_choice in G.V[comp_choice]:
        print("Computer wins!")
        print()
        return
    elif comp_choice in G.V[player_choice]:
        print("Player wins!")
        print()
        return
    else:
        print("Player and computer tie!")
        print()
        return
    
rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("Spock")