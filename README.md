---

# 🐾 Petagotchi — UCU MLOps Project (brief)

> An interactive, ML-powered virtual pet (yes, like Tamagotchi) that learns from how you treat it.
> **Status**: 🚧 In Progress
> **Timeline**: May 2, 2025 – July 12, 2025
> **Owner**: Andrii Hupalo

---

## 🧠 Overview

The goal of this project is to build **Petagotchi**, a virtual pet that adapts to user interactions such as feeding, playing, or sleeping. Unlike traditional digital pets, Petagotchi uses machine learning to **personalize** its behavior over time. The project is built on **Google Cloud Platform (GCP)** to support data handling, model deployment, and scaling.

(Why not AWS? Unexpected charges can sneak up fast. GCP feels safer for MVPs.)

---

## 💡 Motivation

Most virtual pets follow predefined rules and don't evolve. Petagotchi introduces machine learning into the mix — think *Pokegotchi* — making the pet's behavior dynamic, reactive, and unique to each user. GCP offers the managed services needed to make this scalable, cost-effective, and fast to prototype.

---

## 📈 Success Metrics

* **User Engagement**: Track session time and interaction frequency.
* **Model Accuracy**: Evaluate how well the pet’s reactions align with user expectations.
* **Pet Satisfaction Score**: Computed from health, mood, and other status indicators after each interaction.

---

## ✅ Requirements & Constraints

### Functional Requirements

* The pet reacts dynamically to user interactions (feed, play, sleep).
* Behavior should improve over time through learned patterns.

### Non-Functional Requirements

* **Performance**: Response time < 1s for smooth UX.
* **Scalability**: Handle concurrent users with no downtime.
* **Cost-Efficiency**: Stay within GCP’s free tier (as much as possible).

### Constraints

* **Scope**: Single pet, basic interactions. No multi-pet ecosystems (yet).
* **Privacy**: No sensitive data collected — only interaction-based data.

---

## 📦 In-Scope vs Out-of-Scope

### ✅ In-Scope

* Machine learning model (reinforcement learning or classification).
* Core interactions: feeding, playing, sleeping.
* Pet state tracking: hunger, mood, energy.

### 🚫 Out-of-Scope (for MVP)

* Advanced user environments or multi-pet features.
* High-end graphics or 3D rendering (but maybe in later phases).

---

## 🧪 Methodology

### 🔍 Problem Statement

Design an ML model that predicts and adapts pet behavior based on user inputs. E.g., feed it → happy pet; ignore it → sad pet.

### 📊 Data

* **Interaction Data**: User actions (feed/play/sleep).
* **Pet State Data**: Mood, hunger, energy, health, etc.

### 🛠 Techniques

* **Reinforcement Learning** to optimize pet behavior.
* **Data Preprocessing**: Clean, normalize features (e.g., mood 0–100 scale).

### ✅ Validation

* **Offline Testing**: Validate on historical interaction sequences.
* **Metrics**: Model accuracy, interaction prediction error, happiness score.

### 🔁 Human-in-the-Loop

* Let users give feedback (e.g., "Pet too sad") to improve personalization.

---

## ⚙️ Implementation

### 🔧 High-Level Design

* **UI**: Web-based interface for interacting with the pet.
* **ML Model**: Predicts pet responses based on recent interactions.
* **Backend**: Real-time serverless API (hosted on GCP).

### 🏗 Infrastructure (GCP)

* **Cloud Storage (GCS)**: Store user-pet interaction data.
* **Cloud Functions**: Handle API requests + inference calls.
* **AI Platform**: Host and manage ML models (e.g., TensorFlow).
* **BigQuery/PostgreSQL**: Optional, for growing datasets.

### 🚀 Performance

* **Latency**: <1s interaction turnaround.
* **Scalability**: GCP auto-scaling for concurrent users.

### 🔐 Security & Privacy

* **Authentication**: Firebase Auth for login and identity.
* **Data Encryption**: At-rest and in-transit.
* **Retention**: Only store data as long as needed.

### 🛡 Monitoring

* **Logging**: GCP Cloud Logging for API health.
* **Alerts**: Cloud Monitoring for errors, latency spikes, etc.

### 💰 Cost Estimates

Low-cost by design, leveraging:

* GCP’s free tier (Cloud Functions, Storage).
* Minimal inference workload during MVP.

### ⚠ Risks

* **Overfitting**: Pet may become too tailored to single users.
* **User Inactivity**: Not enough interactions to train the model effectively.

---

## 🔁 Alternatives

* **Non-ML Rule-Based Logic**: Simpler to implement but less engaging or adaptive.
* **Alternative Platforms**: AWS or Azure were considered but GCP was chosen for cost control and ML tools.

---

## 📎 Appendix

> This project is part of the **UCU MLOps** course final deliverable.
> Feel free to fork, comment, or contribute.

---
