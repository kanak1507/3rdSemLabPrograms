import turtle

# Setup window canvas
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#1a1a2e") # Dark background makes the lily colors pop

t = turtle.Turtle()
t.speed(0) # Fastest drawing speed
t.pensize(2)

def draw_tapered_petal(radius, angle, steps=15):
    """Draws a more organic, tapered lily petal with sharp tips."""
    # Left side curve
    for i in range(steps):
        t.forward(radius / steps)
        t.left(angle / steps)
    t.left(180 - angle)
    # Right side curve back
    for i in range(steps):
        t.forward(radius / steps)
        t.left(angle / steps)
    t.left(180 - angle)

def draw_petal_veins(length):
    """Draws detailed texture lines inside the petal for realism."""
    t.penup()
    t.forward(20)
    t.pendown()
    t.color("#e94560") # Darker pink/magenta for inner texture lines
    t.pensize(1)
    
    # Main center vein
    t.forward(length - 40)
    
    # Small branching veins
    for distance, branch_angle in [(0.3, 20), (0.5, 25), (0.7, 30)]:
        t.backward(length * 0.2)
        # Left branch
        t.left(branch_angle)
        t.forward(25)
        t.backward(25)
        t.right(branch_angle * 2)
        # Right branch
        t.forward(25)
        t.backward(25)
        t.left(branch_angle)

def jump_to_center():
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

# ==========================================
# 1. DRAW LAYER 1: Large Outer Petals
# ==========================================
for i in range(6):
    jump_to_center()
    t.left(i * 60)
    
    t.color("#e94560", "#ff9a9e") # Magenta borders, soft pink fill
    t.begin_fill()
    draw_tapered_petal(180, 55)
    t.end_fill()
    
    # Draw texture inside outer petal
    t.left(27.5) # Align to center line of the petal
    draw_petal_veins(180)

# ==========================================
# 2. DRAW LAYER 2: Intersecting Inner Petals
# ==========================================
for i in range(6):
    jump_to_center()
    t.left(i * 60 + 30) # Offset by 30 degrees to fill gaps
    
    t.color("#ff2e63", "#fecfef") # Richer pink borders, lighter fill
    t.begin_fill()
    draw_tapered_petal(150, 50)
    t.end_fill()
    
    # Draw texture inside inner petal
    t.left(25) # Align to center line of the petal
    draw_petal_veins(150)

# ==========================================
# 3. DRAW DETAILED STAMENS (Filaments & Anthers)
# ==========================================
stamen_angles = [15, 75, 135, 195, 255, 315]
for angle in stamen_angles:
    jump_to_center()
    t.left(angle)
    
    # Filament (The thin stalk)
    t.color("#e2f3f5") # Pale greenish white
    t.pensize(3)
    t.forward(60)
    
    # Anther (The pollen head at the tip)
    t.pensize(1)
    t.color("#b83b5e", "#f08a5d") # Deep red border, orange/gold pollen fill
    t.begin_fill()
    
    # Draw a little oval bead for the pollen anther
    for _ in range(2):
        t.circle(8, 90)
        t.circle(4, 90)
    t.end_fill()

# ==========================================
# 4. DRAW CENTRAL PISTIL
# ==========================================
jump_to_center()
t.color("#3ec1d3") # Distinct mint green center
t.pensize(5)
t.forward(15)
t.dot(14, "#ffbc12") # Three-lobed stigma style representation

# Hide and complete
t.hideturtle()
turtle.done()
