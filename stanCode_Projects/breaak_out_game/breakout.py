"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Make a Breakout Bricks game
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():


    rate = FRAME_RATE     # To speed up
    lives = NUM_LIVES     # Easy to set lives
    graphics = BreakoutGraphics()

    while lives > 0:
        graphics.check()            # Determine the state of the ball and other objects
        graphics.faster(rate)       # Speed up the game

        if graphics.lose():         # Determine whether to lose
            graphics.reset()        # Reset the position and speed of the ball
            lives = graphics.lives_time(lives)
            graphics.print_lives()


        pause(rate)

    graphics.end()





    # Add animation loop here!


if __name__ == '__main__':
    main()
