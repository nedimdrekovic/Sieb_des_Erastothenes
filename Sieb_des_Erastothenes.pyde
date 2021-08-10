from Cell import Cell

def setup():
    '''
    Method is called before draw method to set up basic settings of the application.
    '''
    global board, colors, currentColor
    if n >= 800:
        print("Choose a number in [10, 800] otherwise the board is too small to show all numbers")
        return   
    size(heightSize, widthSize)
    background(200)    # background color
    stroke(100)    # strokes lines white
    
    # fill board with cells
    for row in range(ceil(n / 10.0)):
        board.append([])
        for column in range(10):  # 10 numbers for each row
            board[row].append(Cell())

    for i in range(len(board)):
        line(0, float(width / float(len(board))) * i,
             width, float(width / float(len(board))) * i)    # draw horizontal lines

    for i in range(10):
        line(float(height / 10) * i, 0,
             float(height / 10) * i, height)    # draw vertical lines

    # maximal number of colors is defined by the square roots length of the board
    colors = [(173, 216, 230), (153, 255, 204), (153, 255, 255), (255, 229, 204), (204, 255, 229), (200, 240, 220), (120, 180, 255), (155, 255, 200)]
    more_colors = [(255, 204, 204), (229, 204, 255), (255, 255, 204), (240, 230, 140), (224,255,255), (170, 200, 210), (130, 255, 180), (100, 150, 200)]
    colors.extend(more_colors)

    currentColor = colors[int(random(len(colors)))]    # select first random color

def draw():
    '''
    Loops until it has been stopped.
    '''
    global counter, multiple, currentColor, colors, board
    
    if n >= 800:
        fill(255, 0, 0)
        textSize(15)
        text("Choose a number in [10, 800] otherwise the board is too small to show all numbers", 10, 30)
        noLoop()
        return

    if counter * counter < n:
        if not board[(multiple - 1)/10][(multiple - 1)%10].prime:
            board[(multiple-1)/10][(multiple-1)%10].prime = True    # avoids coloring on blocks that are aleady colored
            board[(multiple - 1) / 10][(multiple - 1) % 10].col = (currentColor[0], currentColor[1], currentColor[2])    # add color

            # draw colored rect
            fill(board[(multiple - 1) / 10][(multiple - 1) % 10].col[0], board[(multiple - 1) / 10][(multiple - 1) % 10].col[1], board[(multiple - 1) / 10][(multiple - 1) % 10].col[2])
            rect((widthSize / 10) * ((multiple-1) % 10), (height / float(len(board))) * ((multiple-1) / 10), (widthSize / 10), (height / float(len(board))))

    # mark prime numbers
    if not board[(counter - 1)/10][(counter - 1)%10].prime:
        # color current prime number
        board[(counter - 1) / 10][(counter - 1) % 10].col = (255, 0, 0)

        # color prime number
        fill(board[(counter - 1) / 10][(counter - 1) % 10].col[0], board[(counter - 1) / 10][(counter - 1) % 10].col[1], board[(counter - 1) / 10][(counter - 1) % 10].col[2])
        rect((widthSize / 10) * ((counter-1) % 10), (height / float(len(board))) * ((counter-1) / 10), (widthSize / 10), (height / float(len(board))))
    

    # multiple of current prime number
    multiple += counter

    # select next prime number when n is reached
    if multiple > n:
        #if not board[(counter - 1)/10][(counter - 1)%10].prime:        # print current prime number
        #    print(counter)

        # increase counter for prime number and skip non primes
        while counter < n:
            counter += 1
            if not board[(counter - 1)/10][(counter - 1)%10].prime:
                break

        # set new starting multiple point of next prime number 
        multiple = counter + counter
        
        # remove last used color to avoid that color is used twice but only if color has been used (cause the cells has been colored already
        if any(cell for row in board for cell in row if cell.col == currentColor):
            colors = colors[:colors.index(currentColor)] + colors[(colors.index(currentColor)+1):]

        # if no colors are available anymore
        if len(colors) == 0:
            colors = [100 + int(random(156)), 155 + int(random(101)), 255 - int(random(101))]

        # select new color
        currentColor = colors[int(random(len(colors)))]

    drawNumbers()

    # stop when all prime numbers are known
    if counter > n:
        print("Alle Primzahlen bekannt.")
        noLoop()

    # stop for a moment
    delay(delay_time)

def drawNumbers():
    '''
    Draw numbers and their size and position.
    '''
    for r in range(len(board)):
        for c in range(len(board[r])):
            if 0 < (10 * r + c) < n:
                # highlighting prime number by coloring its text
                if board[r][c].col == (255, 0, 0):    
                    fill(255, 255, 0)
                else:
                    fill(100)
                
                # x and y text positions for numbers
                if (10 * r + c + 1) < 10:
                    xx = (widthSize / 10) * c + 0.1 * (width / 10.0)
                elif (10 * r + c + 1) < 100:
                    xx = (widthSize / 10) * c + 0.05 * (width / 10.0)
                else: # for all numbers >= 100
                    xx = (widthSize / 10) * c + 0.025 * (width / 10.0)
                yy = (height / (n / 10.0)) * (r+1)
                
                # draw text depending on its size (determined numbers for a certain n)
                if n <= 300:
                    textSize(30 - n * 0.05)
                elif 300 < n < 450:
                    textSize(20)
                else:
                    textSize(12)

                text(10 * r + c + 1, xx, yy)

# only written to illustrate how the algorithm works (not used here)
def sieve_of_erastothenes(n):
    '''
    Prints a list containing all prime numbers in [2,n]
    '''
    # computes prime numbers in [2,n]
    prime_numbers = [False for i in range(n)]
    for prime in range(2, len(prime_numbers)):
        if not prime_numbers[prime - 1]:
            for multiple in range(prime * prime, n + 1, prime):
                prime_numbers[multiple - 1] = True
    prime_numbers = [(index+1) for index in range(1, len(prime_numbers)) if not prime_numbers[index]]
    return prime_numbers

def print_board(board):
    '''
    This method prints the board that contains all the numbers betweetn 2 and n
    '''
    for row in range(len(board)):
        for column in range(len(board[row])):
            print(board[row][column])

if __name__ == '__main__':
    '''
    Main method (called before setup method)
    '''
    board = []    # empty board that has to be filled with numbers in [2, n]
    counter = 2    # counter for prime number
    n = 450    # upper bound assuming n can be divided by 10 resulting an integer
    multiple = counter + counter    # counts the multiples of current prime number
    colors = []    # colors for drawing the squares
    currentColor = None    # current color 
    delay_time = 1    # delayed time to iterate through entire tree
    heightSize = 400 if n <= 300 else 700
    widthSize = heightSize    # assuming that height and width are equal
    
    print("Primzahlen im Intervall (1, " + str(n) + "]:")
    print(sieve_of_erastothenes(n))
