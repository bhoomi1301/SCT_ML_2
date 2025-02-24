from flask import Flask, request, render_template, send_file
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route for home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            
            # Process data and cluster it
            clustered_data = process_and_cluster(filepath)
            
            # Save clustered data
            output_file = "static/Clustered_Customers.csv"
            clustered_data.to_csv(output_file, index=False)
            
            # Generate and save visualizations
            plot_clusters(clustered_data)
            
            return render_template("result.html", filename=file.filename)

    return render_template("index.html")

# Function to process and apply K-Means clustering
def process_and_cluster(filepath):
    df = pd.read_csv(filepath)

    # Select relevant features
    X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

    # Standardize data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply K-Means
    kmeans = KMeans(n_clusters=5, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X_scaled)

    # Label clusters
    cluster_labels = {
        0: "Low Income, Low Spending",
        1: "Low Income, High Spending",
        2: "Middle Income, Moderate Spending",
        3: "High Income, Low Spending",
        4: "High Income, High Spending"
    }
    df["Cluster Label"] = df["Cluster"].map(cluster_labels)

    return df

# Function to generate and save visualizations
def plot_clusters(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=df["Cluster Label"].value_counts().index, 
                y=df["Cluster Label"].value_counts().values, palette="viridis")
    plt.xticks(rotation=45)
    plt.title("Customer Segments Distribution")
    plt.savefig("static/bar_chart.png")
    
    plt.figure(figsize=(7, 7))
    plt.pie(df["Cluster Label"].value_counts().values, 
            labels=df["Cluster Label"].value_counts().index, autopct='%1.1f%%', colors=sns.color_palette("viridis", 5))
    plt.title("Customer Segments Proportion")
    plt.savefig("static/pie_chart.png")

# Route to download clustered CSV file
@app.route("/download")
def download():
    return send_file("static/Clustered_Customers.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
