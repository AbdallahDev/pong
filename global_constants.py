# Global constants file

# main file

# arena file
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = 'Pong'
PROMPT_TITLE = "Play"
PROMPT_TXT = 'Do you want to play the game (y/n)?'
NET_COORDINATES = [(0, 250), (0, 200), (0, 150), (0, 100), (0, 50), (0, 0), (0, -50), (0, -100),
                   (0, -150), (0, -200), (0, -250), ]
NET_SEGMENT_WIDTH = 2
NET_SEGMENT_LENGTH = 0.25

# paddle file
PADDLE_SEGMENT_WIDTH = 0.5
R_PADDLE_COORDINATES = [(380, 20), (380, 0), (380, -20)]
L_PADDLE_COORDINATES = [(-380, 20), (-380, 0), (-380, -20)]

# segment file
SEGMENT_STEPS = 20
CEILING_HIT_POINT = (SCREEN_HEIGHT / 2)
FLOOR_HIT_POINT = -(SCREEN_HEIGHT / 2)

# ball file
BALL_SHAPE = 'circle'
