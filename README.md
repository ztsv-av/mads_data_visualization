# Description

Repository for the Data Visualization Course, University of Luxembourg, 2024.\
Author: Anton Zaitsev.

# Notes

- Firstly, download Exoplanets and Solarplanets dataset to 'data' folder inside the repository.
- See data references in the ```main.ipynb``` file.
- Presentation Powerpoint is not included in the repository, since it has high weight (287 MB), due to the Planet Rotation Period & Temperature animation plot.

# Converting to HTML
```
jupyter nbconvert --to html --no-input main.ipynb
```

# Converting .md to PDF

```
pandoc presentation_notes.md --output presentation_notes.pdf -V fontsize=10pt
```
