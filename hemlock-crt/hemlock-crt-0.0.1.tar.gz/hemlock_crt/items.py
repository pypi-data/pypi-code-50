"""Cognitive Reflection Test (CRT) items"""

from hemlock import *

BALL_BAT_TXT = """
<p>A bat and ball cost $1.10 in total. The bat costs $1.00 more than the ball.</p>
<p>How much does the ball cost?</p>
"""

def gen_ball_bat_q():
    ball_bat_q = Input(label=BALL_BAT_TXT, prepend='$')
    Validate.is_type(ball_bat_q, float)
    Submit.data_type(ball_bat_q, float)
    return ball_bat_q

ball_bat = {
    'var': 'CRT.BallBat',
    'gen_question': gen_ball_bat_q,
    'correct': .05,
    'intuitive': .10
}

MACHINES_TXT = """
<p>If it takes 5 machines 5 minutes to make 5 widgets, how many minutes would it take 100 machines to make 100 widgets?
"""

def gen_machines_q():
    machines_q = Input(label=MACHINES_TXT, append='minutes')
    Validate.is_type(machines_q, float)
    Submit.data_type(machines_q, float)
    return machines_q

machines = {
    'var': 'CRT.Machines',
    'gen_question': gen_machines_q,
    'correct': 5,
    'intuitive': 100
}

LILY_PADS_TXT = """
<p>In a lake, there is a patch of lily pads. Every day, the patch doubles in size.</p>
<p>If it takes 48 days for the patch to covert the entire lake, how many days would it take for the patch to covert half of the lake?</p>
"""

def gen_lily_pads_q():
    lily_pads_q = Input(label=LILY_PADS_TXT, append='days')
    Validate.is_type(lily_pads_q, float)
    Submit.data_type(lily_pads_q, float)
    return lily_pads_q

lily_pads = {
    'var': 'CRT.LilyPads',
    'gen_question': gen_lily_pads_q,
    'correct': 47,
    'intuitive': 24
}