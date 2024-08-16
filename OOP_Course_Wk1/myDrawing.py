from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rectangle1 = Rectangle()
oval1 = Oval()
triangle1 = Triangle(10, 10, 5, 100, 75, 75)

rectangle1.set_color("black")
rectangle1.set_height(100)
rectangle1.set_width(200)
rectangle1.set_x(-20)

rectangle1.draw()

oval1.randomize()

oval1.draw()

triangle1.draw()

paper.display()