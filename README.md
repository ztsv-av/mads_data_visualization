# Description

Repository for the Data Visualization Course, University of Luxembourg, 2024.\
Author: Anton Zaitsev.

# Notes

- First, make sure to download Exoplanets and Solarplanets dataset to the 'data' folder inside the repository.
- See data references in the ```main.ipynb``` file.
- Presentation Powerpoint contains a Planet Rotation Period & Temperature animation plot with a decreased number of frames and planets, due to the high weight of the original animated plot.
- In order to fully reconstruct the Planet Rotation Period & Temperature animation plot, change decreased values for the number of frames and the number of exoplanets (100 and 100 in the code) to the according values specified in the comments. **Beware**: using full num_planets and num_frames will take a lot of time to generate the animation, which is around 30-40 minutes for the animation generation (depends on the processor power).
- The animation plot is displayed in the Markdown cell, not in the code cell. After the plot is generated, it is saved to the 'plot' directory and then Markdown loads the .gif file into the .ipynb file. If the Markdown cell does not display the .gif file, even though the animation plot was saved to the 'plots' directory, you can just reload your code editor and everything will be fixed.

# Required Libraries

To **install** all required **libraries**, one can write the following command in the terminal:
```
pip install -r requirements.txt
```

Libraries used:
- pandas
- numpy
- seaborn
- matplotlib
- scipy
- sklearn

## Python Version

We used ```Python 3.9.11```.

# Useful Commands

## Converting to HTML
```
jupyter nbconvert --to html --no-input main.ipynb
```

## Converting to Slides

```
jupyter nbconvert --to slides --no-input main.ipynb
```

## Converting .md to PDF

```
pandoc notes.md --output notes.pdf -V fontsize=10pt
```

## Creating Custom Template

```
jupyter nbconvert --to slides --no-input main.ipynb --stdout > custom_template.tpl
```
