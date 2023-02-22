#imports
import random

#variables
playerVar= 0
dice1Roll = 0
dice2Roll = 0
totalDice = 0
dice1String=0
dice2String=0
dice1List=[]
dice2List=[]

oneA='''
|  /|   | 
|   |   |
|  _|_  |
'''
twoA='''
|  /`\  |
|    /  |
|  /__  |
'''
threeA='''
|  ___  |
|     | |
|  ---| |
|  ___| |
'''
fourA='''
|  / |  |
| /__|  |
|    |  |
'''
fiveA='''
|  ___  |
| |     |
| '---, |
|  ___| |
'''
sixA='''
|  ___  |
| |     |
| |---, |
| |___| |
'''
sevenA='''
| ____  |
|    /  |
|   /   |
|  /    |
'''
eightA='''
|  ___  |
| |   | |
| |---| |
| |___| |
'''
nineA='''
|  ___  |
| |   | |
| `---| |
|  ___| |
'''
tenA='''
|     __  |
| /| |  | |
|  | |  | |
| _|_|__| |
'''
elevenA='''
|        |
| /| /|  |
|  |  |  |
| _|__|_ |
'''
twelveA='''
|         |
| /|  /`\ |
|  |    / |
| _|_ /__ |
'''
numberList = [[oneA,twoA,threeA,fourA,fiveA,sixA,sevenA,eightA,nineA,tenA,elevenA,twelveA],[1,2,3,4,5,6,7,8,9,10,11,12]]
whitespace='''

'''

dice1List=['''                                                                                             |
|                                                             --------                               |
|                                                            |        |                              |
|                                                            |    *   |                              |
|                                                            |        |                              |
|                                                             --------                               |
''',
'''                                                                                             |
|                                                             --------                               |
|                                                            |     *  |                              |
|                                                            |        |                              |
|                                                            |  *     |                              |
|                                                             --------                               |
''',
'''                                                                                             |
|                                                             --------                               |
|                                                            |     *  |                              |
|                                                            |    *   |                              |
|                                                            |  *     |                              |
|                                                             --------                               |
''',
'''                                                                                             |
|                                                             --------                               |
|                                                            |  *  *  |                              |
|                                                            |        |                              |
|                                                            |  *  *  |                              |
|                                                             --------                               |
''',
'''                                                                                             |
|                                                             --------                               |
|                                                            |  *  *  |                              |
|                                                            |    *   |                              |
|                                                            |  *  *  |                              |
|                                                             --------                               |
''',
'''                                                                                             |
|                                                             --------                               |
|                                                            |  *  *  |                              |
|                                                            |  *  *  |                              |
|                                                            |  *  *  |                              |
|                                                             --------                               |
'''
]
dice2List=['''                                      |
|                    --------                                                                        |       
|                   |        |                                                                       |   
|                   |    *   |                                                                       |
|                   |        |                                                                       |
|                    --------                                                                        |
''',
'''                                      |
|                    --------                                                                        |       
|                   |     *  |                                                                       |   
|                   |        |                                                                       |
|                   |  *     |                                                                       |
|                    --------                                                                        |
''',
'''                                      |
|                    --------                                                                        |       
|                   |     *  |                                                                       |   
|                   |    *   |                                                                       |
|                   |  *     |                                                                       |
|                    --------                                                                        |
''',
'''                                      |
|                    --------                                                                        |       
|                   |  *  *  |                                                                       |   
|                   |        |                                                                       |
|                   |  *  *  |                                                                       |
|                    --------                                                                        |
''',
'''                                      |
|                    --------                                                                        |       
|                   |  *  *  |                                                                       |   
|                   |    *   |                                                                       |
|                   |  *  *  |                                                                       |
|                    --------                                                                        |
''',
'''                                      |
|                    --------                                                                        |       
|                   |  *  *  |                                                                       |   
|                   |  *  *  |                                                                       |
|                   |  *  *  |                                                                       |
|                    --------                                                                        |
'''
]

#functions
def randomRoll():
    global dice1Roll
    global dice2Roll
    global totalDice
    dice1Roll = random.randint(0,5)
    dice2Roll = random.randint(0,5)

    totalDice = dice1Roll + 1 + dice2Roll + 1
    
    print(dice1Roll)
    print(dice2Roll)
    print(totalDice)
    return dice1Roll
    
def clearScreen():
    print('\n'*50)

randomRoll()
clearScreen()

def printBoard(numberList):
    out=(f"""
    ________________________________________________________________________________________________________________________
                      | 
    {numberList[0][0]}|    {numberList[0][1]} {numberList[0][2]} {numberList[0][3]}  {numberList[0][4]}    
                      |
    ------------------------------------------------------------------------------------------------------------------------|
                                                                                                        |
        {dice1List[dice1Roll]}|                                                                                                    |
                                                                                                        |
                                                                                                        |
                                                                                                        |
                                                                {dice2List[dice2Roll]}|                                                                                                    |
                                                                                                        |
                                                                                                        |
    _______________________________________________________________________________________________________________________|
            |         |   ___   |         |   ___   |   ___   |  ____   |   ___   |   ___   |     __  |         |         |
    /|    |   /`\   |      |  |   / |   |  |      |  |      |     /   |  |   |  |  |   |  | /| |  | |  /| /|  | /|  /`\ |
        |    |     /   |   ---|  |  /__|   |  '---,  |  |---,  |    /    |  |---|  |  `---|  |  | |  | |   |  |  |  |    / |
    _|_   |   /__   |   ___|  |     |   |   ___|  |  |___|  |   /     |  |___|  |   ___|  | _|_|__| |  _|__|_ | _|_ /__ |
    ------------------------------------------------------------------------------------------------------------------------
    """)
    print(out)
printBoard(numberList)
move=[]
while totalDice > 0:
    ui = int(input (f"you rolled a {totalDice} what tiles do you want down?: "))
    if ui > totalDice:
        print("NOT A MOVE")
    elif ui in move:                    #https://stackoverflow.com/questions/46915257/how-to-prevent-user-from-inputting-two-of-the-same-numbers
        print("Already picked")
    else:
        totalDice = totalDice-ui
        move.append(ui)
        print(totalDice) 
if playerVar=="0":
    playerVar="1"
elif playerVar=="1":
    playerVar="0"
for i in move:
    numberList[playerVar][i-1]= whitespace
print(numberList)
printBoard(numberList)     

