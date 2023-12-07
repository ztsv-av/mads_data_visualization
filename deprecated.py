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

# ------------------------

fig, axs = plt.subplots(2, 1, figsize=(16, 8))
fig.suptitle("Distance from Star, Orbital Period and Planet's Temperature", fontsize=16)

axs[0].set_xlim(0, 1)
axs[0].set_ylim(0, 500)
axs[0].set_xlabel('Distance from Star', fontsize=12)
axs[0].set_ylabel('Orbital Period', fontsize=12)
axs[0].set_title('How Distance and Orbital Period relate to Temperature', fontsize=12)

scatter = axs[0].scatter(x=solar_exo_animation['pl_orbsmax'], 
                         y=solar_exo_animation['pl_orbper'], 
                         c=solar_exo_animation['pl_eqt'],
                         s=solar_exo_animation['pl_rade'], 
                         cmap='viridis', alpha=0.6)
sns.regplot(
    x=data_regplot1['pl_orbsmax'], 
    y=data_regplot1['pl_orbper'],
    scatter=False,
    ax=axs[0],
    color='#0a456e', 
    label='Regression Line',
    ci=None, 
    truncate=True
)

axs[1].set_xlim(0, 0.2)
axs[1].set_ylim(0, 50)
axs[1].set_xlabel('Distance from Star', fontsize=12)
axs[1].set_ylabel('Orbital Period', fontsize=12)
axs[1].set_title('How Distance and Orbital Period relate to Temperature (Closer Look)', fontsize=12)

scatter = axs[1].scatter(x=solar_exo_animation['pl_orbsmax'], 
                         y=solar_exo_animation['pl_orbper'], 
                         c=solar_exo_animation['pl_eqt'],
                         s=solar_exo_animation['pl_rade'], 
                         cmap='viridis', alpha=0.6)
sns.regplot(
    x=data_regplot2['pl_orbsmax'], 
    y=data_regplot2['pl_orbper'],
    scatter=False,
    ax=axs[1],
    color='#0a456e', 
    label='Regression Line',
    ci=None, 
    truncate=True
)

axs_bottom = plt.subplot(2, 1, 2)
axs_bottom.set_xlim(-5, 5)
axs_bottom.set_ylim(-15, 15)
axs_bottom.set_xlabel('Distance from Star', fontsize=12)
axs_bottom.set_ylabel('Distance from Star', fontsize=12)
axs_bottom.set_title('Distance from Star and Orbital Period, Illustrated', fontsize=12)

norm = Normalize(vmin=solar_exo_animation['pl_eqt'].min(), vmax=solar_exo_animation['pl_eqt'].max())

k_p = axs_bottom.scatter(x=[], y=[], s=[], c=[], cmap='viridis', alpha=0.6, norm=norm)
s_p = axs_bottom.scatter(x=[], y=[], s=[], c=[], cmap='viridis', norm=norm)
earth = axs_bottom.scatter(x=[], y=[], s=50, c=[], cmap='viridis', norm=norm)
earth_text = axs_bottom.text(0, 0, 'Earth', color='black', ha='right', va='bottom')
axs_bottom.scatter(x=0, y=0, s=1500, color="#f5ed51", edgecolors='black')

cbar_kp = plt.colorbar(k_p, ax=axs_bottom)
cbar_kp.set_label('Temperature (K)', rotation=270, labelpad=15)

def update(i):
    k_p.set_offsets(np.column_stack((x_positions[i % num_frames, :len(solar_exo_animation) - 8],
                                    y_positions[i % num_frames, :len(solar_exo_animation) - 8])))
    k_p.set_sizes(planet_sizes[i % num_frames, :len(solar_exo_animation) - 8])
    k_p.set_array(solar_exo_animation['pl_eqt'].iloc[:len(solar_exo_animation) - 8])

    s_p.set_offsets(np.column_stack((x_positions[i % num_frames, -8:-1],
                                    y_positions[i % num_frames, -8:-1])))
    s_p.set_sizes(planet_sizes[i % num_frames, -8:-1])
    s_p.set_array(solar_exo_animation['pl_eqt'].iloc[-8:-1])

    earth.set_offsets(np.column_stack((x_positions[i % num_frames, -1],
                                    y_positions[i % num_frames, -1])))
    earth.set_array([solar_exo_animation['pl_eqt'].iloc[-1]])

    earth_text.set_position((x_positions[i % num_frames, -1], y_positions[i % num_frames, -1]))

    return k_p, s_p, earth, earth_text

plt.tight_layout()

ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=200, repeat=False)
ani.save('planets_orbiting_star_animation.gif', writer='pillow', fps=30)
# Image(filename='planets_orbiting_star_animation.gif')
# plt.show()


from prettytable import PrettyTable

# Function to print table in grid format
def print_table(table, title):
    print(f"\n{title}\n")
    print(table)

# Table 1: Top 10 pl_orbper
table1 = solar_exo_animation.nlargest(10, 'pl_orbper')[['pl_name', 'pl_orbper']].round(2)
table1_pretty = PrettyTable()
table1_pretty.field_names = table1.columns
for row in table1.itertuples(index=False):
    table1_pretty.add_row(row)
print_table(table1_pretty, "Top 10 Orbital Period (Days)")

# Table 2: Top 10 pl_orbsmax
table2 = solar_exo_animation.nlargest(10, 'pl_orbsmax')[['pl_name', 'pl_orbsmax']].round(2)
table2_pretty = PrettyTable()
table2_pretty.field_names = table2.columns
for row in table2.itertuples(index=False):
    table2_pretty.add_row(row)
print_table(table2_pretty, "Top 10 Distance from Star (AU)")

# Table 3: Top 10 pl_rade
table3 = solar_exo_animation.nlargest(10, 'pl_rade')[['pl_name', 'pl_rade']].round(2)
table3_pretty = PrettyTable()
table3_pretty.field_names = table3.columns
for row in table3.itertuples(index=False):
    table3_pretty.add_row(row)
print_table(table3_pretty, "Top 10 Planet Radius (Earth)")

# Table 4: Top 10 pl_eqt
table4 = solar_exo_animation.nlargest(10, 'pl_eqt')[['pl_name', 'pl_eqt']].round(2)
table4_pretty = PrettyTable()
table4_pretty.field_names = table4.columns
for row in table4.itertuples(index=False):
    table4_pretty.add_row(row)
print_table(table4_pretty, "Top 10 Planet Temperature (K)")

# Table 5: Top 10 sy_dist
table5 = solar_exo_animation.nlargest(10, 'sy_dist')[['pl_name', 'sy_dist']].round(2)
table5_pretty = PrettyTable()
table5_pretty.field_names = table5.columns
for row in table5.itertuples(index=False):
    table5_pretty.add_row(row)
print_table(table5_pretty, "Top 10 Distance from Earth (Parsec)")
