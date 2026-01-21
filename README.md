# AI vs. Manual Code Comparison: Data Analysis Project

This project explores data analysis and visualization using high-performance Python libraries. It features a comparative study between manually written code and AI-generated solutions, focusing on efficiency, logic, and visualization quality.

## Project Overview
- **Datasets:** US Avocado Prices and Student Exam Performance.
- **Technologies:** - **Data Handling:** `Polars` (Lazy Evaluation) vs. `Pandas`.
  - **Visualization:** `Altair` (Declarative) vs. `Seaborn/Matplotlib`.
  - **ETL:** `PETL` for data cleaning and migration to `SQLite3`.

## Key Findings from the Report
Based on my comparison analysis (included in the `docs` folder):

* **Manual Precision:** My manual code utilized Polars' `scan_csv` for lazy evaluation. This provides better memory management for large datasets compared to standard AI-generated scripts.
* **Custom Visualization:** Manual plotting with Altair allowed for complex scaling (e.g., scaling Total Volume by $1e7$) which AI often overlooked, leading to clearer data storytelling.
* **AI as an Assistant:** While AI is excellent for rapid prototyping and fixing syntax errors, human oversight is essential for fine-tuning axes, formatting labels, and handling specific data nuances.

## Repository Structure
- `/data`: Source CSV files (`avocado.csv`, `exams.csv`).
- `/scripts`: Python scripts covering Pandas, Polars, Altair, and PETL implementations.
- `/docs`: Full comparison report (`A00325707_Comparison_Report.pdf`).

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/exmactsmm93-dotcom/ai-vs-manual-code-comparison.git](https://github.com/exmactsmm93-dotcom/ai-vs-manual-code-comparison.git)

2.**Install required libraries**
 pip install polars altair pandas seaborn petl vegafusion numpy

3.**Execute the analysis scripts**
	python scripts/Q3_Q1PlotAltair.py

4. Click the green **Commit changes...** button to save.

---

### 2. How to add a `requirements.txt` file (Highly Recommended)
Instead of making people type a long `pip install` command, a `requirements.txt` file allows them to install everything at once. 

**Steps to add it:**
1.  Go to your main repository page: [ai-vs-manual-code-comparison](https://github.com/exmactsmm93-dotcom/ai-vs-manual-code-comparison).
2.  Click **Add file** > **Create new file**.
3.  Name the file exactly: `requirements.txt`
4.  Paste this list into the file:
    ```text
    polars
    altair
    pandas
    seaborn
    petl
    vegafusion
    numpy
    ```
5.  Click **Commit changes...**


---

### 3. Final Step: Organizing your Files
To make the "Execute" command (`python scripts/Q3_Q1PlotAltair.py`) work, you must move your files into folders. 

**On your main GitHub page:**
1. Click **Add file** > **Upload files**.
2. **Crucial:** When you drag and drop your files, GitHub doesn't let you "create" folders easily in the upload window. It is best to **create the folders on your computer first** (put all `.py` files in a folder named `scripts`, and `.csv` files in a folder named `data`), then drag those whole folders into the GitHub upload box.
3.
4. 
   
   ```bash
   git clone [https://github.com/exmactsmm93-dotcom/ai-vs-manual-code-comparison.git](https://github.com/exmactsmm93-dotcom/ai-vs-manual-code-comparison.git)
