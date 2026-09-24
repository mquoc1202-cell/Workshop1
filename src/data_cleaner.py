import pandas as pd
import numpy as np

def clean_movie_data(df_raw: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Làm sạch tập dữ liệu thô movies.csv tạo tập dữ liệu sạch tổng quan (dataset_clean.csv)
    và lưu lại bảng truy xuất nguồn gốc chất lượng dữ liệu (data quality trace).
    """
    trace_records = []
    current_df = df_raw.copy()
    initial_count = len(current_df)

    # 1. Deduplication by ID
    df_dedup = current_df.drop_duplicates(subset=['id']).copy()
    dedup_count = len(df_dedup)
    trace_records.append({
        'Step': 1,
        'Cleaning_Action': 'Deduplication',
        'Target_Column': 'id',
        'Records_Before': initial_count,
        'Records_Removed': initial_count - dedup_count,
        'Records_Remaining': dedup_count,
        'Justification': 'Deduplicate by unique entity id.'
    })

    # 2. Filter Missing Titles
    df_title = df_dedup.dropna(subset=['title']).copy()
    df_title = df_title[df_title['title'].astype(str).str.strip() != ''].copy()
    title_count = len(df_title)
    trace_records.append({
        'Step': 2,
        'Cleaning_Action': 'Remove Missing Titles',
        'Target_Column': 'title',
        'Records_Before': dedup_count,
        'Records_Removed': dedup_count - title_count,
        'Records_Remaining': title_count,
        'Justification': 'Remove records without valid title.'
    })

    # 3. Standardize & Validate Release Date
    df_date = df_title.copy()
    df_date['release_date'] = pd.to_datetime(df_date['release_date'], errors='coerce')
    df_date = df_date.dropna(subset=['release_date']).copy()
    date_count = len(df_date)
    trace_records.append({
        'Step': 3,
        'Cleaning_Action': 'Validate Release Date',
        'Target_Column': 'release_date',
        'Records_Before': title_count,
        'Records_Removed': title_count - date_count,
        'Records_Remaining': date_count,
        'Justification': 'Convert release_date to datetime and remove invalid dates.'
    })

    # 4. Handle Impossible Negative Financial Values (revenue < 0 or budget < 0)
    df_financial = df_date.copy()
    invalid_financial_mask = (df_financial['revenue'] < 0) | (df_financial['budget'] < 0)
    df_financial = df_financial[~invalid_financial_mask].copy()
    financial_count = len(df_financial)
    trace_records.append({
        'Step': 4,
        'Cleaning_Action': 'Filter Impossible Financials',
        'Target_Column': 'revenue, budget',
        'Records_Before': date_count,
        'Records_Removed': date_count - financial_count,
        'Records_Remaining': financial_count,
        'Justification': 'Remove records with impossible negative revenue or budget (< 0).'
    })

    # 5. Fill Missing Categorical Columns with 'Unknown'
    df_clean = df_financial.copy()
    categorical_cols = ['genres', 'production_companies', 'spoken_languages', 'production_countries']
    for col in categorical_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].fillna('Unknown')

    # 6. Create Data Availability Indicator Flags
    df_clean['has_revenue_data'] = df_clean['revenue'].apply(lambda x: 1 if pd.notna(x) and x > 0 else 0)
    df_clean['has_budget_data'] = df_clean['budget'].apply(lambda x: 1 if pd.notna(x) and x > 0 else 0)

    # 7. Extract Time Features
    df_clean['release_year'] = df_clean['release_date'].dt.year.astype(int)
    df_clean['release_month'] = df_clean['release_date'].dt.month.astype(int)

    df_trace = pd.DataFrame(trace_records)
    return df_clean, df_trace


def prepare_data_for_gh1(df_clean: pd.DataFrame) -> pd.DataFrame:
    """
    Tạo tập dữ liệu chuyên biệt phục vụ phân tích Giả thuyết 1 (revenue > 0 và vote_count >= 10).
    """
    df_gh1 = df_clean[(df_clean['revenue'] > 0) & (df_clean['vote_count'] >= 10)].copy()
    df_gh1['log_revenue'] = np.log10(df_gh1['revenue'])
    df_gh1['log_vote_count'] = np.log10(df_gh1['vote_count'])
    return df_gh1
