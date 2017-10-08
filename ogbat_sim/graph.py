from graphics import *

def main():
    win = GraphWin('Draw units', 700, 500)
    win.setBackground('gray')

    p2 = Point(350,250)
    background = Image(p2,'tiles.gif')
    background.draw(win)

    message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    image1 = Image(Point(600,400),'blue_fighter.gif')
    image1.draw(win)
    image2 = Image(Point(650,380),'blue_fighter.gif')
    image2.draw(win)
    image3 = Image(Point(600,440),'blue_amazon.gif')
    image3.draw(win)
    image4 = Image(Point(640,420),'blue_amazon.gif')
    image4.draw(win)

    image5 = Image(Point(200,200),'red_fighter.gif')
    image5.draw(win)
    image6 = Image(Point(250,180),'red_fighter.gif')
    image6.draw(win)
    image7 = Image(Point(210,150),'red_amazon.gif')
    image7.draw(win)
    image8 = Image(Point(260,140),'red_amazon.gif')
    image8.draw(win)


    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()
