import pandas                                                                                   # Import for dataframe creation
import seaborn                                                                                  # Import for visualization
import matplotlib.pyplot as plt

TPs, TNs, FNs, FPs = [[] for i in range(0, 4)]                                                  # Creating arrays to make confusion matrix

# FUNCTION THAT MAKES THE CONFUSION MATRICES

# Uses Seaborn and MatPlotLib to make and save confusion matrices
def visualize(TPs,TNs,FNs,FPs):
    for epoch in range(0,5):                                                                    # For each epoch make a confusion matrix
        seaborn.set(color_codes=True)                                                           # Setting colors for the matrix
        plt.figure(1, figsize=(9, 6))                                                           # Setting size, title and font size

        plt.title("Confusion Matrix")

        seaborn.set(font_scale=1.4)
        ax = seaborn.heatmap([[TPs[epoch],FPs[epoch]],[FNs[epoch],TNs[epoch]]], annot=True,     # Specifics of the heatmap
                             cmap="Blues", cbar_kws={'label': 'Scale'}, fmt='.6g')

        ax.set_xticklabels(["Positive","Negative"])                                             # Setting tick labels
        ax.set_yticklabels(["Negative","Positive"])

        ax.set(ylabel="Predicted Class", xlabel="True Class")                                   # Setting axis values

        plt.savefig("metric_viz_files\\PreHPT\\confusion_matrix_epoch" + str(epoch)+".png",                   # Saving figure with name and directory
                    bbox_inches='tight', dpi=300)
        plt.close()

def main():
    metrics = pandas.read_csv("metrics_file_PHPT.txt", header=None)                                   # Importing file made in ModelPHPT.py
    TPs = metrics.iloc[5].values                                                                # Getting the values we need
    TNs = metrics.iloc[6].values
    FNs = metrics.iloc[7].values
    FPs = metrics.iloc[8].values

    visualize(TPs,TNs,FNs,FPs)                                                                  # Calling function to make confusion matrices

if __name__ == "__main__":
    main()
