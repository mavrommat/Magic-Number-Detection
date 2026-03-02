This repository provides a toolkit to detect unusual patterns in tabular data known as **Magic Numbers**.

### What are Magic Numbers?

Magic Numbers are placeholder values (e.g., `999`, `-9999`, `1E+10`) artificially ingested into tables to indicate unmeasured, uncertain measurements, or internal flags. Researchers have used these since the early days of computing, and they remain common in legacy and modern databases today.

**The Problem:** Ingesting these placeholders into a database can corrupt statistical analysis and machine learning results.

**The Solution:** Without relying on heavy AI or context-based analysis, this algorithm statistically detects these numbers as "delta-peaks" that fall significantly away from the data's normal distribution.

---

## 🛠 The Detection Process

The algorithm processes data through four distinct stages to ensure high precision and recall:

1. **String/Type Cleaning**: Converts raw input and handles non-numeric data.
2. **Sign Violation**: Detects numbers that break the expected sign convention of the column.
3. **Sequential Distance Analysis (Delta)**:
* Calculates distances between unique sorted values.
* Uses a **Dynamic PDF Threshold** to flag improbable "gaps" as outliers based on probability density.
* **Small Table Safeguard**: Uses synthetic KDE sampling to stabilize results on small datasets. (Note: Currently set to output a warning if unique numerical values are below 20).


4. **Clustering & Overlap**: Uses Kernel Density Estimation (KDE) overlap analysis to distinguish between "Extreme" magic numbers (at the edges) and "Non-extreme" numbers (embedded within the data).

---

## Recommended Parameters

To balance precision and recall, the following values are recommended:

| Parameter | Recommended Value | Description |
| --- | --- | --- |
| `sign_violation_threshold` | `3` | Maximum values that can violate the sign of the apparent distribution. |
| `gauss_threshold` | `0.01` (1%) | Sensitivity of the PDF outlier detection (percentage of peak density). |
| `overlap_threshold` | `1.0` to `5.0` | The % of KDE overlap allowed before a number is dismissed as "normal". |
| `min_unique_values` | `20` | Threshold for statistical validity. If unique values < 20, detection is skipped to avoid false positives. |

---

## How to Use

For a full walkthrough, please refer to the provided notebook:

`MagicNumberDetector_use_examples.ipynb`

### Quick Start Example

```python
from astropy.io import ascii
import numpy as np
import pandas as pd
import pprint

from get_magic_numbers import MagicNumberDetector

readme_url = "https://cdsarc.cds.unistra.fr/ftp/J/A+A/469/861/ReadMe"
data_url = "https://cdsarc.cds.unistra.fr/ftp/J/A+A/469/861/table1.dat"

table = ascii.read(data_url, readme=readme_url, format="cds")
df = table.to_pandas()

detector = MagicNumberDetector(
    sign_violation_threshold=3,
    gauss_threshold=0.01,
    overlap_threshold = 0.1,
    plot_graphs=False
)
master_results, cleaned_results = detector.run_magic_detection(df)

print("Cleaned Magic Number Results")
pprint.pprint(cleaned_results)
```

