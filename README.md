---
title: "Species Occurrence Mapping with GBIF and Python️"
author: "Juan Carlos Rubio Polania, PhD"
date: "2024-03-16"
---

# Species Occurrence Mapping with GBIF and Python 🌍🐍🗺️

## Overview

This workflow demonstrates how to retrieve species occurrence records from the Global Biodiversity Information Facility (GBIF) using Python and visualize the results on geographic maps.

The script combines:
- Biodiversity data retrieval
- JSON normalization
- Data cleaning
- Spatial visualization
- Geographic plotting
- Occurrence mapping

The workflow uses the `pygbif` library to access GBIF occurrence records and combines `pandas`, `geopandas`, and `matplotlib` to create scientific visualizations.

Although this example uses the species *Neosmilaster georgianus*, the workflow can be adapted to many applications involving:
- Species distributions
- Biodiversity databases
- Marine organisms
- Ecological studies
- Biogeography
- Conservation analyses
- Environmental assessments
- Spatial ecology

---

# Required Libraries

```python
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

from pygbif import occurrences
from mpl_toolkits.axes_grid1 import make_axes_locatable
```

---

# Workflow

## 1. Import Libraries

```python
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
```

The script imports libraries for:
- Numerical analysis
- Data manipulation
- Geographic visualization
- Scientific plotting

---

## 2. Import GBIF Function

```python
from pygbif import occurrences
```

The `pygbif` package provides access to GBIF biodiversity occurrence records.

---

## 3. Define Species Name

```python
sp = 'Neosmilaster georgianus'
```

The scientific name used for the occurrence search is defined.

---

## 4. Retrieve Occurrence Records

```python
ngd = occurrences.search(
    scientificName=sp,
    limit=500
)
```

Occurrence records are downloaded directly from GBIF.

The `limit` argument defines the maximum number of records retrieved.

---

## 5. Normalize JSON Data

```python
ngdDF = pd.json_normalize(
    ngd['results']
)
```

The JSON structure is converted into a tabular pandas DataFrame.

---

## 6. Select Relevant Variables

```python
cols = [
    'decimalLongitude',
    'decimalLatitude',
    'occurrenceStatus',
    'datasetName',
    'individualCount'
]
```

Relevant geographic and biological variables are selected.

---

## 7. Remove Missing Values

```python
ngdDF2 = ngdDF2.dropna()
```

Rows containing missing information are removed.

---

## 8. Load Geographic Basemap

```python
nl = gpd.read_file(
    gpd.datasets.get_path(
        'naturalearth_lowres'
    )
)
```

Natural Earth geographic boundaries are loaded using GeoPandas.

---

## 9. Create Species Distribution Map

```python
plt.scatter(x=XX, y=YY)
```

Occurrence coordinates are plotted on the map using scatter plots.

The map includes:
- Geographic boundaries
- Longitude and latitude axes
- Species occurrence locations

---

## 10. Create Colored Occurrence Map

```python
sca = ax.scatter(
    x=XX,
    y=YY,
    c=ngdDF2['individualCount']
)
```

A second map is generated where:
- Point colors represent abundance values
- Color intensity reflects `individualCount`

---

## 11. Add Colorbar

```python
plt.colorbar(sca, cax=cax)
```

A colorbar is added to improve interpretation of abundance values.

---

# Applications

This workflow can be useful for:
- Biodiversity analyses
- Marine ecology
- Species distribution studies
- Biogeography
- Conservation biology
- Ecological visualization
- Spatial ecology
- Environmental sciences

---

# Data Source

Occurrence records are obtained from:

- GBIF (Global Biodiversity Information Facility)

The workflow accesses data programmatically using the `pygbif` package.

---

# Requirements

- Python 3.x
- numpy
- pandas
- geopandas
- matplotlib
- pygbif

Install packages with:

```bash
pip install numpy pandas geopandas matplotlib pygbif
```

---

# Notes

Some occurrence records may contain:
- Missing coordinates
- Coordinate errors
- Incomplete metadata

Additional filtering and validation may improve analyses depending on the application.

---

# License

This project is licensed under the MIT License.

---

# Author

Juan Carlos Rubio Polania, PhD
