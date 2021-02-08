
import copy

class State:

    def __init__(self, numOfSheepLeft = 0, numOfWolvesLeft = 0, numOfSheepRight = 0, numOfWolvesRight= 0, BoatIsOnLeft = True):
        self.numOfSheepLeft = numOfSheepLeft
        self.numOfWolvesLeft = numOfWolvesLeft
        self.numOfSheepRight = numOfSheepRight
        self.numOfWolvesRight = numOfWolvesRight
        self.BoatIsOnLeft = BoatIsOnLeft
        self.route = list() #to save all the moves

    def __eq__(self, other):
        return self.numOfSheepLeft == other.numOfSheepLeft and self.numOfWolvesLeft == other.numOfWolvesLeft and self.BoatIsOnLeft == other.BoatIsOnLeft and self.numOfSheepRight == other.numOfSheepRight and self.numOfWolvesRight == other.numOfWolvesRight

    def __hash__(self):
        return hash((self.numOfSheepLeft, self.numOfWolvesLeft, self.numOfSheepRight, self.numOfWolvesRight, self.BoatIsOnLeft))

    def isGoalState(self):
        return self.numOfSheepLeft == 0 and self.numOfWolvesLeft == 0


    def isValidState(self):
        if self.numOfWolvesLeft >= 0 and self.numOfWolvesRight >= 0 and self.numOfSheepLeft >= 0 and self.numOfSheepRight >= 0 and (self.numOfSheepLeft >= self.numOfWolvesLeft or self.numOfSheepLeft == 0) and (self.numOfSheepRight >= self.numOfWolvesRight or self.numOfSheepRight == 0):
            return True
        else:
            return False

    def generateStates(self): #there are 6 valid and efficient ways to move
                              #skip inefficient way such as move 2 sheep from right to left
        
        newStatesList = list()
        #when boat is left side
        if self.BoatIsOnLeft:
            #the case that moves two sheep from left to right
            newState = State(self.numOfSheepLeft - 2, self.numOfWolvesLeft, self.numOfSheepRight + 2,self.numOfWolvesRight, not self.BoatIsOnLeft)
            if newState.isValidState():
                newState.route = copy.copy(self.route)
                newState.route.append((2,0))
                newStatesList.append(newState)

            #the case that moves two wolves from left to right
            newState = State(self.numOfSheepLeft, self.numOfWolvesLeft - 2, self.numOfSheepRight,self.numOfWolvesRight + 2, not self.BoatIsOnLeft)
            if newState.isValidState():
                newState.route = copy.copy(self.route)
                newState.route.append((0,2))
                newStatesList.append(newState)

            #the case that moves one sheep and one wolf from left to right
            newState = State(self.numOfSheepLeft - 1, self.numOfWolvesLeft - 1, self.numOfSheepRight + 1,self.numOfWolvesRight + 1, not self.BoatIsOnLeft)
            if newState.isValidState():
                newState.route = copy.copy(self.route)
                newState.route.append((1,1))
                newStatesList.append(newState)

        else: # when boat is on the right side
            #the case that moves one sheep from right to left
            newState = State(self.numOfSheepLeft + 1, self.numOfWolvesLeft, self.numOfSheepRight -1,self.numOfWolvesRight, not self.BoatIsOnLeft)
            if newState.isValidState():
                newState.route = copy.copy(self.route)
                newState.route.append((1,0))
                newStatesList.append(newState)

            #the case that moves one wolf from right to left
            newState = State(self.numOfSheepLeft, self.numOfWolvesLeft + 1, self.numOfSheepRight, self.numOfWolvesRight - 1, not self.BoatIsOnLeft)
            if newState.isValidState():
                newState.route = copy.copy(self.route)
                newState.route.append((0,1))
                newStatesList.append(newState)
        
            #the case that moves one wolf and one sheep from right to left     
            newState = State(self.numOfSheepLeft + 1, self.numOfWolvesLeft + 1, self.numOfSheepRight - 1,self.numOfWolvesRight - 1, not self.BoatIsOnLeft)
            if newState.isValidState():
                newState.route = copy.copy(self.route)
                newState.route.append((1,1))
                newStatesList.append(newState)

        return newStatesList
