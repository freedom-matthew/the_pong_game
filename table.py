from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


class Table:
    def __init__(self):
        self.screen = Screen()
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.r_paddle = Paddle((350, 0))
        self.l_paddle = Paddle((-350, 0))
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(self.r_paddle.go_up, "Up")
        self.screen.onkeypress(self.r_paddle.go_down, "Down")
        self.screen.onkeypress(self.l_paddle.go_up, "w")
        self.screen.onkeypress(self.l_paddle.go_down, "s")

    def start_game(self):        
        game_is_on = True
        while game_is_on:
            self.screen.update()
            self.ball.move()
            time.sleep(self.scoreboard.move_speed)
        
            # Detect collision with wall
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()
        
            # Detect collision with paddle
            if self.ball.distance(self.r_paddle) < 50 and self.ball.xcor() > 320 or self.ball.distance(self.l_paddle) < 50 and self.ball.xcor() < -320:
                self.ball.bounce_x()
        
            # Detect right paddle misses
            if self.ball.xcor() > 380:
                self.ball.reset_position()
                self.scoreboard.left_point()
        
            # Detect left paddle misses:
            if self.ball.xcor() < -380:
                self.ball.reset_position()
                self.scoreboard.right_point()
        
        self.screen.exitonclick()
