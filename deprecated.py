# Controversial

## is Exoplanet Controversial? How Many Kepler Confirmed Planets?

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
wedges, texts, autotexts = plt.pie(
    exoplanets['pl_controv_flag'].value_counts(), 
    labels=['Not Controversial', 'Controversial'], 
    autopct='', 
    colors=['#22628e', '#ae0038'],
    textprops={'fontsize': 12, 'color': 'black'}, 
    wedgeprops={'edgecolor': 'black', "alpha": 0.7},
    startangle=50
)
percs = exoplanets['pl_controv_flag'].value_counts(normalize=True)*100
labels = [f'{label} - {perc:.1f}%' for label, perc in zip(['Not Controversial', 'Controversial'], percs)]
plt.legend(
    wedges, 
    labels, 
    title='Legend', 
    bbox_to_anchor=(0.5, 1),
    loc='upper center'
)
plt.axis('equal')
plt.title('Proportion of Controversial Exoplanets', fontsize=16)

plt.subplot(1, 2, 2)
wedges, texts, autotexts = plt.pie(
    exoplanets['kepler_confirmed'].value_counts(), 
    labels=['Not Kepler Confirmed', 'Kepler Confirmed'], 
    autopct='', 
    colors=['#ae0038', '#22628e'],
    textprops={'fontsize': 12, 'color': 'black'}, 
    wedgeprops={'edgecolor': 'black', "alpha": 0.7},
    startangle=320
)
percs = exoplanets['kepler_confirmed'].value_counts(normalize=True)*100
labels = [f'{label} - {perc:.1f}%' for label, perc in zip(['Not Kepler Confirmed', 'Kepler Confirmed'], percs)]
plt.legend(
    wedges, 
    labels, 
    title='Legend', 
    bbox_to_anchor=(0.5, 1),
    loc='upper center'
)
plt.axis('equal')
plt.title('Proportion of Kepler Confirmed Exoplanets', fontsize=16)

plt.tight_layout()
plt.show()


# Correlation Heatmap

exoplanets_corr = exoplanets.drop(columns=['sy_mnum', 'sy_snum', 'sy_pnum']).select_dtypes(include=['number']).corr()
pl_orbper_corr = exoplanets_corr.loc[['pl_orbper'], :]
column_mapping = {key: column_descriptions.get(key, key) for key in pl_orbper_corr.columns}
pl_orbper_corr_T = exoplanets_corr.loc[['pl_orbper'], :].T

plt.figure(figsize=(12, 6))
ax = sns.heatmap(pl_orbper_corr_T, annot=True, cmap='icefire', fmt=".2f", linewidths=0.5, xticklabels=['Orbital Period'])
plt.title('Correlation Heatmap for Orbital Period', fontsize=16)
ax.set_yticklabels([column_mapping[key] for key in pl_orbper_corr.columns])

plt.show()


# Feature Relationships

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 8))

# distance
sns.scatterplot(x='pl_orbsmax', y='pl_orbper', hue='sy_dist_log', data=exoplanets, alpha=0.3, color='#22628e', ax=axes[0, 0])
sns.scatterplot(x='semimajorAxis_AU', y='sideralOrbit', data=solarplanets, label='Solar Planets', alpha=0.8, color='#FFC300', edgecolor='black', ax=axes[0, 0])
sns.scatterplot(x='semimajorAxis_AU', y='sideralOrbit', data=earth_data, label='Earth', alpha=1, color='#DAF7A6', edgecolor='black', ax=axes[0, 0])
earth_x = earth_data['semimajorAxis_AU'].values[0]
earth_y = earth_data['sideralOrbit'].values[0]
axes[0, 0].text(earth_x + 0.1, earth_y - 300, 'Earth', color='black', fontsize=12, ha='left', va='bottom', path_effects=[pe.withStroke(linewidth=1, foreground="white")])
axes[0, 0].set_title('Orbital Distance vs Orbital Period', fontsize=16)
axes[0, 0].set_xlabel('Orbital Distance (AU)', fontsize=12)
axes[0, 0].set_ylabel('Orbital Period (days)', fontsize=12)

# radius 
sns.scatterplot(x='pl_rade', y='pl_orbper', data=exoplanets, alpha=0.3, hue='sy_dist_log', ax=axes[0, 1])
sns.scatterplot(x='radius_earth', y='sideralOrbit', data=solarplanets, label='Solar Planets', alpha=0.8, color='#f2d40c', ax=axes[0, 1], edgecolor='black')
sns.scatterplot(x='radius_earth', y='sideralOrbit', data=earth_data, label='Earth', alpha=0.7, color='black', ax=axes[0, 1])
earth_x = earth_data['radius_earth'].values[0]
earth_y = earth_data['sideralOrbit'].values[0]
axes[0, 1].text(earth_x, earth_y, 'Earth', color='black', fontsize=12, ha='left', va='bottom', path_effects=[pe.withStroke(linewidth=1, foreground="white")])
axes[0, 1].set_xlabel('Planet Radius (Earth)', fontsize=12)
axes[0, 1].set_ylabel('Orbital Period (days)', fontsize=12)
axes[0, 1].set_title('Planet Radius vs Orbital Period', fontsize=16)

# mass
sns.scatterplot(x='pl_masse', y='pl_orbper', data=exoplanets, alpha=0.3, hue='sy_dist_log', ax=axes[1, 0])
sns.scatterplot(x='mass_earth', y='sideralOrbit', data=solarplanets, label='Solar Planets', alpha=0.8, color='#f2d40c', ax=axes[1, 0], edgecolor='black')
sns.scatterplot(x='mass_earth', y='sideralOrbit', data=earth_data, label='Earth', alpha=0.7, color='black', ax=axes[1, 0])
earth_x = earth_data['mass_earth'].values[0]
earth_y = earth_data['sideralOrbit'].values[0]
axes[1, 0].text(earth_x, earth_y, 'Earth', color='black', fontsize=12, ha='left', va='bottom', path_effects=[pe.withStroke(linewidth=1, foreground="white")])
axes[1, 0].set_xlabel('Planet Mass (Earth)', fontsize=12)
axes[1, 0].set_ylabel('Orbital Period (days)', fontsize=12)
axes[1, 0].set_title('Planet Mass vs Orbital Period', fontsize=16)

# eccentricity
sns.scatterplot(x='pl_orbeccen', y='pl_orbper', data=exoplanets, alpha=0.3, hue='sy_dist_log', ax=axes[1, 1])
sns.scatterplot(x='eccentricity', y='sideralOrbit', data=solarplanets, label='Solar Planets', alpha=0.8, color='#f2d40c', ax=axes[1, 1], edgecolor='black')
sns.scatterplot(x='eccentricity', y='sideralOrbit', data=earth_data, label='Earth', alpha=0.7, color='black', ax=axes[1, 1])
earth_x = earth_data['eccentricity'].values[0]
earth_y = earth_data['sideralOrbit'].values[0]
axes[1, 1].text(earth_x, earth_y, 'Earth', color='black', fontsize=12, ha='left', va='bottom', path_effects=[pe.withStroke(linewidth=1, foreground="white")])
axes[1, 1].set_xlabel('Planet Eccentricity', fontsize=12)
axes[1, 1].set_ylabel('Orbital Period (days)', fontsize=12)
axes[1, 1].set_title('Planet Eccentricity vs Orbital Period', fontsize=16)

for ax in axes.flat:
    ax.get_legend().remove()
    ax.set_xscale('log')
    ax.set_yscale('log')
handles, labels = axes[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right', bbox_to_anchor=(0.62, 0.03), fontsize=12)
plt.tight_layout()
plt.show()


# Drop Planets with NAs

columns_drop_nas = ['pl_orbper', 'pl_orbsmax', 'pl_rade', 'pl_masse', 'pl_orbeccen', 'sy_dist']
exoplanets_nas = exoplanets.dropna(subset=columns_drop_nas)

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

# -----------------------

plt.figure(figsize=(12, 6))

ax1 = plt.subplot(1, 2, 1)
sns.histplot(
    data=exoplanets, 
    y='disc_year', 
    multiple="stack",
    binwidth=2, 
    hue='discoverymethod', 
    palette='viridis'
)
plt.title('Exoplanets by Year and Discovery Method', fontsize=16)
plt.xlabel('Number of Exoplanets Discovered',fontsize=12)
plt.ylabel('Year',fontsize=12)
plt.xticks(rotation=45)
plt.yticks(range(2000, max(exoplanets['disc_year'])+1, 5))
legend_labels = exoplanets['discoverymethod'].unique()
ax1.legend(labels=legend_labels, title='Discovery Method', fontsize=11)

ax2 = plt.subplot(1, 2, 2)
sns.histplot(
    data=exoplanets[exoplanets['kepler_confirmed']], 
    y='disc_year', 
    multiple="stack",
    binwidth=2, 
    hue='discoverymethod', 
    palette='viridis'
)
plt.title('Kepler Confirmed Exoplanets by Year and Discovery Method', fontsize=16)
plt.xlabel('Number of Kepler Confirmed Exoplanets Discovered',fontsize=12)
plt.ylabel('Year',fontsize=12)
plt.xticks(rotation=45)
plt.yticks(range(2000, max(exoplanets['disc_year'])+1, 5))
legend_labels_kepler = exoplanets[exoplanets['kepler_confirmed']]['discoverymethod'].unique()
ax2.legend(labels=legend_labels_kepler, title='Discovery Method', fontsize=12, loc='lower right')

plt.tight_layout()
plt.show()


# -----------------------

plt.figure(figsize=(12, 6))
plt.suptitle("Where Exoplanets are Located in the Sky", fontsize=16)

ax1 = plt.subplot(1, 2, 1)
sns.scatterplot(
    x='ra', 
    y='dec', 
    hue='discoverymethod', 
    palette='viridis',
    data=exoplanets, 
    alpha=0.5, 
    ax=ax1
)
ax1.set_title("Map of Exoplanets Locations in the Sky")
ax1.set_xlabel("Right Ascention (RA)")
ax1.set_ylabel("Declination (Deg)")
ax1.legend(labels=legend_labels, title='Discovery Method', fontsize=8).set_visible(False)
legend_labels = exoplanets['discoverymethod'].unique()
ax1.legend(labels=legend_labels, title='Discovery Method', fontsize=8, bbox_to_anchor=(1.05, 1), loc='upper left')

ax2 = plt.subplot(1, 2, 2)
sns.scatterplot(
    x='ra', 
    y='dec', 
    hue='sy_dist', 
    palette='viridis',
    data=exoplanets, 
    alpha=0.5, 
    ax=ax2
)
ax2.set_title("Map of Exoplanets Locations in the Sky")
ax2.set_xlabel("Right Ascention (RA)")
ax2.set_ylabel("Declination (Deg)")
legend2_labels = ['1500 P','3000 P','4500 P','6000 P','7500 P']
ax2.legend(labels=legend2_labels, fontsize=8, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
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

# PRINTING CONVEX HULL AT KMEANS
# PC1	PC2	Cluster	Center
# 0	-4.188380	-0.537268	1	[-3.3358130281780167, -0.5275890053379767]
# 1	-3.845811	-0.014483	1	[-3.3358130281780167, -0.5275890053379767]
# 2	-1.973248	-1.031016	1	[-3.3358130281780167, -0.5275890053379767]
# 3	-1.355944	-0.643700	0	[0.041930427373717376, -0.22920241824658824]
# 4	-1.414702	-2.196838	4	[-1.4147016350743464, -2.196838375226245]
# 5	-1.385345	3.487958	2	[-0.1559401159293939, 2.2306042141353872]
for i in pc_clusters['Cluster'].unique():
    points = pc_clusters[pc_clusters['Cluster'] == i][['PC1', 'PC2']].values
    if len(points) == 1:
        continue
    # get convex hull
    hull = ConvexHull(points)
    # get x and y coordinates
    # repeat last point to close the polygon
    x_hull = np.append(points[hull.vertices,0],
                       points[hull.vertices,0][0])
    y_hull = np.append(points[hull.vertices,1],
                       points[hull.vertices,1][0])
    # plot shape
    ax4.fill(x_hull, y_hull, c=cluster_colors[kmeans_clusters[idx]], alpha=0.3, )
