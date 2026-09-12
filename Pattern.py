import pgzrun
WIDTH=300
HEIGHT=300
def draw():
    screen.fill("black")
    w=300
    h=50
    for i in range(25):
        r1=Rect((0,70),(w,h))
        r1.center=150,150
        screen.draw.rect(r1,"green")
        w=w-10
        h=h+10
pgzrun.go()