import pandas as pd

def load_excel(file):
    try:
        df = pd.read_excel(file)
        df.columns = df.columns.str.strip().str.replace('\n', ' ')
        return df
    except Exception as e:
        print("Error reading file:", e)
        return None

def infer_schema(df):
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    num_cols = df.select_dtypes(include='number').columns.tolist()

    date_cols = []
    for col in df.columns:
        try:
            parsed = pd.to_datetime(df[col])
            if parsed.notnull().sum() > 0:
                date_cols.append(col)
        except:
            continue

    return cat_cols, num_cols, date_cols
