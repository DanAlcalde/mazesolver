from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "red")
    l = Line(Point(150, 50), Point(220, 400))
    win.draw_line(l, "blue")
    
    win.wait_for_close()

main()