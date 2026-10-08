{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4659a122-01a2-453a-9c28-793d05a3c4fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4249327f-e891-45c9-8253-d6466f73e355",
   "metadata": {},
   "outputs": [],
   "source": [
    "rng = np.random.default_rng(42)\n",
    "N = 500"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "59811476-d0e6-4761-a7d3-91ad0efa46c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "dates = pd.date_range(\"2025-01-01\", periods=N, freq=\"D\")\n",
    "day_of_year = dates.dayofyear.to_numpy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3c1372ef-daff-4b23-b766-e9f5253c0692",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Yerevan seasonal temperature(-3C in Jan,28C in July)\n",
    "temp = 12.5 - 15.5 * np.cos(2 * np.pi * (day_of_year - 15) / 365) + rng.normal(0, 3, N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fb210cdf-97e5-4c12-b293-785a087f3407",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rain probability: more likely in spring/autumn and when it is cooler\n",
    "rain_prob = 0.10 + 0.12 * ((day_of_year > 80) & (day_of_year < 150)) \\\n",
    "            + 0.10 * ((day_of_year > 270) & (day_of_year < 330))\n",
    "is_rainy = rng.random(N) < rain_prob\n",
    "precip_mm = np.where(is_rainy, rng.gamma(2.0, 3.0, N), 0.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "456647a9-839f-45e2-9c53-ac4fc8dcda16",
   "metadata": {},
   "outputs": [],
   "source": [
    "weekday = dates.dayofweek.to_numpy() \n",
    "is_weekend = weekday >= 5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7edb8b62-c12e-4b9f-b7fa-d701277096a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Coffee cups sold\n",
    "coffee = (\n",
    "    220\n",
    "    - 3.2 * (temp - 15)              \n",
    "    + 45 * is_rainy                  \n",
    "    + 0.8 * precip_mm\n",
    "    + 25 * (weekday < 5)            \n",
    "    + rng.normal(0, 18, N)\n",
    ").clip(min=40)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2228e3f3-007d-42e8-848d-4ad4fddc0b0b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# people sitting in cafes\n",
    "checkins = (\n",
    "    150\n",
    "    + 35 * is_rainy\n",
    "    + 40 * is_weekend\n",
    "    - 1.2 * np.abs(temp - 20)       \n",
    "    + rng.normal(0, 15, N)\n",
    ").clip(min=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "94165e6e-c548-4be1-8583-d1df763bca5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({\n",
    "    \"date\": dates,\n",
    "    \"temp_c\": temp.round(1),\n",
    "    \"is_rainy\": is_rainy.astype(int),\n",
    "    \"precip_mm\": precip_mm.round(1),\n",
    "    \"weekday\": dates.day_name(),\n",
    "    \"coffee_cups\": coffee.round().astype(int),\n",
    "    \"cafe_checkins\": checkins.round().astype(int),\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c342998c-2db2-4bee-bff8-c4f2be08ac55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(500, 7)\n",
      "        date  temp_c  is_rainy  precip_mm    weekday  coffee_cups  \\\n",
      "0 2025-01-01    -1.6         0        0.0  Wednesday        310.0   \n",
      "1 2025-01-02    -5.7         0        0.0   Thursday        289.0   \n",
      "2 2025-01-03    -0.4         0        0.0     Friday        326.0   \n",
      "3 2025-01-04     0.1         0        0.0   Saturday        280.0   \n",
      "4 2025-01-05    -8.6         0        0.0     Sunday        295.0   \n",
      "\n",
      "   cafe_checkins  \n",
      "0            119  \n",
      "1            110  \n",
      "2            151  \n",
      "3            169  \n",
      "4            168  \n"
     ]
    }
   ],
   "source": [
    "# Add a few realistic \"dirty\" values so the cleaning step is meaningful\n",
    "dirty_idx = rng.choice(N, 12, replace=False)\n",
    "df.loc[dirty_idx[:6], \"temp_c\"] = np.nan\n",
    "df.loc[dirty_idx[6:9], \"coffee_cups\"] = np.nan\n",
    "df.loc[dirty_idx[9:], \"temp_c\"] = 99.9  # sensor error\n",
    "\n",
    "df.to_csv(\"yerevan_coffee_weather.csv\", index=False)\n",
    "print(df.shape)\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7b83f71-2db7-4604-8e88-e260c07ba4c3",
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
