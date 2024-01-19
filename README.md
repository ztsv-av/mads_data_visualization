# Description

Repository for the Data Visualization Course, University of Luxembourg, 2024.\
Author: Anton Zaitsev.

# Notes

- First, make sure to download Exoplanets and Solarplanets dataset to the 'data' folder inside the repository.
- See data references in the ```main.ipynb``` file.
- Presentation Powerpoint contains a Planet Rotation Period & Temperature animation plot with a decreased number of frames and planets, due to the high weight of the original animated plot.
- In order to fully reconstruct the Planet Rotation Period & Temperature animation plot, change decreased values for the number of frames and the number of exoplanets (100 and 100 in the code) to the according values specified in the comments. **Beware**: using full num_planets and num_frames will take a lot of time to generate the animation, which is around 8 minutes for data generation and 30-40 minutes for the animation generation (depends on the processor power).

# Converting to HTML
```
jupyter nbconvert --to html --no-input main.ipynb
```

# Converting .md to PDF

```
pandoc presentation_notes.md --output presentation_notes.pdf -V fontsize=10pt
```
