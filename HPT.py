import keras.metrics                                                                            # Import for all the metrics for model performance
import pandas                                                                                   # Import for dataframe creation
from keras.models import Sequential                                                             # Import for model creation
from keras.layers import Dense                                                                  # Import for layer addition
from sklearn.model_selection import KFold                                                       # Import to do kFold cross validation
import keras_tuner as kt                                                                        # HPT libraries
import tensorflow as tf


def make_model(hp):
    model = Sequential()                                                                        # We want a sequence of layers
    model.add(Dense(16, input_dim=16, activation='relu'))                                       # Creating input layer with n_ins(16 nodes)


    # Tuning number of hidden layers
    for i in range(1, hp.Int("num_layers", 1, 6,step=1)):
        # Tuning number of nodes in the hidden layer
        model.add(Dense(units= hp.Int("units_" + str(i), min_value=8, max_value=30, step=2), activation='relu'))

    model.add(Dense(7, activation='softmax'))                                              # Creating output layer with n_outs(7 nodes)

    model.compile(loss="categorical_crossentropy", optimizer="adam",
                  metrics=["accuracy", "mean_squared_error", keras.metrics.Precision(), keras.metrics.Recall()
                      , keras.metrics.TruePositives()
                      , keras.metrics.TrueNegatives(), keras.metrics.FalseNegatives()           # Compiling with specified charactertics
                      , keras.metrics.FalsePositives()])                                        # and returning specified metrics

    return model  # returning model

def main():
    # Reading the dataset and seperating them into x and y data
    obesity_df = pandas.read_csv("data_processing\\Processed_data.csv")  # Reading preprocessed data
    obesity_x = obesity_df.iloc[:, 0:16]  # Selecting input columns
    obesity_y = obesity_df.iloc[:, 16:]  # Selecting output column
    obesity_y_encoded = pandas.get_dummies(obesity_y, columns=["NObeyesdad"])  # One hot encoding the output column

    # Creating the search space
    tuner = kt.RandomSearch(make_model,
                         objective='val_accuracy',
                         max_trials=15,
                         directory='my_dir2',
                         project_name='intro_to_kt')

    # Stop condition
    stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=50)

    # Searching
    tuner.search(obesity_x, obesity_y_encoded, epochs=50, validation_split=0.2, callbacks=[stop_early],verbose=2)
    # Retrieving best params
    best_hps=tuner.get_best_hyperparameters()[0].values
    print(best_hps)

if __name__ == "__main__":
    main()