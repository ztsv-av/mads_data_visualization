fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_xlabel('X (Distance from Star)')
ax.set_ylabel('Y (Distance from Star)')
ax.set_title('Animated 2D Plot of Planets Orbiting a Star')

# Initialize scatter plots for each planet
planets, = ax.plot([], [], '.', markersize=4)

# Star
star, = ax.plot(0, 0, 'o', markersize=3, color="yellow")

plt.grid(False)

# Function to initialize the plot
def init():
    planets.set_data([], [])
    return planets,

# Function to update the plot in each animation frame
def update(i):
    planets.set_data(x_positions[i % num_frames, :], y_positions[i % num_frames, :])
    return planets,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=200, repeat=False)

# Save the animation
ani.save('planets_orbiting_star_animation2.gif', writer='pillow', fps=30)

# Show the plot
plt.show()