# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue # import queue from util(FIFO)

    intial = problem.getStartState() # go in searchagents.py to get the start state of the problem

    if problem.isGoalState(intial): # if the start is at goal then 
        return []                  # just return cause solution is found

    queue = Queue()   #else make the queue so we can explore the maze and find a path
    queue.push((intial, []))   # we start with intial node and the empty path  
 
    beenThere = set()     # if the node has been visited then it will be stored in the set 
    beenThere.add(intial)  # becasue we don't revist node we have to add the start to the visited set so it doesn't go back

    while not queue.isEmpty():  # i am making while loop run until there are no nodes left in the queue to explore
        state, path = queue.pop() # pop the state we are at(current location) and the path we took to get here 

        print("going to :", state, "cost of length:", len(path)) # for debugging purposes
        # i wanted to check if the code is acutally working as the bfs 

        if problem.isGoalState(state): # now we check the node we are at if it is a goal 
            return path # then return the path from start to goal 
    

        for nextState, actionTaken, cost in problem.getSuccessors(state):  #because we have to look at next node also cost is an passed but not used my code wouldn't work
            
          #  if problem.isGoalState(nextState): # from our current sate if the nextsate is goal 
            #    return path + [actionTaken] # then return the path from intial to until current we are standing on  + the goal path we will take
            
            if nextState not in beenThere: # we only look at node that are not yet visted 
                beenThere.add(nextState)  # now we are at the now so mark that node as visited(i was getting infinte loop because of this)
                queue.push((nextState, path + [actionTaken])) # and push it in the queue with the updated path 

    return []  # return the empty queue list because no answer exists

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
