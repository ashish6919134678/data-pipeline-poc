import streamlit as st
import pandas as pd
from utils import load_excel, infer_schema
from analysis import compute_concentration, detect_anomalies

st.set_page_config(page_title="Financial Data Concentration Analyzer", layout="wide")
st.title("Financial Data Concentration Analyzer")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = load_excel(uploaded_file)

    if df is not None:
        st.subheader("File Preview")
        st.dataframe(df.head())

        cat_cols, num_cols, date_cols = infer_schema(df)

        if not cat_cols or not num_cols or not date_cols:
            st.error("Could not infer schema. Make sure your file has at least one text, numeric, and date column.")
        else:
            st.markdown("###Column Selection")
            category_col = st.selectbox("Select Categorical Column", cat_cols)
            value_col = st.selectbox("Select Numeric Column", num_cols)
            time_col = st.selectbox("Select Time/Date Column", date_cols)

            if st.button("Run Concentration Analysis"):
                
                output_df = compute_concentration(df, category_col, value_col, time_col)

                st.subheader("Concentration Analysis")
                st.dataframe(output_df)

                csv = output_df.to_csv(index=False).encode('utf-8')
                st.download_button("Download Result CSV", csv, "concentration_output.csv", "text/csv")

                
                st.markdown("---")

                
                st.subheader("Anomaly Detection (Revenue Outliers)")

                anomalies = detect_anomalies(df, value_col, z_thresh=1.5)

                if not anomalies.empty:
                    st.dataframe(anomalies)

                    csv_anomalies = anomalies.to_csv(index=False).encode('utf-8')
                    st.download_button("Download Anomalies CSV", csv_anomalies, "anomalies.csv", "text/csv")
                else:
                    st.success("No anomalies detected in the selected column.")

                
                st.markdown("### Z-Score Preview (Debug Only)")
                z_debug = df[[value_col]].copy()
                z_debug["z_score"] = (z_debug[value_col] - z_debug[value_col].mean()) / z_debug[value_col].std()
                st.dataframe(z_debug)
