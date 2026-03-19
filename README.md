# Data Engineering learning project

## Kaggle-to-Postgres ETL pipeline

Extracts data from https://www.kaggle.com/datasets/alanjo/cpu-benchmarks/data
A streamlined pipeline to automate data ingestion from Kaggle, processing with Pandas, and storage in PostgreSQL.

🚀 Overview

This pipeline automates the movement of datasets from the source to a relational database for further analysis.

🛠 Tech Stack

- Source: Kaggle API
- Processing: Python (Pandas)
- Storage: PostgreSQL
- Environment: Docker (optional) / Virtualenv
- Testing: Behave (gherkin)

⚙️ Setup & Usage

1. Prerequisites

Access to Kaggle dataset https://www.kaggle.com/datasets/alanjo/cpu-benchmarks/data.
Running PostgreSQL instance.

2. Installation

```sh
git clone <repo-url>
pip install -r requirements.txt
```

3. Configuration

Create an `.env` file:

```yml
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
POSTGRES_PORT=
POSTGRES_HOST=
```

4. Execution

```sh
python3 main.py
```

5. Behave tests:

```sh
behave
```