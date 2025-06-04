# Financial Data Concentration Analyzer

This is a Streamlit-based tool to upload Excel files, perform concentration analysis, and detect statistical anomalies using z-scores.

Built as a take-home project to demonstrate:

- Data ingestion from unknown schemas
- Interactive and auditable analysis
- Dynamic normalization and grouping
- AI-readiness and scalability
- Containerized reproducibility with Docker

## Features

- Upload `.xlsx` Excel files
- Auto-infer categorical, numeric, and date columns
- Dynamic column selection via UI
- Concentration analysis by year (Top 10%, 20%, 50%)
- Z-score-based anomaly detection (configurable threshold)
- Downloadable results and anomaly tables
- Fully Dockerized for reproducibility

## Tech Stack

- Python 3.10
- Streamlit
- Pandas
- OpenPyXL
- Docker

## File Structure

.
├── app.py
├── analysis.py
├── utils.py
├── requirements.txt
├── Dockerfile
├── README.md
└── sample_data.xlsx

## Run Locally (Python + Streamlit)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open your browser at:  
👉 http://localhost:8501
