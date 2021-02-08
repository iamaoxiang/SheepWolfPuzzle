from State import State

class SemanticNetsAgent:

    def __init__(self):
        pass

    def solve(self, initial_sheep, initial_wolves):

        #construct state object
        state = State(initial_sheep, initial_wolves, 0, 0, True)

     
        #if there is only 1 animal in initial state, just move that animal to the right river
        if initial_sheep + initial_wolves == 1:
            return (initial_sheep, initial_wolves)
        if state.isGoalState():
            return list()

        #otherwise, breadth first search from current state
        else:
            return self.bfs(state)

    def bfs(self, state):
        #bfs use a queue to access current state, push new generated states to the back of the queue
        queue = list()
        #set to store all the states that have been seen 
        visitedStates = set()
        
        #start from initial state
        queue.append(state)
        visitedStates.add(state)

        #while the queue is not empty, keep poping state
        while queue:
            curState = queue.pop(0)

            #generate all possible states from current state
            nextStates = curState.generateStates()
            
            #check each newly generated state,
            #if the state is goalState, return
            #if the state has not been seen, add it to the visited set, add it to queue
            for eachState in nextStates: 
                if eachState.isGoalState():
                    return eachState.route
                if eachState not in visitedStates:
                    visitedStates.add(eachState)
                    queue.append(eachState)

        return list()


