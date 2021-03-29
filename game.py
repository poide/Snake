from random import randrange
import random
class Game:
  
  def __init__(self):
    initialPosition = randrange(100)
    initialPositionFood = randrange(100)
    while initialPosition == initialPositionFood:
      initialPositionFood = randrange(100)
    initBoard =  [0] * 100
    initBoard[initialPosition] = 1
    initBoard[initialPositionFood] = -1

    self.board = initBoard
    self.positionList=[initialPosition]
    self.facing = "N"
    self.FoodPosition = initialPositionFood
    self.state = "Running"
    self.score = 0
  
  def boardToConsole(self): 
    i = 0
    while i < 10:
        j = 0
        numberLine = []
        while j < 10:
            index = (i * 10) + j
            numberLine.append(self.board[index])
            j = j + 1
        print(numberLine)
        i = i+1


  def spawnFood(self):
    copyboard = self.board.copy()
    listEmptyPos = []
    i = 0
    while i < len(copyboard):
      if copyboard[i] == 0:
        listEmptyPos.append(i)
      i = i+1 

    self.board[random.choice(listEmptyPos)] = -1

  def move(self):
    if self.score == 99:
      self.state = "Win"
    if self.facing == "N" :
      newHeadPosition = self.positionList[0] - 10
      if newHeadPosition < 0:
        newHeadPosition = newHeadPosition + 100
      if self.board[newHeadPosition] > 0 :
        self.state = "Dead"
      if self.board[newHeadPosition] == -1: #Here you eat a piece of food, so we need to create another one
        self.positionList.insert(0,newHeadPosition)
        self.board[newHeadPosition]= 1
        self.spawnFood()
        self.score = self.score + 1
      if self.board[newHeadPosition] == 0:
        self.positionList.insert(0,newHeadPosition)
        self.board[newHeadPosition]= 1
        self.board[self.positionList[-1]] = 0
        self.positionList = self.positionList[0:(len(self.positionList)-1)]
    if self.facing == "S" :
      newHeadPosition = self.positionList[0] + 10
      if newHeadPosition >=100:
        newHeadPosition = newHeadPosition -100
      if self.board[newHeadPosition] > 0 :
        self.state = "Dead"
      if self.board[newHeadPosition] == -1: #Here you eat a piece of food, so we need to create another one
        self.positionList.insert(0,newHeadPosition)
        self.board[newHeadPosition]= 1
        self.spawnFood()
        self.score = self.score + 1
      if self.board[newHeadPosition] == 0:
        self.positionList.insert(0,newHeadPosition)
        self.board[newHeadPosition]= 1
        self.board[self.positionList[-1]] = 0
        self.positionList = self.positionList[0:(len(self.positionList)-1)]
    if self.facing == "E" :
      newHeadPosition = self.positionList[0] + 1
      if newHeadPosition % 10 == 0:
        newHeadPosition = newHeadPosition -10
      if self.board[newHeadPosition] > 0 :
        self.state = "Dead"
      if self.board[newHeadPosition] == -1: #Here you eat a piece of food, so we need to create another one
        self.positionList.insert(0,newHeadPosition)
        self.board[newHeadPosition]= 1
        self.spawnFood()
        self.score = self.score + 1
      if self.board[newHeadPosition] == 0:
        self.positionList.insert(0,newHeadPosition)
        self.board[newHeadPosition]= 1
        self.board[self.positionList[-1]] = 0
        self.positionList = self.positionList[0:(len(self.positionList)-1)]  
    if self.facing == "W" :
      newHeadPosition = self.positionList[0] - 1
      if newHeadPosition % 10 == 9:
        newHeadPosition = newHeadPosition + 10
      if self.board[newHeadPosition] > 0 :
        self.state = "Dead"
      if self.board[newHeadPosition] == -1: #Here you eat a piece of food, so we need to create another one
        self.positionList.insert(0,newHeadPosition)
        self.board[newHeadPosition]= 1
        self.spawnFood()
        self.score = self.score + 1
      if self.board[newHeadPosition] == 0:
        self.positionList.insert(0,newHeadPosition)
        self.board[newHeadPosition]= 1
        self.board[self.positionList[-1]] = 0
        self.positionList = self.positionList[0:(len(self.positionList)-1)]

  def changeOrientation(self,orientation:str):
    if orientation == "W":
      if self.facing != "E":
        self.facing = "W"
    if orientation == "E":
      if self.facing != "W":
        self.facing = "E"
    if orientation == "N":
      if self.facing != "S":
        self.facing = "N"
    if orientation == "S" :
      if self.facing != "N":
        self.facing = "S"