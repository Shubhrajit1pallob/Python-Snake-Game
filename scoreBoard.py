from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open('data.txt') as score:
            self.high_score = int(score.read())
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.pendown()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center",
                   font=('Ariel', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as score:
                score.write(str(self.high_score))

        self.score = 0

        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
