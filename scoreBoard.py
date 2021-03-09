from turtle import Turtle
FONT = ("courier", 22, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore: {self.highscore}", align="center", font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreBoard()
    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align="center", font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreBoard()


