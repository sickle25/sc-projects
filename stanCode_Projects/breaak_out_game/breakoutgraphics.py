"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Make a Breakout Bricks game
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.pw = paddle_width
        self.ph = paddle_height
        self.paddle = GRect(self.pw,self.ph ,x=(self.window_width-self.pw)/2, y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.bra = ball_radius*2
        self.ball = GOval(self.bra,self.bra)
        self.ball.filled = True
        self.window.add(self.ball,(self.window_width-self.bra)/2,(self.window_height-self.bra)/2)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0


        # Initialize our mouse listeners.
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)


        # Draw bricks.
        self.build_bricks()


        self.score = 0
        self.score_text = GLabel('Score: ' +str(self.score))
        self.score_text.font = '-15-bold'
        self.window.add(self.score_text, 0, self.window_height)

        self.lives_text = GLabel('Lives: ' + str(3))
        self.lives_text.font = '-15-bold'
        self.window.add(self.lives_text, self.window_width - 80, self.window_height)

    def build_bricks(self):
        """

        :return: Build bricks
        """
        self.br = BRICK_ROWS
        self.bc = BRICK_COLS
        for i in range(self.br):
            for j in range(self.bc):
                self.bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT,x=i * (BRICK_WIDTH + BRICK_SPACING), y=j * (BRICK_HEIGHT + BRICK_SPACING))
                self.bricks.filled = True
                if j < 5:
                    self.bricks.fill_color = 'red'
                else:
                    self.bricks.fill_color = 'blue'

                self.window.add(self.bricks)


    def paddle_move(self,e):
        """

        :param e: Mouse position
        :return: Only change the X-axis position of the mouse
        """
        if self.pw/2 < e.x < self.window_width - self.pw/2 :
             self.paddle.x = e.x - self.paddle.width/2

    def ball_move(self,e):
        """

        :return: Give the ball x and y speed
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if (random.random() > 0.5):
            self.__dx = -(self.__dx)

    def check(self):
        """

        :return: Determine the state of the ball and other objects
        """

        # Avoid the ball beyond the window
        if self.ball.x < 0 or self.ball.x > (self.window_width - self.bra):
            self.__dx *= -1
        if self.ball.y < 0 or self.ball.y > (self.window_height - self.bra):
            self.__dy *= -1


        # Record old scores
        self.old_score = self.score


        # Set four points as the judgment state
        maybe_object1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_object2 = self.window.get_object_at(self.ball.x + self.bra, self.ball.y)
        maybe_object3 = self.window.get_object_at(self.ball.x, self.ball.y + self.bra)
        maybe_object4 = self.window.get_object_at(self.ball.x + self.bra, self.ball.y + self.bra)


        # Judgment points and the status of bricks
        if maybe_object1 is not self.paddle and maybe_object2 is not self.paddle and \
                maybe_object3 is not self.paddle and maybe_object4 is not self.paddle \
                and maybe_object1 is not self.lives_text and maybe_object2 is not self.lives_text \
                and maybe_object3 is not self.lives_text and maybe_object4 is not self.lives_text \
                and maybe_object1 is not self.score_text and maybe_object2 is not self.score_text \
                and maybe_object3 is not self.score_text and maybe_object4 is not self.score_text:

            while True:
                if maybe_object1 is not None or maybe_object2 is not None:
                    if maybe_object1 is not None and maybe_object2 is not None:
                        self.window.remove(maybe_object1)
                        self.window.remove(maybe_object2)
                        self.__dy *= -1
                        if maybe_object1 is maybe_object2:
                            self.score += 1
                        else:
                            self.score += 2
                    else:
                        if maybe_object1 is not None:
                            self.window.remove(maybe_object1)
                            self.__dy *= -1
                            self.score += 1
                        else:
                            self.window.remove(maybe_object2)
                            self.__dy *= -1
                            self.score +=1

                if maybe_object2 is not None or maybe_object4 is not None:
                    if maybe_object2 is not None and maybe_object4 is not None:
                        self.window.remove(maybe_object2)
                        self.window.remove(maybe_object4)
                        self.__dx *= -1
                        if maybe_object2 is maybe_object4:
                            self.score += 1
                        else:
                            self.score += 2
                    else:
                        if maybe_object4 is not None:
                            self.window.remove(maybe_object4)
                            self.__dx *= -1
                            self.score +=1

                if maybe_object1 is not None or maybe_object3 is not None:
                    if maybe_object1 is not None and maybe_object3 is not None:
                        self.window.remove(maybe_object1)
                        self.window.remove(maybe_object3)
                        self.__dx *= -1
                        if maybe_object1 is maybe_object3:
                            self.score += 1
                        else:
                            self.score += 2
                    else:
                        if maybe_object3 is not None:
                            self.window.remove(maybe_object3)
                            self.__dx *= -1
                            self.score += 1
                break


        # Judgment point and paddle state
        if maybe_object3 is self.paddle or maybe_object4 is self.paddle:
            self.__dy *= -1
            self.ball.move(0,-10)


        # If the score changes, change the score on the window
        if self.old_score != self.score:
            self.score_text.text = 'Score: ' + str(self.score)
            self.window.add(self.score_text, 0, self.window_height)


        # After the inspection, the ball moves
        self.ball.move(self.__dx,self.__dy)


    def reset(self):
        """
        Reset the position and speed of the ball
        """
        self.ball.x=(self.window_width-self.bra)/2
        self.ball.y=(self.window_height-self.bra)/2
        self.__dx = 0
        self.__dy = 0


    def lose(self):
        """

        :return:(bool)  Check if the ball is under the paddle
        """
        ball_lose = self.ball.y > self.paddle.y + 15

        return ball_lose


    def lives_time(self,lives):
        """

        :param lives: (int) The number of times you can play
        :return: (int) Remaining times
        """
        lives -= 1
        self.lives = lives

        return lives


    def print_lives(self):

        self.lives_text.font = '-15-bold'
        self.lives_text.text = 'Lives: ' + str(self.lives)
        self.window.add(self.lives_text, self.window_width - 80, self.window_height)


    def faster(self,rate):
        '''

        :param rate: (int) Game speed
        :return: (int) Speed of the game after acceleration
        '''
        rate += self.score*0.01
        return rate


    def end(self):
        """

        :return: End screen
        """
        pic = GRect(self.window_width,self.window_height)
        pic.filled = True
        pic.fill_color = 'gold'
        end_word = GLabel('Your score: ' + str(self.score))
        end_word.font = '-20-bold'
        self.window.add(pic)
        self.window.add(end_word,self.window_width/4+30, self.window_height/2)
