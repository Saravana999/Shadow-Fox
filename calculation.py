{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ff4e35cd-4b08-4e1b-bbf8-84f5b76a32a6",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AQI calculation completed.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load the data\n",
    "data = pd.read_csv(\"Downloads/processed_delhiaqi.csv\")\n",
    "\n",
    "# Define AQI breakpoints and corresponding AQI values\n",
    "aqi_breakpoints = [\n",
    "    (0, 12.0, 50), (12.1, 35.4, 100), (35.5, 55.4, 150),\n",
    "    (55.5, 150.4, 200), (150.5, 250.4, 300), (250.5, 350.4, 400),\n",
    "    (350.5, 500.4, 500)\n",
    "]\n",
    "\n",
    "def calculate_aqi(concentration):\n",
    "    for low, high, aqi in aqi_breakpoints:\n",
    "        if low <= concentration <= high:\n",
    "            return aqi\n",
    "    return None\n",
    "\n",
    "def calculate_overall_aqi(row):\n",
    "    aqi_values = []\n",
    "    pollutants = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']\n",
    "    for pollutant in pollutants:\n",
    "        aqi = calculate_aqi(row[pollutant])\n",
    "        if aqi is not None:\n",
    "            aqi_values.append(aqi)\n",
    "    return max(aqi_values) if aqi_values else None\n",
    "\n",
    "# Calculate AQI for each row\n",
    "data['AQI'] = data.apply(calculate_overall_aqi, axis=1)\n",
    "\n",
    "# Save the data with AQI\n",
    "data.to_csv(\"Downloads/aqi_calculated_delhiaqi.csv\", index=False)\n",
    "print(\"AQI calculation completed.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92b37a2b-9765-4438-9984-6a45293b41fc",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
