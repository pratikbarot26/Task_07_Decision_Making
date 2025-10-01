### Data Lineage and Provenance

- **Source:** Syracuse University official football stats PDFs (2021 & 2024, first-page cumulative stats).
- **Collection:** Manually transcribed into Python dictionaries in Task_05 notebook.
- **Cleaning/Preprocessing:**
  * Confirmed numeric columns (yards, points, plays) were cast to float.
  * Checked for missing values and corrected transcription errors.
  * Converted categorical variables (Home/Away, Conference/Non-Conf) to strings.
- **Limitations:** Only first-page stats; small sample size; no player-specific data.
- **Usage:** Scripts in /scripts/ generate descriptive stats, visualizations, and CSV tables using this data.