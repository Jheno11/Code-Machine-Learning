# Libraries Import
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, GridSearchCV
from imblearn.over_sampling import RandomOverSampler, BorderlineSMOTE
from imblearn.combine import SMOTEENN
from imblearn.over_sampling import KMeansSMOTE
from sklearn.metrics import accuracy_score, classification_report

# Balancing methods
before_splitting_methods = {
    'No Balancing': None,
    'RandomOverSampler': RandomOverSampler(random_state=42, sampling_strategy=0.35),
    'SMOTEENN': SMOTEENN(random_state=42, sampling_strategy=0.32),
    'KMeansSMOTE': KMeansSMOTE(random_state=42, sampling_strategy=0.35),
    'BorderlineSMOTE': BorderlineSMOTE(random_state=42, sampling_strategy=0.33)
}

# DataFrame to store results
results_df = pd.DataFrame(columns=['Jumlah Gene', 'Split_Ratio', 'Initial_No_of_cancer', 
                                   'Initial_No_of_normal', 'Before_Splitting', 'No. of cancer in Train', 'No. of normal in Train', 
                                   'No. of cancer in Test', 'No. of normal in Test','Hyperparameter', 'Test_Accuracy', 'Train_Classification_Report', 'Classification_Report'])

# Loop through each dataset
datasets = ['4', '7', '13', '139']
hyper = ['yes', 'no']
split_ratios = [(0.8, 0.2), (0.7, 0.3), (0.6, 0.4)]

# Train Naive Bayes model with GridSearchCV
param_grid = {
    'var_smoothing': np.logspace(0, -9, num=100)
}

for param in hyper:
    for dataset in datasets:
        # Read each dataset
        data_path = f"C:/UMN/JP/penelitian/Final/DataBlack{dataset}.csv"
        data = pd.read_csv(data_path)
        print("Reading dataset:", data_path)

        # Get features
        features_df = data.iloc[:, 1:]

        # Process data
        data = data.set_index("Ensembl_ID")
        data = data.round().astype(int)
        data = data.T

        # Label the samples
        data['label'] = ['cancer' if '-01' in sample else 'normal' for sample in data.index]

        features_df = features_df.round().astype(int).T
        X = np.asarray(features_df)
        y = np.asarray(data['label'])

        print(f"\nProcessing Dataset: {dataset}")
        print("Original Class Distribution:")
        print(data['label'].value_counts())

        # Store initial data distribution
        initial_cancer_count = sum(data['label'] == 'cancer')
        initial_normal_count = sum(data['label'] == 'normal')

        for train_size, test_size in split_ratios:
            # Split the dataset according to the current ratio
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

            # Loop through all balancing methods for after-split balancing
            for Before_Splitting_name, Before_Splitting in before_splitting_methods.items():
                if Before_Splitting is None:
                    X_resampled, y_resampled = X_train, y_train
                else:
                    # Apply balancing method to the training dataset
                    X_resampled, y_resampled = Before_Splitting.fit_resample(X_train, y_train)
                
                label_encoder = LabelEncoder()
                y_train_encoded = label_encoder.fit_transform(y_resampled)
                y_test_encoded = label_encoder.transform(y_test)

                # Initialize GridSearchCV with GaussianNB and the parameter grid
                grid_search = GridSearchCV(GaussianNB(), param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=0, return_train_score=True)
                grid_search.fit(X_resampled, y_train_encoded)
                best_nb = grid_search.best_estimator_

                y_pred_test = best_nb.predict(X_test)
                y_pred_train = best_nb.predict(X_resampled)

                # Calculate test accuracy
                test_accuracy = accuracy_score(y_test_encoded, y_pred_test)

                # Print results
                print(f"\nDataset: {dataset} | Before: {Before_Splitting_name} | Split Ratio: {train_size}/{test_size}")
                classification_report_str = classification_report(y_test_encoded, y_pred_test, target_names=label_encoder.classes_)
                train_classification_report_str = classification_report(y_train_encoded, y_pred_train, target_names=label_encoder.classes_)
                print("Classification Report:\n", classification_report_str)

                new_row = pd.DataFrame({
                    'Jumlah Gene': [dataset],
                    'Split_Ratio': [f"{train_size}/{test_size}"],
                    'Initial_No_of_cancer': [initial_cancer_count],
                    'Initial_No_of_normal': [initial_normal_count],
                    'Before_Splitting': [Before_Splitting_name],
                    'No. of cancer in Train': [sum(y_train_encoded == 0)],
                    'No. of normal in Train': [sum(y_train_encoded == 1)],
                    'No. of cancer in Test': [sum(y_test_encoded == 0)],
                    'No. of normal in Test': [sum(y_test_encoded == 1)],
                    'Hyperparameter': [param],
                    'Test_Accuracy': [test_accuracy],
                    'Train_Classification_Report': [train_classification_report_str],
                    'Classification_Report': [classification_report_str]
                })

                results_df = pd.concat([results_df, new_row], ignore_index=True)

# Sort results by Test_Accuracy in descending order
results_df = results_df.sort_values(by='Test_Accuracy', ascending=False)

# Save the results to a CSV file
results_df.to_csv('C:/UMN/JP/penelitian/Final/NB_ALL_801010_RESULTSblack.csv', index=False)
print("Results saved to 'NB_ALL_801010_RESULTSblack.csv'")
