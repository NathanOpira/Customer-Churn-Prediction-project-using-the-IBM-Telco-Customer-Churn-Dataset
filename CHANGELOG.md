# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-12-05

### Added
- Initial project release
- Customer churn prediction analysis using Logistic Regression and Deep Neural Networks
- Data preprocessing pipeline with SMOTE for class imbalance handling
- Feature selection using Mutual Information
- Hyperparameter tuning with GridSearchCV
- Comprehensive model evaluation metrics (Accuracy, Precision, Recall, F1, ROC-AUC)
- Comparative analysis between LR and DNN models
- Complete documentation and setup instructions
- Requirements.txt for easy dependency installation
- MIT License
- Contributing guidelines

### Features
- **Data Preprocessing**: Target encoding, missing value imputation, one-hot encoding, min-max scaling
- **Class Imbalance Handling**: SMOTE on training data only
- **Feature Selection**: Top 10 features via Mutual Information
- **Model 1**: Logistic Regression with hyperparameter optimization
- **Model 2**: Deep Neural Network with early stopping
- **Evaluation**: Multi-metric assessment on holdout test set

### Changed
- Renamed notebook from `b30308.ipynb` to `Customer_Churn_Prediction.ipynb`
- Added comprehensive README documentation
- Created professional repository structure

### Fixed
- Resolved TensorFlow compatibility issues with Python 3.11.9
- Fixed data type conversion for neural network training
- Added missing module installations

## [Unreleased]

### Planned Features
- Visualization dashboards for model comparison
- ROC curves and confusion matrix plots
- Feature importance visualizations
- Ensemble methods implementation
- Model explainability analysis
- Automated testing suite
- CI/CD pipeline integration

---

## How to Update This File

When making contributions, update this changelog with:
- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Now removed features
- **Fixed**: Bug fixes
- **Security**: Security-related fixes
