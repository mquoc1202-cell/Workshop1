Training Assignments Python Programming for AI PPA.MP01 

**PYTHON PROGRAMMING FOR AI Mini-Project Assignment** 

**MINI-PROJECT 1** 

**Tabular Data Exploration, Analysis, and Visualization**

| Document Code  | PPA.MP01 |
| :---- | :---- |
| **Version**  | **1.0** |
| **Assignment Type**  | **TEAM MINI-PROJECT** |
| **Assessment Weight**  | **20% of course grade** |

Training Assignments Python Programming for AI PPA.MP01 

| CODE:  | PPA.MP01 |
| :---: | ----- |
| TYPE:  | TEAM MINI-PROJECT |
| TEAM SIZE:  | 5 TRAINEES |
| WEIGHT:  | 20% |

**Assignment \- Tabular Data Exploration, Analysis, and Visualization 1\. Objectives**   
• Select and justify a suitable public tabular dataset from Kaggle. 

• Profile dataset structure, data types, distributions, missing values, duplicate records, and data-quality  limitations. 

• Formulate three measurable and testable hypotheses from the available variables. • Clean, transform, aggregate, and analyze data using NumPy and Pandas. 

• Create clear and appropriate visualizations using Matplotlib and Seaborn. 

• Use evidence to accept, reject, or mark each hypothesis as inconclusive. 

• Organize the solution into readable modules, apply PEP 8 and clean-code practices, and verify critical logic  with pytest. 

• Present findings, limitations, and team contributions clearly. 

**2\. Working Environments** 

• Python 3.x 

• Visual Studio Code or Jupyter Notebook 

• NumPy 

• Pandas 

• Matplotlib 

• Seaborn 

• pytest 

• Git or another team version-control workflow 

**Installation command:** python \-m pip install numpy pandas matplotlib seaborn pytest 

**3\. Assignment Description** 

Your team will conduct an end-to-end exploratory analysis of a real-world tabular dataset selected from Kaggle.  The project must move from raw data to defensible findings through a transparent workflow: dataset selection,  profiling, cleaning, hypothesis formulation, analysis, visualization, interpretation, and review. 

**Machine learning model development is not required.** The primary objective is to demonstrate reliable data  exploration and evidence-based reasoning using the Python data stack. 

**Core question** What does the selected dataset support you in claiming, and what does it not establish?  
Training Assignments Python Programming for AI PPA.MP01 

**4\. Team and Dataset Requirements**

| Item  | Requirement |
| :---: | ----- |
| Team size  | 5 trainees |
| Dataset source  | A public Kaggle dataset with an accessible dataset page and reusable license or usage terms |
| Data form  | Structured tabular data, preferably CSV |
| Minimum scope  | At least 500 records and 5 meaningful analytical columns |
| Domain  | A real-world area such as education, healthcare, commerce, finance, media, sports, tourism,  or customer behavior |
| Privacy  | Do not use confidential company data, personal credentials, or unlawfully obtained personal  data |
| Project boundary  | Exploratory analysis and hypothesis evaluation. No machine learning model is required. |

Training Assignments Python Programming for AI PPA.MP01 

**5\. Functional Requirements** 

**FR01 \- Select and Register the Dataset** 

• Select one suitable dataset from Kaggle and record the dataset title, publisher, Kaggle page, license or usage  information, domain context, update/version information if available, and download date. • Explain why the dataset is suitable for the project objectives and the three intended hypotheses. • Keep the original dataset unchanged in the raw-data folder. 

**FR02 \- Profile the Dataset** 

• Report the number of rows and columns, column names, inferred data types, and a data dictionary. • Identify numerical, categorical, Boolean, identifier, date/time, and free-text fields where applicable. • Report missing values, exact duplicates, candidate business keys, suspicious ranges, inconsistent categories,  and potential outliers. 

• Provide descriptive statistics for numerical fields and frequency summaries for categorical fields. **FR03 \- Define Three Hypotheses**   
• Create exactly three analytical hypotheses before performing the final hypothesis analysis. • Each hypothesis must state a measurable relationship, comparison, difference, trend, or distribution pattern  supported by available columns. 

• For each hypothesis, identify the variables, population or subset, metric, planned analysis, planned  visualization, and decision rule. 

• Avoid causal language unless the dataset and analysis design genuinely support causality. **FR04 \- Prepare and Clean Data**   
• Document every cleaning rule and its justification. 

• Handle missing values, duplicates, inconsistent labels, invalid types, and impossible or out-of-range values  appropriately. 

• Create derived analytical columns only when their definitions are explicit and reproducible. • Preserve a data-quality trace showing row counts and major changes at each stage. 

**FR05 \- Analyze Each Hypothesis** 

• Apply suitable selection, filtering, sorting, grouping, aggregation, and comparison operations. • Use NumPy where array-based numerical processing is meaningful and Pandas for labeled tabular  workflows. 

• Provide at least one analytical result table for each hypothesis. 

• Check whether missing values, group imbalance, outliers, or limited sample size could affect interpretation. **FR06 \- Visualize the Evidence**   
• Create at least one primary visualization for each hypothesis. 

• Choose chart type according to the analytical question: line for ordered trends, bar for category comparisons,  histogram for distributions, scatter for relationships, and box plot for spread and outliers. • Use clear titles, axis labels, units, readable categories, legends only when needed, and non-misleading  scales. 

• Save final charts as reproducible image files in the output folder. 

**FR07 \- Evaluate Hypotheses** 

• Classify each hypothesis as Accepted, Rejected, or Inconclusive. 

• Link the decision to numeric evidence and the visualization. 

• Explain limitations and alternative interpretations. 

• Do not treat correlation or visual association as proof of causation.  
Training Assignments Python Programming for AI PPA.MP01 

**FR08 \- Package Reproducible Results** 

• Export the cleaned analytical dataset, summary tables, charts, and hypothesis evaluation table. • Ensure a reviewer can reproduce all outputs from the submitted raw data and source code. • Record software dependencies and execution instructions in README.md. 

**6\. Technical Requirements**

| ID  | Requirement |
| :---: | ----- |
| TR01  | Use functions with explicit inputs and return values for major processing steps. |
| TR02  | Use multiple modules or clearly separated notebook sections with single purposes. |
| TR03  | Use Pandas for loading, inspecting, cleaning, selecting, filtering, grouping, aggregating, and exporting tabular  data. |
| TR04  | Use NumPy where vectorized numerical operations or array summaries add value. |
| TR05  | Use Matplotlib and Seaborn for final visualizations. |
| TR06  | Write pytest tests for at least three critical functions or rules, including one boundary or invalid case. |
| TR07  | Apply meaningful names, PEP 8, DRY, and appropriate comments or docstrings. |
| TR08  | Do not hard-code machine-specific absolute paths. Use pathlib or relative project paths. |
| TR09  | Use fixed random seeds whenever sampling or randomized display logic is introduced. |
| TR10  | Do not silently remove or alter records. Every major data-quality decision must be traceable. |

Training Assignments Python Programming for AI PPA.MP01 

**7\. Recommended Project Structure** 

| PPA.MP01\_\<TeamName\>/  |-- README.md  |-- requirements.txt  |-- main.py  |-- data/  | |-- raw/  | | \`-- dataset.csv  | \`-- processed/  | \`-- dataset\_clean.csv  |-- notebooks/  | \`-- exploration.ipynb  |-- src/  | |-- \_\_init\_\_.py  | |-- data\_loader.py  | |-- data\_cleaner.py  | |-- analyzer.py  | \`-- visualizer.py  |-- tests/  | \`-- test\_pipeline.py  |-- outputs/  | |-- tables/  | |-- figures/  | \`-- hypothesis\_results.csv  |-- report/  | \`-- mini\_project\_1\_report.pdf  \`-- slides/   \`-- mini\_project\_1\_presentation.pptx |
| :---- |

**8\. Expected Processing Flow** 

**Select Kaggle dataset** 

↓ 

**Register source and assumptions** 

↓ 

**Load raw data** 

↓ 

**Profile structure and quality** 

↓ 

**Define three hypotheses** 

↓ 

**Clean and transform** 

↓ 

**Analyze each hypothesis** 

↓ 

**Create visual evidence** 

↓ 

**Evaluate hypotheses** 

↓ 

**Export results** 

↓ 

**Present and defend findings**  
Training Assignments Python Programming for AI PPA.MP01 

**9\. Required Deliverables** 

| No.  | Deliverable  | Minimum content |
| :---: | ----- | :---: |
| 1  | Source code  | Reproducible loading, cleaning, analysis, visualization, export, and tests |
| 2  | Raw and processed data  | Original dataset or approved retrieval instructions, plus cleaned analytical dataset |
| 3  | Project report  | Dataset context, profile, cleaning decisions, three hypotheses, methods, results, charts,  conclusions, and limitations |
| 4  | Presentation  | Maximum 10 slides for a 10-minute team presentation |
| 5  | Evidence package  | Summary tables, image files, hypothesis result table, and pytest results |
| 6  | README  | Environment setup, execution steps, project structure, dataset citation, and team roles |

**10\. Evaluation Criteria** 

| No.  | Evaluation Area  | Weight  | Meets Expectations |
| ----- | ----- | ----- | ----- |
| 1  | Dataset selection and source  documentation  | 10%  | Suitable dataset; source, context, license/usage information, and  limitations documented |
| 2  | Dataset profiling and data-quality  analysis  | 15%  | Structure, types, missingness, duplicates, ranges, distributions, and  risks analyzed |
| 3  | Hypothesis quality  | 15%  | Three clear, measurable, testable, and data-supported hypotheses |
| 4  | Cleaning and transformation  | 15%  | Rules are justified, reproducible, and traceable |
| 5  | Analysis correctness  | 15%  | Metrics, filters, groups, comparisons, and denominators are correct |
| 6  | Visualization quality  | 10%  | Charts match questions and communicate evidence honestly |
| 7  | Conclusions and limitations  | 10%  | Each decision follows evidence and includes cautious interpretation |
| 8  | Code quality, testing, and   reproducibility  | 5%  | Readable modular code, tests, dependencies, and repeatable outputs |
| 9  | Presentation and team contribution  | 5%  | Clear delivery, balanced participation, and effective response to  questions |
|  | TOTAL  | 100% |  |

**Minimum completion criteria** The submission must include one documented Kaggle dataset, three  hypotheses, reproducible analysis, at least three primary visualizations, three evidence-based decisions,  source code, report, and presentation.  
Training Assignments Python Programming for AI PPA.MP01 

**11\. Presentation and Review** 

| Slide  | Recommended Content |
| :---: | ----- |
| 1  | Project title, team members, and analytical objective |
| 2  | Dataset source, domain, license/usage information, and scope |
| 3  | Dataset characteristics and important quality issues |
| 4  | Cleaning and transformation decisions |
| 5  | Hypothesis 1: method, evidence, visualization, and decision |
| 6  | Hypothesis 2: method, evidence, visualization, and decision |
| 7  | Hypothesis 3: method, evidence, visualization, and decision |
| 8  | Cross-cutting findings and limitations |
| 9  | Technical design, testing, and reproducibility |
| 10  | Conclusions, lessons learned, and next steps |

• Presentation time: 10 minutes. 

• Question-and-answer time: determined by the trainer during Project Review 1\. 

• Every team member must explain a substantive part of the work. 

• The team must be able to trace each conclusion to code, a result table, and a visualization. **12\. Submission Guidelines**   
• Name the root folder PPA.MP01\_\<TeamName\>. 

• Compress the complete project as PPA.MP01\_\<TeamName\>.zip. 

• Include requirements.txt and execution instructions. 

• Include the Kaggle dataset page in the report and README. If redistribution is restricted, include retrieval  instructions instead of republishing the file. 

• Do not include virtual environments, cache folders, credentials, tokens, or unnecessary generated files. • Confirm the project runs from the project root in a clean environment. 

• Submit the report as PDF and the presentation as PPTX. 

**13\. Constraints** 

• The analysis must be implemented in Python. 

• The dataset must be selected from Kaggle. 

• Exactly three hypotheses must be evaluated. 

• Machine learning model training is outside the project scope. 

• Conclusions must be based on submitted evidence and must not fabricate unavailable facts. • Confidential, restricted, or unlawfully collected data must not be used. 

• Automated AI tools may support brainstorming or code review, but the team remains accountable for  correctness, attribution, and the ability to explain every submitted artifact.  
Training Assignments Python Programming for AI PPA.MP01 **14\. Submission Checklist** 

☐ One Kaggle dataset has been selected and documented. 

☐ The raw dataset is preserved or reproducibly retrievable. 

☐ Dataset structure and quality have been analyzed. 

☐ Exactly three hypotheses are stated with variables, methods, visualizations, and decision rules. ☐ Cleaning and transformation rules are documented. 

☐ Each hypothesis has a result table and at least one primary visualization. ☐ Each hypothesis is marked Accepted, Rejected, or Inconclusive with evidence. ☐ Limitations and non-causal interpretations are stated. 

☐ Source code is modular, readable, and reproducible. 

☐ At least three critical tests are included and pass. 

☐ Report, slides, outputs, README, and team contribution record are included. **\-- THE END \--**