{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4f80358a-613e-4f63-9c2b-013ec719c1ed",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data processing completed.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load the data\n",
    "data = pd.read_csv(\"Downloads/delhiaqi.csv\")\n",
    "\n",
    "# Convert 'date' column to datetime\n",
    "data['date'] = pd.to_datetime(data['date'])\n",
    "\n",
    "# Extract date and time\n",
    "data['date_only'] = data['date'].dt.date\n",
    "data['time_only'] = data['date'].dt.time\n",
    "\n",
    "# Save the processed data\n",
    "data.to_csv(\"Downloads/processed_delhiaqi.csv\", index=False)\n",
    "print(\"Data processing completed.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db04af37-12f9-4b1e-a112-41eaa38690af",
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
