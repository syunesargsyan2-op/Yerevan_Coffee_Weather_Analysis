{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "56e64f17-72b0-4a47-a259-e0883b33e4ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib\n",
    "matplotlib.use(\"Agg\")\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e61d536d-c0c3-4119-9593-358d986526a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "BLUE, ORANGE, INK, MUTED, SURFACE = \"#2a78d6\", \"#eb6834\", \"#0b0b0b\", \"#52514e\", \"#fcfcfb\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a9361acd-38a5-4859-8474-2f04af8fe4d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Raw shape: (500, 7)\n",
      "Missing values:\n",
      " temp_c         6\n",
      "coffee_cups    3\n",
      "dtype: int64 \n",
      "\n",
      "Sensor errors (temp out of range): 3\n"
     ]
    }
   ],
   "source": [
    "#1) Load & clean (Pandas)\n",
    "df = pd.read_csv(\"yerevan_coffee_weather.csv\", parse_dates=[\"date\"])\n",
    "print(\"Raw shape:\", df.shape)\n",
    "print(\"Missing values:\\n\", df.isna().sum()[lambda s: s > 0], \"\\n\")\n",
    "\n",
    "bad_temp = (df[\"temp_c\"] > 50) | (df[\"temp_c\"] < -40)\n",
    "print(\"Sensor errors (temp out of range):\", int(bad_temp.sum()))\n",
    "df.loc[bad_temp, \"temp_c\"] = np.nan\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7942be51-0a51-4756-b027-eac75b3efa97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Clean shape: (500, 9) | remaining NaN: 0 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Fill gaps: temperature by interpolation in time, coffee by weekday median\n",
    "df = df.sort_values(\"date\").reset_index(drop=True)\n",
    "df[\"temp_c\"] = df[\"temp_c\"].interpolate(limit_direction=\"both\")\n",
    "df[\"coffee_cups\"] = df[\"coffee_cups\"].fillna(\n",
    "    df.groupby(\"weekday\")[\"coffee_cups\"].transform(\"median\")).round().astype(int)\n",
    "\n",
    "df[\"is_weekend\"] = df[\"weekday\"].isin([\"Saturday\", \"Sunday\"]).astype(int)\n",
    "df[\"temp_band\"] = pd.cut(df[\"temp_c\"], [-100, 5, 15, 25, 100],\n",
    "                         labels=[\"<5°C\", \"5–15°C\", \"15–25°C\", \">25°C\"])\n",
    "df.to_csv(\"yerevan_coffee_clean.csv\", index=False)\n",
    "print(\"Clean shape:\", df.shape, \"| remaining NaN:\", int(df.isna().sum().sum()), \"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8f385531-8cc3-45b6-9704-a7f596c79b61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correlation matrix:\n",
      "                temp_c  is_rainy  precip_mm  is_weekend  coffee_cups  \\\n",
      "temp_c           1.00      0.08       0.09       -0.02        -0.77   \n",
      "is_rainy         0.08      1.00       0.81        0.02         0.33   \n",
      "precip_mm        0.09      0.81       1.00        0.02         0.26   \n",
      "is_weekend      -0.02      0.02       0.02        1.00        -0.23   \n",
      "coffee_cups     -0.77      0.33       0.26       -0.23         1.00   \n",
      "cafe_checkins    0.29      0.44       0.34        0.64        -0.23   \n",
      "\n",
      "               cafe_checkins  \n",
      "temp_c                  0.29  \n",
      "is_rainy                0.44  \n",
      "precip_mm               0.34  \n",
      "is_weekend              0.64  \n",
      "coffee_cups            -0.23  \n",
      "cafe_checkins           1.00   \n",
      "\n"
     ]
    }
   ],
   "source": [
    "# 2) Correlations \n",
    "corr = df[[\"temp_c\", \"is_rainy\", \"precip_mm\", \"is_weekend\",\n",
    "           \"coffee_cups\", \"cafe_checkins\"]].corr().round(2)\n",
    "print(\"Correlation matrix:\\n\", corr, \"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fc4d4ada-8ca4-4d53-8bbb-0f2dc03971e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "500"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3) SQL (SQLite) \n",
    "con = sqlite3.connect(\"coffee.db\")\n",
    "df.assign(date=df[\"date\"].dt.strftime(\"%Y-%m-%d\"),\n",
    "          temp_band=df[\"temp_band\"].astype(str)).to_sql(\"daily\", con, if_exists=\"replace\", index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8f5e3bd9-e7b4-4dd9-8651-743199786e2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "queries = {\n",
    "    \"Q1. Avg coffee on days colder than 15°C\":\n",
    "        \"SELECT ROUND(AVG(coffee_cups),1) AS avg_coffee, COUNT(*) AS days FROM daily WHERE temp_c < 15;\",\n",
    "    \"Q2. Rainy vs dry days\":\n",
    "        \"\"\"SELECT CASE is_rainy WHEN 1 THEN 'Rainy' ELSE 'Dry' END AS day_type,\n",
    "                  ROUND(AVG(coffee_cups),1) AS avg_coffee,\n",
    "                  ROUND(AVG(cafe_checkins),1) AS avg_checkins, COUNT(*) AS days\n",
    "           FROM daily GROUP BY is_rainy;\"\"\",\n",
    "    \"Q3. Weekday ranking (avg check-ins)\":\n",
    "        \"\"\"SELECT weekday, ROUND(AVG(cafe_checkins),1) AS avg_checkins, ROUND(AVG(coffee_cups),1) AS avg_coffee\n",
    "           FROM daily GROUP BY weekday ORDER BY avg_checkins DESC;\"\"\",\n",
    "    \"Q4. Temperature bands with >=50 days (HAVING)\":\n",
    "        \"\"\"SELECT temp_band, COUNT(*) AS days, ROUND(AVG(coffee_cups),1) AS avg_coffee\n",
    "           FROM daily GROUP BY temp_band HAVING COUNT(*) >= 50 ORDER BY avg_coffee DESC;\"\"\",\n",
    "    \"Q5. Month with highest avg coffee\":\n",
    "        \"\"\"SELECT SUBSTR(date,1,7) AS month, ROUND(AVG(coffee_cups),1) AS avg_coffee\n",
    "           FROM daily GROUP BY month ORDER BY avg_coffee DESC LIMIT 3;\"\"\",\n",
    "    \"Q6. Cold AND rainy days vs everything else\":\n",
    "        \"\"\"SELECT CASE WHEN temp_c < 10 AND is_rainy = 1 THEN 'Cold + rain' ELSE 'Other' END AS grp,\n",
    "                  ROUND(AVG(coffee_cups),1) AS avg_coffee, COUNT(*) AS days\n",
    "           FROM daily GROUP BY grp;\"\"\",\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ee8d3a7b-bd45-4706-a2cb-701454475771",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Q1. Avg coffee on days colder than 15°C\n",
      " avg_coffee  days\n",
      "      281.7   314\n",
      "\n",
      "Q2. Rainy vs dry days\n",
      "day_type  avg_coffee  avg_checkins  days\n",
      "     Dry       253.9         147.3   432\n",
      "   Rainy       294.6         183.2    68\n",
      "\n",
      "Q3. Weekday ranking (avg check-ins)\n",
      "  weekday  avg_checkins  avg_coffee\n",
      " Saturday         182.8       247.2\n",
      "   Sunday         178.6       240.2\n",
      "   Monday         143.7       269.2\n",
      " Thursday         142.1       262.9\n",
      "   Friday         140.9       267.4\n",
      "  Tuesday         140.7       264.1\n",
      "Wednesday         137.1       264.6\n",
      "\n",
      "Q4. Temperature bands with >=50 days (HAVING)\n",
      "temp_band  days  avg_coffee\n",
      "     <5°C   199       289.9\n",
      "   5–15°C   118       266.7\n",
      "  15–25°C   119       234.2\n",
      "    >25°C    64       198.0\n",
      "\n",
      "Q5. Month with highest avg coffee\n",
      "  month  avg_coffee\n",
      "2025-01       297.9\n",
      "2025-12       296.8\n",
      "2025-02       294.6\n",
      "\n",
      "Q6. Cold AND rainy days vs everything else\n",
      "        grp  avg_coffee  days\n",
      "Cold + rain       323.0    25\n",
      "      Other       256.1   475\n",
      "\n"
     ]
    }
   ],
   "source": [
    "sql_out = []\n",
    "for title, q in queries.items():\n",
    "    res = pd.read_sql(q, con)\n",
    "    print(title); print(res.to_string(index=False)); print()\n",
    "    sql_out.append((title, q, res))\n",
    "con.close()\n",
    "\n",
    "with open(\"queries.sql\", \"w\") as f:\n",
    "    for title, q, _ in sql_out:\n",
    "        f.write(f\"-- {title}\\n{q}\\n\\n\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "32b517d5-4d33-4359-9588-618c3e95cff8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#4) Charts (Seaborn) \n",
    "sns.set_theme(style=\"whitegrid\", rc={\n",
    "    \"axes.facecolor\": SURFACE, \"figure.facecolor\": SURFACE, \"grid.color\": \"#e6e5e1\",\n",
    "    \"axes.edgecolor\": \"#c9c8c2\", \"text.color\": INK, \"axes.labelcolor\": MUTED,\n",
    "    \"xtick.color\": MUTED, \"ytick.color\": MUTED, \"font.size\": 11})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "db16a648-fcf8-4f03-85a8-3a6c4f07f4e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Charts saved.\n"
     ]
    }
   ],
   "source": [
    "# Chart 1: temperature vs coffee, rainy vs dry\n",
    "fig, ax = plt.subplots(figsize=(9, 5.5))\n",
    "for rainy, color, label in [(0, BLUE, \"Dry day\"), (1, ORANGE, \"Rainy day\")]:\n",
    "    sub = df[df.is_rainy == rainy]\n",
    "    ax.scatter(sub.temp_c, sub.coffee_cups, s=22, color=color, alpha=0.75,\n",
    "               edgecolor=SURFACE, linewidth=0.8, label=label)\n",
    "    m, b = np.polyfit(sub.temp_c, sub.coffee_cups, 1)\n",
    "    xs = np.linspace(sub.temp_c.min(), sub.temp_c.max(), 50)\n",
    "    ax.plot(xs, m * xs + b, color=color, lw=2)\n",
    "r = corr.loc[\"temp_c\", \"coffee_cups\"]\n",
    "ax.set_title(f\"Colder days sell more coffee, and rain adds more (r = {r})\",\n",
    "             loc=\"left\", fontsize=14, fontweight=\"bold\", color=INK)\n",
    "ax.set_xlabel(\"Temperature, °C\"); ax.set_ylabel(\"Coffee cups per day\")\n",
    "ax.legend(frameon=False, loc=\"upper right\")\n",
    "sns.despine()\n",
    "fig.tight_layout(); fig.savefig(\"chart1_temp_vs_coffee.png\", dpi=160); plt.close(fig)\n",
    "\n",
    "# Chart 2: avg check-ins by weekday\n",
    "order = [\"Monday\", \"Tuesday\", \"Wednesday\", \"Thursday\", \"Friday\", \"Saturday\", \"Sunday\"]\n",
    "wk = df.groupby(\"weekday\")[\"cafe_checkins\"].mean().reindex(order)\n",
    "fig, ax = plt.subplots(figsize=(9, 5))\n",
    "bars = ax.bar(wk.index.str[:3], wk.values, color=[BLUE] * 5 + [ORANGE] * 2, width=0.6)\n",
    "for bar, v in zip(bars, wk.values):\n",
    "    ax.text(bar.get_x() + bar.get_width() / 2, v + 2, f\"{v:.0f}\", ha=\"center\", color=INK, fontsize=10)\n",
    "ax.set_title(\"Weekends fill the cafés\", loc=\"left\", fontsize=14, fontweight=\"bold\", color=INK)\n",
    "ax.set_ylabel(\"Average café check-ins\"); ax.set_ylim(0, wk.max() * 1.15)\n",
    "sns.despine()\n",
    "fig.tight_layout(); fig.savefig(\"chart2_weekday_checkins.png\", dpi=160); plt.close(fig)\n",
    "\n",
    "# Chart 3: correlation heatmap (single hue sequential + diverging-ish via blue/orange)\n",
    "fig, ax = plt.subplots(figsize=(7.5, 6))\n",
    "sns.heatmap(corr, annot=True, cmap=sns.diverging_palette(40, 255, s=85, l=55, center=\"light\", as_cmap=True),\n",
    "            vmin=-1, vmax=1, center=0, linewidths=2, linecolor=SURFACE, cbar_kws={\"shrink\": 0.8}, ax=ax)\n",
    "ax.set_title(\"Correlation matrix\", loc=\"left\", fontsize=14, fontweight=\"bold\", color=INK)\n",
    "plt.xticks(rotation=30, ha=\"right\")\n",
    "fig.tight_layout(); fig.savefig(\"chart3_correlation_heatmap.png\", dpi=160); plt.close(fig)\n",
    "\n",
    "print(\"Charts saved.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc20bfba-443e-4893-993f-e2449e07814e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
