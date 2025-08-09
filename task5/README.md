## Task 5: Data Analysis on CSV Files

This task analyzes a small sales dataset with Pandas and produces charts.

### Files
- `sales.csv`: sample dataset
- `analysis.ipynb`: Jupyter notebook with the steps and charts
- `analysis_script.py`: script that computes summaries and saves charts
- `interview_answers.md`: answers to all the questions in `task.txt`

### Environment
- Python 3.10+

### Install dependencies (PowerShell)
```powershell
cd task5
pip install -r requirements.txt
```

### Run the analysis script
```powershell
python analysis_script.py
```
Outputs:
- `revenue_by_region.png`
- `units_by_product.png`

### Open the notebook
```powershell
jupyter notebook analysis.ipynb
```

### Notes
- The dataset is tiny and for demonstration only.
- The notebook shows `groupby()`, `sum()`, `plot()` usage and basic inspection like `head()` and `shape`.

