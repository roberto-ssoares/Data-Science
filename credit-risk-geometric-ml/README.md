## 🧠 Credit Risk with Graph Ricci Curvature

## 📌 Overview

This project explores a **Geometric Machine Learning approach** to credit risk modeling.

Instead of treating customers as independent observations, we model them as a **graph of similarities**, extracting structural properties using **Ricci curvature**.

---

## 🎯 Objective

Evaluate whether **graph geometry** contains predictive signal for credit default risk.

---

## 🏗️ Methodology

### 1. Data

- Home Credit Default Risk dataset (Kaggle)

### 2. Feature Engineering

- Selection of numerical attributes
- Handling missing values
- Standardization

### 3. Graph Construction

- K-Nearest Neighbors (KNN)
- Nodes: customers
- Edges: similarity relationships

### 4. Geometric Feature Extraction

- Ollivier-Ricci curvature
- Degree (weighted and unweighted)
- Local clustering coefficient
- Curvature statistics (mean, min, max, std)

### 5. Modeling

- Logistic Regression (baseline vs enriched)
- Random Forest (non-linear model)

---

## 📐 Theoretical Background

Ricci curvature in graphs measures the divergence between local neighborhoods.

κ(x, y) = 1 - W₁(mₓ, mᵧ) / d(x, y)

Where:

- W₁: Wasserstein distance
- mₓ, mᵧ: neighborhood distributions

---

## 📊 Key Insights

- Graph structure introduces **relational context**
- Curvature captures **local topology**
- Negative curvature highlights **structural bottlenecks**
- Geometric features can improve model performance

---

## 🧪 Results

| Model                | ROC AUC |
| -------------------- | ------- |
| Baseline             | XX      |
| + Geometric Features | XX      |

---

## 🚀 Future Work

- Graph Neural Networks (GNN)
- Graph rewiring based on curvature
- Multi-table graph integration (bureau, previous applications)
- Temporal graph modeling

---

## 🧠 Key Takeaway

> Customers are not independent. Their position in a relational structure matters.

---

## 📂 Project Structure

data/  
notebooks/  
src/  
reports/

---

## 🛠️ Technologies

- Python
- Pandas / NumPy
- Scikit-learn
- NetworkX
- GraphRicciCurvature

---

## 📎 Author

Roberto Soares  
Data Science & Data Engineering
