import os.path
import random

import pythonGraph


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
START_BALLS = 3


# Generates common ball attributes to adds to parallel lists
def fill_values(ball_dx, ball_dy, ball_color):
    pythonGraph.play_sound_effect(os.path.join(os.path.dirname(__file__),
                                               'media', 'magic-wand.ogg'))
    while True:
        dx = random.randrange(-4, 4)
        dy = random.randrange(-4, 4)
        if dx != 0 and dy != 0:
            break
    ball_dx.append(dx)
    ball_dy.append(dy)
    ball_color.append(pythonGraph.create_color(random.randrange(0, 255),
                                               random.randrange(0, 255),
                                               random.randrange(0, 255)))


# Generates ball attributes and adds to parallel lists when space bar is
# clicked or upon initial execution
def make_ball(ball_x, ball_y, ball_dx, ball_dy, ball_size, ball_color):
    size = random.randrange(4, 45)
    ball_size.append(size)
    ball_x.append(random.randrange(size, SCREEN_WIDTH - size))
    ball_y.append(random.randrange(size, SCREEN_HEIGHT - size))
    fill_values(ball_dx, ball_dy, ball_color)


# Generates ball attributes and adds to parallel lists when mouse is clicked
def place_ball(ball_x, ball_y, ball_dx, ball_dy, ball_size, ball_color, x, y):
    ball_size.append(random.randrange(4, 45))
    ball_x.append(x)
    ball_y.append(y)
    fill_values(ball_dx, ball_dy, ball_color)


def main():
    # Define parrallel lists to store ball attributes
    ball_x = []
    ball_y = []
    ball_dx = []
    ball_dy = []
    ball_size = []
    ball_color = []

    # Setup tasks for window and sound
    pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
    pythonGraph.set_window_title("Bounce Balls")

    # Generate number of starting balls
    for i in range(START_BALLS):
        make_ball(ball_x, ball_y, ball_dx, ball_dy, ball_size, ball_color)

    # Animation loop
    while pythonGraph.window_not_closed():

        # Erase items in offscreen buffer
        pythonGraph.clear_window(pythonGraph.colors.WHITE)

        # Move / check boudries for each ball
        for i in range(len(ball_x)):
            # Move the ball's center
            ball_x[i] += ball_dx[i]
            ball_y[i] += ball_dy[i]

            # Bounce the ball if needed
            if (ball_y[i] > SCREEN_HEIGHT - ball_size[i] or
                    ball_y[i] < ball_size[i]):
                ball_dy[i] *= -1
            if (ball_x[i] > SCREEN_WIDTH - ball_size[i] or
                    ball_x[i] < ball_size[i]):
                ball_dx[i] *= -1

            # Draw (i)th ball to the offscreen buffer
            pythonGraph.draw_circle(ball_x[i], ball_y[i], ball_size[i],
                                    ball_color[i], True)

        # Draw the number of balls to the offscreen buffer
        pythonGraph.draw_text("Number of Balls: " + str(len(ball_x)),
                              SCREEN_WIDTH - 210, 5, pythonGraph.colors.BLACK,
                              30)

        # Handle quit, mouse, and keyboard events
        if pythonGraph.key_pressed('space'):
            make_ball(ball_x, ball_y, ball_dx, ball_dy, ball_size, ball_color)

        # Left mouse button was pressed
        if pythonGraph.mouse_button_pressed(pythonGraph.mouse_buttons.LEFT):
            x = pythonGraph.get_mouse_x()
            y = pythonGraph.get_mouse_y()
            place_ball(ball_x, ball_y, ball_dx, ball_dy, ball_size, ball_color,
                       x, y)

        if pythonGraph.key_pressed('q'):
            pythonGraph.close_window()

        # display items drawn to offscreen buffer to the screen
        pythonGraph.update_window()


if __name__ == "__main__":
    main()
