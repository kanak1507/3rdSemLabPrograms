colors = ["Red", "Green", "Golden", "Blue", "Yellow"]
states = ["A", "B", "C", "D"]
neighbours = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"],
}
colors_assigned = {}
for state in states:
  neighbor_colors = [colors_assigned.get(n) for n in neighbours[state]]
  for color in colors:
    if color not in neighbor_colors:
      colors_assigned[state] = color
      break
print(colors_assigned)
