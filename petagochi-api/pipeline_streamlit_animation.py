import streamlit as st
import time
import random

st.set_page_config(layout="wide")
st.title("📊 Petagotchi MLOps Pipeline Simulation")

steps = [
    "1️⃣ Data Ingestion via Airflow → S3",
    "2️⃣ Data Validation & Preprocessing",
    "3️⃣ Model Training on SageMaker",
    "4️⃣ MLflow Tracking & Artifact Storage",
    "5️⃣ Model Evaluation & Comparison",
    "6️⃣ Model Registration",
    "7️⃣ Model Deployment (Champion/Challenger)",
    "8️⃣ Real-time Inference Endpoint",
]

status = {
    "1️⃣ Data Ingestion via Airflow → S3": "✅ Data loaded to `s3://petagotchi-bucket/data/train.csv`",
    "2️⃣ Data Validation & Preprocessing": "✅ Cleaned missing values, encoded actions/states",
    "3️⃣ Model Training on SageMaker": "✅ RandomForestClassifier trained (accuracy: 91%)",
    "4️⃣ MLflow Tracking & Artifact Storage": "✅ Model + metrics logged to `mlruns/123/model.pkl`",
    "5️⃣ Model Evaluation & Comparison": "✅ New model better than previous (↑3% F1)",
    "6️⃣ Model Registration": "✅ Registered as `petagotchi:staging`",
    "7️⃣ Model Deployment (Champion/Challenger)": "✅ Deployed via SageMaker endpoint: `petagotchi-endpoint`",
    "8️⃣ Real-time Inference Endpoint": "📦 Predicted state: `['happy', 'hungry']` for action: `feed`"
}

col1, col2 = st.columns(2)

with col1:
    for step in steps[:4]:
        st.subheader(f"🔁 {step}")
        with st.expander("Details", expanded=True):
            st.success(status[step])
        time.sleep(0.5)

with col2:
    for step in steps[4:]:
        st.subheader(f"🔁 {step}")
        with st.expander("Details", expanded=True):
            if "happy" in status[step]:
                st.info(status[step])
            else:
                st.success(status[step])
        time.sleep(0.5)

st.markdown("---")
st.caption("📍 Powered by Streamlit, SageMaker, MLflow, Airflow, S3")


