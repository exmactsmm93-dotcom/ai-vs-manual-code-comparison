# AI vs. Manual Code Comparison: Data Analysis

This project performs a comparative analysis of data processing and visualization using two different Python stacks. It also includes a case study comparing manually written code against AI-generated solutions.

## 📊 Project Scope
- **Datasets:** US Avocado Prices and Student Exam Performance.
- **Manual Implementation:** Using `Pandas` and `Seaborn`.
- **Advanced Implementation:** Using `Polars` (Lazy evaluation) and `Altair` (Declarative visualization).
- **ETL:** Data transformation and loading into `SQLite3` using the `PETL` library.

## 📁 Repository Structure
- `/scripts`: Python scripts for data analysis and plotting.
- `/data`: Source CSV files.
- `/docs`: Comparison report detailing AI vs. Manual coding performance.

## 🛠️ Requirements
To run these scripts, you will need:
```bash
pip install pandas polars altair seaborn petl vegafusion

## Key Findings from the Comparison Report

### 1. Code Efficiency & Logic
* **Manual Code:** Utilized specific Polars lazy evaluation techniques (`pl.scan_csv`) which are optimized for larger datasets and provide more granular control over data types.
* **AI Code:** Tended to produce "one-size-fits-all" solutions. While functional, it sometimes missed the specific performance benefits of the Polars lazy API unless explicitly prompted.

### 2. Visualization Accuracy
* **Customization:** Manual implementation using Altair allowed for better axis scaling (e.g., scaling volume by $1e7$) and custom color palettes that made the Avocado data more readable.
* **AI Limitations:** AI-generated plots often lacked fine-tuning for labels and legends, requiring manual "post-processing" to meet professional standards.

### 3. The "Human in the Loop"
* The study found that while AI is an excellent tool for rapid prototyping, a developer's understanding of the underlying library (Polars/Altair) is essential to catch errors in data filtering and to optimize performance.
