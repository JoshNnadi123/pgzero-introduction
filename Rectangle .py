import pgzrun
WIDTH=350
HEIGHT=350
def draw():
    screen.fill("Blue")
    r1=Rect((250,250),(100,50))
    r1.center=250,250
    screen.draw.rect(r1,"green")
    r2=Rect((350,20),(50,100))
    screen.draw.rect(r2,"red")
    r3=Rect((100,370),(50,50))
    screen.draw.rect(r3,"yellow")
pgzrun.go()