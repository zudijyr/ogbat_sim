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

    p1 = win.getMouse()
    image1 = Image(p1,'blue_fighter.gif')
    image1.draw(win)
    p1 = win.getMouse()
    image2 = Image(p1,'blue_fighter.gif')
    image2.draw(win)
    p1 = win.getMouse()
    image3 = Image(p1,'blue_amazon.gif')
    image3.draw(win)
    p1 = win.getMouse()
    image4 = Image(p1,'blue_amazon.gif')
    image4.draw(win)

    p1 = win.getMouse()
    image1 = Image(p1,'red_fighter.gif')
    image1.draw(win)
    p1 = win.getMouse()
    image2 = Image(p1,'red_fighter.gif')
    image2.draw(win)
    p1 = win.getMouse()
    image3 = Image(p1,'red_amazon.gif')
    image3.draw(win)
    p1 = win.getMouse()
    image4 = Image(p1,'red_amazon.gif')
    image4.draw(win)


    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()
