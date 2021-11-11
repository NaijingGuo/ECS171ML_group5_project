import keras.metrics                                                                            # Import for all the metrics for model performance
import pandas                                                                                   # Import for dataframe creation
from keras.models import Sequential                                                             # Import for model creation
from keras.layers import Dense                                                                  # Import for layer addition
from sklearn.model_selection import KFold                                                       # Import to do kFold cross validation

loss,accuracy,mse,Precision,Recall,TPs,TNs,FNs,FPs= [[] for i in range(0,9)]                    # Creating global variables to store model metrics


# FUNCTION THAT CONVERTS METRICS TO a text file to pass onto the visualization function

# Uses pandas library to convert the arrays that were made into a dataframe into a csv file
def metricsToFile():
    data = [loss, accuracy, mse, Precision, Recall, TPs, TNs, FNs, FPs]
    df = pandas.DataFrame(data)
    df.to_csv("metrics_file_PHPT.txt",index=False,header = False)

# FUNCTION THAT DEFINES MODEL STRUCTURE :

# Creates the model as follows:
# 16 attributes ->     [20 neurons]     ->     [20 neurons]     ->     [15 neurons]      ->    7 outputs
# [ Input Layer  ->    Hidden Layer 1          Hidden Layer 2          Hidden Layer 3          Output Layer]

# Compiles and returns the model with the following characteristics:
# -> Loss - Categorical Cross Entropy
# -> Optimizer - adam (better stochastic gradient descent)

# During compilation, the instruction to return the following metrics are given:
# -> Accuracy
# -> Mean Squared Error
# -> Precision
# -> Recall
# -> True Positives
# -> True Negatives
# -> False Negatives
# -> False Positives
def make_model(n_ins, n_outs, hl1, hl2, hl3):
    model = Sequential()                                                                        # We want a sequence of layers
    model.add(Dense(n_ins, input_dim=n_ins, activation='relu'))                                 # Creating input layer with n_ins(16 nodes)
    model.add(Dense(hl1, activation='relu'))                                                    # Creating hidden layer 1 with hl1(20 nodes)
    model.add(Dense(hl2, activation='relu'))                                                    # Creating hidden layer 2 with hl2(20 nodes)
    model.add(Dense(hl3, activation='relu'))                                                    # Creating hidden layer 3 with hl3(15 nodes)
    model.add(Dense(n_outs, activation='softmax'))                                              # Creating output layer with n_outs(7 nodes)

    model.compile(loss="categorical_crossentropy", optimizer="adam",
                  metrics=["accuracy", "mean_squared_error", keras.metrics.Precision(), keras.metrics.Recall()
                      , keras.metrics.TruePositives()
                      , keras.metrics.TrueNegatives(), keras.metrics.FalseNegatives()           # Compiling with specified charactertics
                      , keras.metrics.FalsePositives()])                                        # and returning specified metrics

    return model  # returning model

# FUNCTION THAT EVALUATES EVERYTHING

# Does KFold and then fits,tests and returns the model making the metrics and storing them in an array of values
def return_model(obesity_x,obesity_y_encoded):
    n_split = 5  # Number of splits for Kfold cross validation
    # LOOP THAT IMPLEMENTS KFOLD CROSS VALIDATION

    # sklearn.model_selection.KFold generates indices that we can use for the folds
    # Those indices are used to select the rows for the train and test respectively
    # These rows are appended to new train and test dataframes that are made for each fold
    # The returned metrics are then stored in each of their respective arrays so we can use them for metrics and presentation
    fold_no = 1
    for train_index, test_index in KFold(n_split).split(obesity_x):
        X_train = pandas.DataFrame()                                                            # Creating X train dataframe
        Y_train = pandas.DataFrame()                                                            # Creating Y train dataframe
        X_test = pandas.DataFrame()                                                             # Creating X test dataframe
        Y_test = pandas.DataFrame()                                                             # Creating Y test dataframe

        for i in train_index:
            X_train = pandas.concat([X_train, obesity_x.iloc[[i]]])                             # Appending X_train values
            Y_train = pandas.concat([Y_train, obesity_y_encoded.iloc[[i]]])                     # Appending Y_train values

        for i in test_index:
            X_test = pandas.concat([X_test, obesity_x.iloc[[i]]])                               # Appending X_test values
            Y_test = pandas.concat([Y_test, obesity_y_encoded.iloc[[i]]])                       # Appending Y_test values

        model = make_model(X_train.shape[1], Y_train.shape[1], 20, 20,15)                       # Making a model while passing input and output dims
                                                                                                # and hidden layer sizes
        print("Training Model")
        model.fit(X_train, Y_train, epochs=500, verbose=0)                                      # Fitting model per KFold

        metrics = model.evaluate(X_test, Y_test,verbose=1)                                      # Fitting model with the dataframes and 500 epochs

        loss.append(metrics[0])                                                                 # Storing metrics in global variables
        accuracy.append(metrics[1])
        mse.append(metrics[2])
        Precision.append(metrics[3])
        Recall.append(metrics[4])
        TPs.append(metrics[5])
        TNs.append(metrics[6])
        FNs.append(metrics[7])
        FPs.append(metrics[8])

    return model                                                                                # return model

def main():
    # Reading the dataset and seperating them into x and y data
    obesity_df = pandas.read_csv("data_processing\\Processed_data.csv")                                        # Reading preprocessed data
    obesity_x = obesity_df.iloc[:,0:16]                                                         # Selecting input columns
    obesity_y = obesity_df.iloc[:,16:]                                                          # Selecting output column
    obesity_y_encoded = pandas.get_dummies(obesity_y, columns=["NObeyesdad"])                   # One hot encoding the output column

    trained_model = return_model(obesity_x,obesity_y_encoded)                                   # Receiving the trained model
    metricsToFile()                                                                             # Converting the metrics to a file
    trained_model.save('PHPTtrainedmodel.h5')                                                     # Saving trained file for hyperparameter Tuning and backend deployment

if __name__ == "__main__":
    main()