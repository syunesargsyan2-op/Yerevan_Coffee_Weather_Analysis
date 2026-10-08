# Coffee and Weather in Yerevan

How temperature, rain, and the day of the week affect coffee consumption and coffee shop visits.

## Files
`data.py` - Creates `yerevan_coffee_weather.csv`

`analysis1.py` - Cleaning (Pandas), SQLite queries, correlation, Seaborn charts

`yerevan_coffee_clean.csv` - Cleaned data

`chart1…3_*.png` - Charts

## Running

```bash
pip install pandas numpy seaborn matplotlib
python data.py
python analysis.py
```

## Main Results

- **Temperature ↔ coffee.** r = −0.77. The colder it is, the more coffee is consumed. On days <5°C - average 290 cups, on days >25°C - 198.
- **Rain.** On rainy days - average 295 cups vs 254 on dry days, and visits - 183 vs 147.
- **Cold + rain** together - 323 cups (other days - 256).
- **Days of the week.** Saturday/Sunday have the most people staying (~180), but on weekdays more coffee is bought to take away (~265 vs ~245).
- **Months.** Most coffee: January, December, February.

## Cleaning Steps

1. 6 missing values in `temp_c` and 3 in `coffee_cups`.
2. 3 sensor errors (`temp_c = 99.9`) → changed to NaN.
3. Temperature is filled using time interpolation, coffee amount using the median for the day of the week.