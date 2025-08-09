## Interview Questions: Answers (Task 5)

1. **What is Pandas used for?**
   - Pandas is a Python library for data analysis and manipulation, offering fast, flexible data structures like `Series` and `DataFrame` and tools for reading/writing files, cleaning, transforming, aggregating, and summarizing data.

2. **What’s a DataFrame?**
   - A 2D, tabular, labeled data structure in Pandas with columns of potentially different types. Think of it like an in-memory spreadsheet or SQL table.

3. **How do you read a CSV file?**
   - `pd.read_csv('file.csv', parse_dates=[...])` reads a CSV into a DataFrame; options handle delimiters, headers, dtypes, NA values, etc.

4. **What is groupby()?**
   - `groupby()` splits data into groups based on keys (columns), applies aggregations or transformations to each group, and combines the results (split-apply-combine pattern).

5. **How do you filter rows?**
   - Use boolean masks: `df[df['col'] > 0]` or combine with `&`/`|`: `df[(df['region']=='North') & (df['units']>10)]`.

6. **Difference between loc[] and iloc[]?**
   - `loc[]` is label-based (uses index/column labels). `iloc[]` is position-based (uses integer positions).

7. **What does .head() do?**
   - Returns the first N rows (default 5) of a DataFrame for a quick preview.

8. **How can you create a bar chart?**
   - With Matplotlib/Seaborn: `sns.barplot(x=index, y=values)` or directly from DataFrame: `df.plot(kind='bar')`.

9. **What’s the shape of a DataFrame?**
   - `df.shape` returns a tuple `(rows, columns)` representing the dimensions.

10. **What is NaN?**
    - A special floating-point value representing missing or undefined data in numerical arrays; Pandas uses `NaN` to denote missing values.

