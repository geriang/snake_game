from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.color("White")
        self.update_board()
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))



