# How Exoplanets were Discovered and Where They are Located in the Sky

## Units of Measurement

1. Here we explore which methods were the most common to use to discover exoplanets, by years.
2. We notice that at first people used Radial Velocity method, but then Transit became the most prominent.
3. Then we plot the location in the sky (Latitude and Longitude analogues) by discovery method and distance from Earth.
4. On these plots we can notice this patch of planets, around 100 planets, that are really far away. For these planets, Microlensing method was used. For the batch above, closer exoplanets, Transit was used.

An astronomical unit (AU) is a unit of measurement equal to the average distance between a planet and its host star.
- 1 AU is the average distance from the Earth to the Sun.
- 1 AU = 1.5 x 10^8 KM (150 million kilometers).
- 1 Parsec = 206,265 AU.
- 1 Parsec = 3.09 x 10^13 KM.

# Distribution Analysis of Exoplanetary Parameters, Including Comparison with Earth

1. Here we explore how different features of exoplanets are distributed and compared to the Earth. We can notice almost normal distribution for some features, while other features follow bimodal distribution.
2. Distribution of Distance from Earth: includes Mars for reference, distance from Earth to Mars: 0.000015 Parcec (356 million km).

## Parameters 

- Planetary radius refers to the average distance from the center to the outer boundary of a celestial body, such as a planet, providing a measure of its size.
- Orbital period is the time it takes for a celestial object, such as a planet, to complete one full revolution around its host star or a central point in its orbit.
- Orbital distance is the measure of how far a planet is from its hosting star.
- Equilibrium Temperature is an estimate of the temperature a planet or celestial body would have if it were a simple black body, thus not subject to atmospheric windows, internal heat sources, etc.
    - Does not count the greenhouse effect !
- Some Earth data for reference:
    - Earth radius = 6.371 x 10^3 km
    - Earth mass = 5.972 x 10^24 kg
    - Earth orbital distance = 1 AU
    - Earth's Equilibrium Temperature: $\approx$ 255K = -18C

# How Distance to Star Affects Planet's Temperature and Rotational Period

1. From the animation I noticed that closer the planet to its host star, the hotter it is. So, I decided to plot the relationship between planet temperature to distance to its host star and we can notice a high positive correlation between these two features.
2. Also, I changed the color gradient to go from blue, to purple to yellow (purple instead of black) to better represent the temperature.

# Which planets are Inhabitable? Calculating Habitable Zone and Performing Clustering Analysis

## Habitable Zone

1. Show formula if needed.
2. Same as with the animation, I noticed that there might be a positive correlation between star temperature and its mass. Indeed, after plotting this relationship, we notice high correlation between these two features. We can also observe positive correlation between planet orbital distance and star mass (higher mass of the star $=>$ further away the planet is from it).
3. The color cmap for stars is different from planet one, colors go from red to light yellow-blue to dark blue (usually used to represent star temperature).

- Inner Boundary ("Runaway Greenhouse"): This is the distance from the star where the greenhouse effect becomes too strong making the surface temperature too hot for liquid water.
- Outer Boundary ("Maximum CO2 Greenhouse"): Beyond this distance, the greenhouse effect is not sufficient to keep the surface temperature warm enough for liquid water to exist.

## K-Means & PCA

1. In the habitable zone, there are around 50 planets, however in the Cluster plot we only see 17. This is because some planets miss important feature information, such as planet radius, planet temperature, especially planet temperature
2. We used $K=3$, but $K=5$ showed the same cluster difference (Earth cluster was far away from the other ones).

## Earth, Mars, Closets Exoplanet inside Habitable Zone Boundaries and closest Exoplanet to Earth according to K-Means Analysis

1. Planet's information was checked on the official NASA Exoplanets catalog website.
2. The planet that is closest to Earth according to K-Means Analysis, i.e. Kepler 22-b, is supposedly a super-Earth that could be covered in a super ocean, meaning our Habitable Zone analysis is correct.
3. Time to get calculations are extremely approximate. Used approximate time to get to Mars, which is about 7 month. Then used the distance to mars, to exoplanet and calculated the time to get to the planet $\left(\frac{\text{time to get to mars} \times \text{distance to exoplanet}}{\text{distance to mars}}\right)$.
