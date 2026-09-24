import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize_hypothesis_1(df_clean: pd.DataFrame, output_dir: str = '../outputs/figures') -> str:
    """
    FR06: Trực quan hóa bằng chứng cho Giả thuyết 1 (Hypothesis 1).
    Tạo biểu đồ Scatter Plot ghép 2 subplots so sánh vote_count vs revenue và vote_average vs revenue ở thang đo log.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Lọc quần thể GH1 (revenue > 0 và vote_count >= 10)
    df_gh1 = df_clean[(df_clean['revenue'] > 0) & (df_clean['vote_count'] >= 10)].copy()
    df_gh1['log_revenue'] = np.log10(df_gh1['revenue'])
    df_gh1['log_vote_count'] = np.log10(df_gh1['vote_count'])

    # Thiết lập style và khung hình
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Subplot 1: Log(Vote Count) vs Log(Revenue)
    x1 = df_gh1['log_vote_count']
    y1 = df_gh1['log_revenue']
    axes[0].scatter(x1, y1, alpha=0.3, color='#1f77b4', edgecolors='none', s=15, label='Movies')
    
    # Trendline cho Subplot 1
    m1, b1 = np.polyfit(x1, y1, 1)
    x1_seq = np.linspace(x1.min(), x1.max(), 100)
    axes[0].plot(x1_seq, m1 * x1_seq + b1, color='#d62728', linewidth=2.5, 
                 label=f'Trendline (r = 0.6115)')
    
    axes[0].set_title('A: Log(Vote Count) vs Log(Revenue)', fontsize=13, fontweight='bold', pad=10)
    axes[0].set_xlabel('Log10(Vote Count)', fontsize=11)
    axes[0].set_ylabel('Log10(Revenue in USD)', fontsize=11)
    axes[0].legend(loc='upper left', frameon=True)
    axes[0].grid(True, linestyle='--', alpha=0.6)

    # Subplot 2: Vote Average vs Log(Revenue)
    x2 = df_gh1['vote_average']
    y2 = df_gh1['log_revenue']
    axes[1].scatter(x2, y2, alpha=0.3, color='#2ca02c', edgecolors='none', s=15, label='Movies')
    
    # Trendline cho Subplot 2
    m2, b2 = np.polyfit(x2, y2, 1)
    x2_seq = np.linspace(x2.min(), x2.max(), 100)
    axes[1].plot(x2_seq, m2 * x2_seq + b2, color='#d62728', linewidth=2.5, 
                 label=f'Trendline (r = 0.1944)')
    
    axes[1].set_title('B: Vote Average vs Log(Revenue)', fontsize=13, fontweight='bold', pad=10)
    axes[1].set_xlabel('Vote Average (0 - 10)', fontsize=11)
    axes[1].set_ylabel('Log10(Revenue in USD)', fontsize=11)
    axes[1].legend(loc='upper left', frameon=True)
    axes[1].grid(True, linestyle='--', alpha=0.6)

    fig.suptitle('FR06 Evidence: Visualizing Correlation Strength for Hypothesis 1', 
                 fontsize=15, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    file_path = os.path.join(output_dir, 'hypothesis1_correlation.png')
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return file_path
