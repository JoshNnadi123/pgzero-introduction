import pgzrun
HEIGHT=400
WIDTH=400
def draw():
    screen.fill("green")
    rbody=Rect((150,150),(100,80))
    screen.draw.rect(rbody,"blue")
    rightleg=Rect((210,230),(25,70))
    screen.draw.rect(rightleg,"blue")
    leftleg=Rect((170,230),(25,70))
    screen.draw.rect(leftleg,"blue")
    neck=Rect((175,140),(50,10))
    screen.draw.rect(neck,"blue")
    head=Rect((150,60),(100,80))
    screen.draw.rect(head,"blue")
    head2=Rect((160,70),(80,60))
    screen.draw.rect(head2,"blue")
pgzrun.go()