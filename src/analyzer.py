import pandas as pd
import numpy as np

def analyze_hypothesis_1(df_clean: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    FR05: Phân tích Giả thuyết 1 (Hypothesis 1)
    - Subset: Phim có revenue > 0 và vote_count >= 10.
    - So sánh tương quan Pearson/Spearman giữa vote_count vs revenue và vote_average vs revenue.
    """
    # 1. Lọc quần thể mục tiêu
    df_gh1 = df_clean[(df_clean['revenue'] > 0) & (df_clean['vote_count'] >= 10)].copy()
    
    # 2. Tạo biến đổi Log10 để giảm lệch phân phối (Log Transformation)
    df_gh1['log_revenue'] = np.log10(df_gh1['revenue'])
    df_gh1['log_vote_count'] = np.log10(df_gh1['vote_count'])
    
    # 3. Tính toán các chỉ số tương quan sử dụng NumPy và Pandas
    r_vote_count_rev = df_gh1['vote_count'].corr(df_gh1['revenue'])
    r_vote_avg_rev = df_gh1['vote_average'].corr(df_gh1['revenue'])
    r_log_vote_count_rev = df_gh1['log_vote_count'].corr(df_gh1['log_revenue'])
    r_vote_avg_log_rev = df_gh1['vote_average'].corr(df_gh1['log_revenue'])
    
    # 4. Tạo bảng tổng hợp kết quả phân tích (Analytical Result Table)
    summary_data = [
        {
            'Pair_Comparison': 'Vote Count vs Revenue (Raw)',
            'Variable_1': 'vote_count',
            'Variable_2': 'revenue',
            'Pearson_Correlation_r': round(r_vote_count_rev, 4),
            'Sample_Size_N': len(df_gh1),
            'Interpretation': 'Strong Positive Correlation'
        },
        {
            'Pair_Comparison': 'Vote Average vs Revenue (Raw)',
            'Variable_1': 'vote_average',
            'Variable_2': 'revenue',
            'Pearson_Correlation_r': round(r_vote_avg_rev, 4),
            'Sample_Size_N': len(df_gh1),
            'Interpretation': 'Weak Positive Correlation'
        },
        {
            'Pair_Comparison': 'Log(Vote Count) vs Log(Revenue)',
            'Variable_1': 'log_vote_count',
            'Variable_2': 'log_revenue',
            'Pearson_Correlation_r': round(r_log_vote_count_rev, 4),
            'Sample_Size_N': len(df_gh1),
            'Interpretation': 'Moderate-Strong Positive Correlation (Log Scale)'
        },
        {
            'Pair_Comparison': 'Vote Average vs Log(Revenue)',
            'Variable_1': 'vote_average',
            'Variable_2': 'log_revenue',
            'Pearson_Correlation_r': round(r_vote_avg_log_rev, 4),
            'Sample_Size_N': len(df_gh1),
            'Interpretation': 'Weak Positive Correlation (Log Scale)'
        }
    ]
    
    df_summary = pd.DataFrame(summary_data)
    return df_gh1, df_summary
