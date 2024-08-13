# Handling Outliers with Z-Score
def ol_remover_zscore(data):
    # Calculate Z-scores
    z_scores = np.abs(stats.zscore(data))

    # Set a threshold for Z-score (common choice is 3)
    threshold = 3

    # Identify outliers
    outliers = np.where(z_scores > threshold)

    # Remove outliers
    df_no_outliers = data[(z_scores < threshold).all(axis=1)]

    return df_no_outliers

# Handling Outliers with IQR
def ol_remover_iqr(df):
    # Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)

    # Calculate IQR (Interquartile Range)
    IQR = Q3 - Q1

    # Define outlier criteria
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = (df < lower_bound) | (df > upper_bound)

    # Remove outliers
    df_no_outliers = df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]

    return df_no_outliers