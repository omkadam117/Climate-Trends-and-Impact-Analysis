import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

# Preprocess the data
def preprocess_data(data):
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Set 'Date' column as the index
    data.set_index('Date', inplace=True)
    
    # Resample data to yearly averages
    data_yearly = data.resample('Y').mean()
    
    return data_yearly

# Plot the data
def plot_data(data_yearly):
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=data_yearly, x=data_yearly.index, y='Temperature', marker='o')
    plt.title('Annual Average Temperature Trend')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig('temperature_trends.png')
    plt.show()

def main():
    # File path to the CSV file
    filepath = 'data/temperature_data.csv'
    
    # Load and preprocess the data
    data = load_data(filepath)
    data_yearly = preprocess_data(data)
    
    # Plot the data
    plot_data(data_yearly)

if __name__ == "__main__":
    main()
