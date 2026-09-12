import pgzrun
WIDTH=250
HEIGHT=250
def draw():
    screen.fill("blue")
    roof=Rect((13,15),(145,15))
    screen.draw.filled_rect(roof,"white")
    Housebody=Rect((22, 29), (130, 59))
    screen.draw.filled_rect(Housebody, "green")
    Window=Rect((34, 57), (18, 19))
    screen.draw.filled_rect(Window, "red")
    Doorline=Rect((70,40),(30,50))
    screen.draw.filled_rect(Doorline,"indigo")
pgzrun.go()