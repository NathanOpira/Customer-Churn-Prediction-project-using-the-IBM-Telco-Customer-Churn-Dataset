# Customer Churn Prediction using IBM Telco Dataset

## Overview
This project implements machine learning models to predict customer churn using the IBM Telco Customer Churn dataset. The analysis compares Logistic Regression and Deep Neural Network approaches to identify customers at risk of leaving.

## Dataset
- **Source**: IBM Telco Customer Churn Dataset
- **File**: `WA_Fn-UseC_-Telco-Customer-Churn.csv`
- **Records**: 7,043 customers with 21 attributes
- **Target Variable**: Churn (Yes/No)

## Project Structure
```
.
├── Customer_Churn_Prediction.ipynb    # Main analysis notebook
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset
├── requirements.txt                    # Python dependencies
├── README.md                          # This file
└── LICENSE                            # Project license
```

## Methodology

### 1. Data Preprocessing
- **Target Encoding**: Mapped 'Churn' to binary (1/0)
- **Missing Value Handling**: Imputed empty TotalCharges with median
- **Feature Engineering**: One-hot encoding for categorical variables
- **Data Scaling**: Min-Max scaling for numeric features

### 2. Class Imbalance Handling
- Applied **SMOTE (Synthetic Minority Oversampling Technique)** on training data only
- Maintained original distribution in test set for unbiased evaluation

### 3. Feature Selection
- Used **Mutual Information** classification to identify top 10 most informative features
- Features selected for Logistic Regression model

### 4. Model Development

#### Logistic Regression
- **Hyperparameter Tuning**: GridSearchCV with 5-fold cross-validation
- **Parameters Tuned**:
  - C: [0.01, 0.1, 1, 10, 100]
  - Penalty: ['l1', 'l2']
- **Scoring Metric**: ROC-AUC
- **Features**: Top 10 mutual information features

#### Deep Neural Network
- **Architecture**:
  - Input Layer: Full feature set
  - Hidden Layer 1: 64 neurons (ReLU activation)
  - Hidden Layer 2: 32 neurons (ReLU activation)
  - Output Layer: 1 neuron (Sigmoid activation)
- **Compilation**: Adam optimizer, binary crossentropy loss
- **Training**: Early stopping with patience=5
- **Epochs**: Up to 100 (with early stopping)

### 5. Model Evaluation
All models evaluated on the holdout test set (30%) using:
- **Accuracy**: Overall correct predictions
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1-Score**: Harmonic mean of Precision and Recall
- **ROC-AUC**: Area under the Receiver Operating Characteristic curve

## Key Results
The comparative evaluation results show:
- **Model Performance Metrics** are displayed in the main notebook
- Confusion matrix analysis for false positives/negatives
- Feature importance insights from mutual information scores

## Installation & Setup

### Prerequisites
- Python 3.11+
- Jupyter Notebook or JupyterLab
- Virtual environment (recommended)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/NathanOpira/Customer-Churn-Prediction-project-using-the-IBM-Telco-Customer-Churn-Dataset.git
   cd Customer-Churn-Prediction-project-using-the-IBM-Telco-Customer-Churn-Dataset
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the notebook:
   ```bash
   jupyter notebook Customer_Churn_Prediction.ipynb
   ```

## Usage
1. Open the Jupyter notebook
2. Run cells sequentially from top to bottom
3. The notebook will:
   - Load and preprocess the dataset
   - Apply SMOTE for class balance
   - Train both Logistic Regression and DNN models
   - Display comparative evaluation metrics
   - Visualize results and insights

## Dependencies
See `requirements.txt` for a complete list of dependencies. Main packages:
- **numpy**: Numerical computations
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning algorithms
- **imbalanced-learn**: SMOTE implementation
- **tensorflow/keras**: Deep learning framework
- **matplotlib/seaborn**: Data visualization

## Results & Insights
The analysis provides:
- Model comparison on key performance metrics
- Identification of top predictive features
- Best hyperparameters for Logistic Regression
- Confusion matrices and classification reports
- ROC-AUC scores for model ranking

## Future Enhancements
- [ ] Add feature importance visualizations
- [ ] Implement cross-validation analysis
- [ ] Add ROC curve and confusion matrix plots
- [ ] Explore ensemble methods (Random Forest, Gradient Boosting)
- [ ] Hyperparameter optimization for DNN architecture
- [ ] Model explainability analysis (SHAP, LIME)

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- **Dataset**: IBM Telco Customer Churn Dataset
- **Tools**: TensorFlow, scikit-learn, pandas, numpy
- **Techniques**: SMOTE, Mutual Information, GridSearchCV

## Contact
For questions or suggestions, please reach out to [your email/GitHub profile].

---
**Last Updated**: December 2025
