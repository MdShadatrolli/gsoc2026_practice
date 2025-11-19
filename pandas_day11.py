# pandas_day11.py
import pandas as pd

# ---------- 1. Create a Series ----------
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Series s:")
print(s)
print()

# ---------- 2. Create a DataFrame from dict ----------
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 28],
    "city": ["Delhi", "Pune", "Mumbai", "Chandigarh"],
    "score": [85.0, 92.5, None, 74.0]   # note: one missing value (None)
}
df = pd.DataFrame(data)
print("DataFrame df:")
print(df)
print()

# ---------- 3. Inspecting the data ----------
print("HEAD (first 2 rows):")
print(df.head(2))
print()
print("INFO:")
print(df.info())
print()
print("DESCRIBE (numeric):")
print(df.describe())
print()

# ---------- 4. Selecting columns ----------
print("Column 'name' (as Series):")
print(df['name'])
print()
print("Columns 'name' and 'age' (as DataFrame):")
print(df[['name', 'age']])
print()

# ---------- 5. Selecting rows ----------
print("Row with index 2 using iloc:")
print(df.iloc[2])   # 0-based integer location
print()
print("Row with index label 2 using loc (same here):")
print(df.loc[2])    # label-based (here numeric index matches)
print()

# ---------- 6. Boolean filtering ----------
print("People with age > 28:")
print(df[df['age'] > 28])
print()

# ---------- 7. Add / modify columns ----------
df['age_plus_5'] = df['age'] + 5
print("Added column 'age_plus_5':")
print(df[['name','age','age_plus_5']])
print()

# ---------- 8. Handling missing values ----------
print("Rows with missing values (any column):")
print(df[df.isna().any(axis=1)])
print()
print("Fill missing 'score' with mean score:")
mean_score = df['score'].mean(skipna=True)
df['score_filled'] = df['score'].fillna(mean_score)
print(df[['name','score','score_filled']])
print()

# ---------- 9. Groupby + aggregation ----------
print("Average score by city (after fill):")
print(df.groupby('city')['score_filled'].mean())
print()

# ---------- 10. Save to CSV ----------
df.to_csv("pandas_day11_output.csv", index=False)
print("Saved DataFrame to pandas_day11_output.csv")
