# **Customer Segmentation using K-Means Clustering**

This project implements customer segmentation using the K-Means clustering algorithm on retail store customer data. The Flask web application allows users to upload a dataset, perform clustering, and visualize the results.

📌 Features

Upload customer purchase data (CSV format)

Preprocess and normalize data

Apply K-Means clustering to segment customers

Generate visualizations (bar charts, pie charts)

Download clustered customer data as CSV

🚀 Technologies Used

Python (Flask, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)

Machine Learning (K-Means Clustering, StandardScaler)

Flask (Web Framework)

HTML, CSS (Frontend Design)

📂 Project Structure

/Customer-Segmentation
│── app.py                # Flask application
│── kmeans.pkl            # Saved K-Means model
│── /templates            # HTML templates
│   │── index.html        # File upload page
│   │── result.html       # Results page
│── /static               # Static files (CSS, Images, CSV)
│   │── styles.css        # Stylesheet
│   │── bar_chart.png     # Cluster visualization
│   │── pie_chart.png     # Cluster distribution
│── /uploads              # Folder for uploaded files
│── /output               # Folder for processed CSV files
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation

📥 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation

2️⃣ Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Run the Flask Application

python app.py

App will run on: http://127.0.0.1:5000/

🎯 How It Works

Upload the customer dataset (CSV file).

Preprocessing: Standardizes numerical features (Annual Income & Spending Score).

K-Means Clustering: Segments customers into 5 groups.

Visualization: Displays pie chart and bar chart of clusters.

Download: Processed dataset with cluster labels.

🖼️ Screenshots

🔹 File Upload Page



🔹 Clustered Data Visualization



📌 API Endpoints

Endpoint

Method

Description

/

GET, POST

Upload CSV & display results

/download

GET

Download clustered data CSV

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Developed by Bhoomika N.S 🚀

📩 Connect with me on [LinkedIn](https://www.linkedin.com/in/bhoomikans/)
