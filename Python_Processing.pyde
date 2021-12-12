barX = 300
barY = 600             
ballX = 0
ballY = 0              
speedX = 0
speedY = 0             
barH = 20
barW = 60           
block_X = 0
block_Y = 0     
blocks = []
x = 0
y = 0
name_Pattern = 0
nouse_Count=0
out = 0
d = 0
x1=0;x2=0


def setup():
    global ballX, ballY, speedX, speedY, d
    
    size(800, 800)      
    ballX = width/2      
    ballY = height*5/8    
    barX = 300         
    barY = 600           
    speedX = 3.0        
    speedY = 3.0    
    d = 30
    block()
    
def draw():
    global ballX, ballY, barX, barY, speedX, speedY, barH, bar
    background(0) 
    fill(255)
    rect(barX, barY, barW*2, barH*2)
    ellipse(ballX, ballY, d, d)   
    play()       
    block_delete()
    in_block()
    
    if keyPressed:
        if key == CODED:                        
            if keyCode == LEFT or RIGHT:       
                barY = 600.0                     
                if keyCode == RIGHT:         
                    barX += 5.0                  
                    if (barX > width-barW*2):          
                        barX = width-barW*2          
                elif keyCode == LEFT:        
                    barX -= 5.0               
                    if (barX < 0):            
                        barX = 0         
                                
    if out == 0:                                  
        ballX += speedX                        
        if ballX <= d or ballX >= width - d:    
            speedX *= -1                        
        
        ballY += speedY                     
        if ballY < d or ballY >= height - d:  
            speedY *= -1                       
    
        if ((barX < ballX) and (barX+barW*2 > ballX)) and ((barY < ballY+d) and (barY+barH*2 > ballY+d)) : 
            speedY *= -1 
    
    if out == -1:
        background(255)
        fill(0)
        textSize(130)
        strokeWeight(90)
        text('GAME OVER', 10, 150)
        outName()
        
    if out == 1:
        background(255)
        fill(0)
        textSize(110)
        strokeWeight(50)
        text('Congatulation!', 20, 130)
        creaName()
    
    
def play():
    global out
    if ballY >= height-d:
        out = -1
        
    for block in blocks:
        if block['OK']:
            return
    out = 1
        
def block():
    global block_X, block_Y, blocks
    for i in range(8):
        for j in range(8):
            block_X = 0+i*100
            block_Y = 0+j*50
            block = {'x':block_X, 'y':block_Y, 'OK':True}
            blocks.append(block)
            
def in_block():
    for block in blocks:
        if block['OK']:
            fill(255, 0, 0)
            rect(block['x'], block['y'], 100, 50)

def block_delete():
    global speedY
    for block in blocks:
        if (ballX > block['x']) and (ballX < block['x']+100) and (ballY > block['y']) and  (ballY < block['y']+40) and block['OK']:
            block['OK'] = False
            speedY *= -1
        
def outName():
    stroke(255, 0, 0)
    strokeWeight(50)
    line(50, 400, 350, 400)
    line(200, 300, 200, 650)
    line(200, 400, 50, 650)
    line(200, 400, 350, 650)
    
    line(450, 400, 750, 400)
    line(600, 300, 600, 400)
    line(525, 400, 525, 650)
    line(675, 400, 675, 650)
    line(450, 650, 750, 650)
    
def creaName():
    global x1, x2
    frameRate(2)
    stroke(random(255), random(255), random(255))
    strokeWeight(50)
    if x1<400:
        x1+=20
    line(-300+x1, 350, -50+x1, 350)
    line(-175+x1, 250, -175+x1, 550)
    line(-175+x1, 350, -295+x1, 550)
    line(-175+x1, 350, -45+x1, 550)
    
    if x2>-400:
        x2-=20
    line(850+x2, 350, 1100+x2, 350)
    line(975+x2, 250, 975+x2, 350)
    line(912+x2, 350, 912+x2, 550)
    line(1032+x2, 350, 1032+x2, 550)
    line(850+x2, 550, 1100+x2, 550) 
