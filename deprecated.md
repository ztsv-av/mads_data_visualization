```
# Some Maximums

column_averages = solar_exo_animation.drop(columns=['pl_name']).mean()
table1 = solar_exo_animation.nlargest(10, 'pl_orbper')[['pl_name', 'pl_orbper']].round(2)
table2 = solar_exo_animation.nlargest(10, 'pl_orbsmax')[['pl_name', 'pl_orbsmax']].round(2)
table3 = solar_exo_animation.nlargest(10, 'pl_rade')[['pl_name', 'pl_rade']].round(2)
table4 = solar_exo_animation.nlargest(10, 'pl_eqt')[['pl_name', 'pl_eqt']].round(2)
table5 = solar_exo_animation.nlargest(10, 'sy_dist')[['pl_name', 'sy_dist']].round(2)
```

<div style="display: flex; justify-content: space-between;">
<!-- Top 10 Orbital Period (Days) -->
<div style="flex: 1">
  <strong>    Top 10 Orbital Period (Days)</strong>
  <table>
    <thead>
      <tr>
        <th>pl_name</th>
        <th>pl_orbper</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Neptune</td>
        <td>60189.0</td>
      </tr>
      <tr>
        <td>Uranus</td>
        <td>30685.4</td>
      </tr>
      <tr>
        <td>Saturn</td>
        <td>10759.22</td>
      </tr>
      <tr>
        <td>Jupiter</td>
        <td>4332.59</td>
      </tr>
      <tr>
        <td>Kepler-1647 b</td>
        <td>1107.59</td>
      </tr>
      <tr>
        <td>Kepler-1654 b</td>
        <td>1047.84</td>
      </tr>
      <tr>
        <td>Kepler-167 e</td>
        <td>979.95</td>
      </tr>
      <tr>
        <td>Kepler-1704 b</td>
        <td>911.1</td>
      </tr>
      <tr>
        <td>Kepler-1708 b</td>
        <td>737.11</td>
      </tr>
      <tr>
        <td>Mars</td>
        <td>686.98</td>
      </tr>
    </tbody>
  </table>
  <strong>    Average: 339.79</strong>
</div>

<!-- Top 10 Distance from Star (AU) -->
<div style="flex: 1">
  <strong>    Top 10 Distance from Star (AU)</strong>
  <table>
    <thead>
      <tr>
        <th>pl_name</th>
        <th>pl_orbsmax</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Neptune</td>
        <td>30.07</td>
      </tr>
      <tr>
        <td>Uranus</td>
        <td>19.19</td>
      </tr>
      <tr>
        <td>Saturn</td>
        <td>9.54</td>
      </tr>
      <tr>
        <td>Jupiter</td>
        <td>5.2</td>
      </tr>
      <tr>
        <td>Kepler-1647 b</td>
        <td>2.72</td>
      </tr>
      <tr>
        <td>Kepler-1654 b</td>
        <td>2.03</td>
      </tr>
      <tr>
        <td>Kepler-1704 b</td>
        <td>1.88</td>
      </tr>
      <tr>
        <td>Kepler-167 e</td>
        <td>1.71</td>
      </tr>
      <tr>
        <td>Kepler-1708 b</td>
        <td>1.64</td>
      </tr>
      <tr>
        <td>Mars</td>
        <td>1.52</td>
      </tr>
    </tbody>
  </table>
  <strong>    Average: 0.38</strong>
</div>

<!-- Top 10 Planet Radius (Earth) -->
<div style="flex: 1">
  <strong>    Top 10 Planet Radius (Earth)</strong>
  <table>
    <thead>
      <tr>
        <th>pl_name</th>
        <th>pl_rade</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Kepler-29 b</td>
        <td>929.99</td>
      </tr>
      <tr>
        <td>Kepler-29 c</td>
        <td>410.69</td>
      </tr>
      <tr>
        <td>KOI-1599.02</td>
        <td>36.37</td>
      </tr>
      <tr>
        <td>Kepler-359 d</td>
        <td>23.46</td>
      </tr>
      <tr>
        <td>Kepler-57 c</td>
        <td>21.52</td>
      </tr>
      <tr>
        <td>KOI-13 b</td>
        <td>20.73</td>
      </tr>
      <tr>
        <td>Kepler-419 b</td>
        <td>20.11</td>
      </tr>
      <tr>
        <td>Kepler-12 b</td>
        <td>18.68</td>
      </tr>
      <tr>
        <td>Kepler-7 b</td>
        <td>17.52</td>
      </tr>
      <tr>
        <td>HAT-P-7 b</td>
        <td>16.67</td>
      </tr>
    </tbody>
  </table>
  <strong>    Average: 8.35</strong>
</div>

<!-- Top 10 Planet Temperature (K) -->
<div style="flex: 1">
  <strong>    Top 10 Planet Temperature (K)</strong>
  <table>
    <thead>
      <tr>
        <th>pl_name</th>
        <th>pl_eqt</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>KOI-13 b</td>
        <td>3202.22</td>
      </tr>
      <tr>
        <td>HAT-P-7 b</td>
        <td>2237.9</td>
      </tr>
      <tr>
        <td>Kepler-78 b</td>
        <td>2236.5</td>
      </tr>
      <tr>
        <td>Kepler-1658 b</td>
        <td>2061.5</td>
      </tr>
      <tr>
        <td>Kepler-407 b</td>
        <td>2037.6</td>
      </tr>
      <tr>
        <td>Kepler-10 b</td>
        <td>2023.09</td>
      </tr>
      <tr>
        <td>Kepler-76 b</td>
        <td>2012.29</td>
      </tr>
      <tr>
        <td>Kepler-21 b</td>
        <td>1874.75</td>
      </tr>
      <tr>
        <td>Kepler-91 b</td>
        <td>1863.5</td>
      </tr>
      <tr>
        <td>Kepler-323 b</td>
        <td>1860.0</td>
      </tr>
    </tbody>
  </table>
  <strong>    Average: 802.80</strong>
</div>

<!-- Top 10 Distance from Earth (Parsec) -->
<div style="flex: 1;">
  <strong>    Top 10 Distance from Earth (Parsec)</strong>
  <table>
    <thead>
      <tr>
        <th>pl_name</th>
        <th>sy_dist</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Kepler-40 b</td>
        <td>2305.01</td>
      </tr>
      <tr>
        <td>Kepler-328 b</td>
        <td>2213.19</td>
      </tr>
      <tr>
        <td>Kepler-328 c</td>
        <td>2213.19</td>
      </tr>
      <tr>
        <td>Kepler-433 b</td>
        <td>1878.31</td>
      </tr>
      <tr>
        <td>Kepler-223 b</td>
        <td>1859.71</td>
      </tr>
      <tr>
        <td>Kepler-223 c</td>
        <td>1859.71</td>
      </tr>
      <tr>
        <td>Kepler-223 d</td>
        <td>1859.71</td>
      </tr>
      <tr>
        <td>Kepler-223 e</td>
        <td>1859.71</td>
      </tr>
      <tr>
        <td>Kepler-35 b</td>
        <td>1819.17</td>
      </tr>
      <tr>
        <td>Kepler-34 b</td>
        <td>1800.82</td>
      </tr>
    </tbody>
  </table>
  <strong>    Average: 658.63</strong>
</div>
