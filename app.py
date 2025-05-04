import streamlit as st
from PIL import Image
import random

# Load sprites
bird = Image.open("gallery/sprites/bird.png")
background = Image.open("gallery/sprites/background.png")
base = Image.open("gallery/sprites/base.png")
pipe = Image.open("gallery/sprites/pipe.png")
pipe_rotated = pipe.transpose(Image.FLIP_TOP_BOTTOM)

# Game constants
SCREENWIDTH = 289
SCREENHEIGHT = 511
GROUNDY = int(SCREENHEIGHT * 0.8)

if 'playerY' not in st.session_state:
    st.session_state.playerY = SCREENHEIGHT // 2
if 'pipes' not in st.session_state:
    st.session_state.pipes = []
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'velocity' not in st.session_state:
    st.session_state.velocity = 0
if 'flap' not in st.session_state:
    st.session_state.flap = False

def get_random_pipe():
    pipe_height = pipe.size[1]
    offset = SCREENHEIGHT / 3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - base.size[1] - 1.2 * offset))
    x = SCREENWIDTH + 10
    y1 = pipe_height - y2 + offset
    return {'x': x, 'y_upper': -y1, 'y_lower': y2}

def move_pipes():
    new_pipes = []
    for p in st.session_state.pipes:
        p['x'] -= 4
        if p['x'] > -pipe.size[0]:
            new_pipes.append(p)
    if not st.session_state.pipes or st.session_state.pipes[-1]['x'] < 140:
        new_pipes.append(get_random_pipe())
    st.session_state.pipes = new_pipes

def check_collision():
    if st.session_state.playerY >= GROUNDY or st.session_state.playerY <= 0:
        return True
    for p in st.session_state.pipes:
        px = p['x']
        py_up = p['y_upper']
        py_low = p['y_lower']
        playerx = 50
        if abs(px - playerx) < pipe.size[0]:
            if st.session_state.playerY < py_up + pipe.size[1] or st.session_state.playerY + bird.size[1] > py_low:
                return True
    return False

def update_frame():
    if st.session_state.flap:
        st.session_state.velocity = -9
    else:
        st.session_state.velocity = min(st.session_state.velocity + 1, 10)
    st.session_state.playerY += st.session_state.velocity
    move_pipes()

    for p in st.session_state.pipes:
        if abs(p['x'] + pipe.size[0] // 2 - 50) < 2:
            st.session_state.score += 1

    return check_collision()

# Title
st.title("🕹️ Flappy Bird (Streamlit Edition)")

# Controls
col1, col2 = st.columns(2)
with col1:
    flap_btn = st.button("Flap 🕊️")
    st.session_state.flap = flap_btn
with col2:
    if st.button("Reset 🔄"):
        st.session_state.playerY = SCREENHEIGHT // 2
        st.session_state.pipes = []
        st.session_state.score = 0
        st.session_state.velocity = 0

# Update game frame
game_over = update_frame()

# Draw the screen
canvas = Image.new("RGB", (SCREENWIDTH, SCREENHEIGHT))
canvas.paste(background, (0, 0))
for p in st.session_state.pipes:
    canvas.paste(pipe_rotated, (p['x'], p['y_upper']), pipe_rotated)
    canvas.paste(pipe, (p['x'], p['y_lower']), pipe)
canvas.paste(base, (0, GROUNDY), base)
canvas.paste(bird, (50, int(st.session_state.playerY)), bird)

st.image(canvas, caption=f"Score: {st.session_state.score}", use_column_width=True)

if game_over:
    st.error("💥 Game Over! Click Reset to try again.")

