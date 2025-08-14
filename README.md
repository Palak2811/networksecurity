### Network Security Projects For Phising Data
using ETL(extract,transform,load) pipeline:-
extract =extracting the data from the source(csv file,comming from apis,etc)
transform=tranforming the dataset by doing basic preprocessing like cleaning raw data and converting into json
load=loading the jason file to destination(mongodb,sql,etc)


This project is a Machine Learning application for **Network Security / Phishing Detection**.  
It uses a **FastAPI** backend, integrates with **MongoDB** for data storage, and includes a complete **ML training pipeline** (data ingestion → transformation → model training → prediction).  

---

## 🚀 Features
- **Data Ingestion** from CSV or MongoDB.
- **Data Transformation** for ML-ready formats.
- **Model Training** using `scikit-learn`.
- **Prediction API** using FastAPI + Uvicorn.
- **MLflow** integration for experiment tracking.
- **DagsHub** support for remote logging.
- **Modular Codebase** with clear folder structure.

---

## 📂 Project Structure
.
├── Artifacts/ # Stores generated artifacts (data, models, logs)
├── Network_Data/ # Raw datasets
├── networksecurity/ # Core Python package
│ ├── components/ # Data ingestion, transformation, validation, training
│ ├── constants/ # Constant values (paths, configs)
│ ├── entity/ # Entity classes for configs/artifacts
│ ├── exception/ # Custom exceptions
│ ├── logging/ # Logging setup
│ ├── pipeline/ # Training & prediction pipelines
│ └── utils/ # Utility functions
├── notebooks/ # Jupyter notebooks for exploration
├── prediction_output/ # Model prediction outputs
├── templates/ # HTML templates for API frontend
├── app.py # FastAPI app entry point
├── main.py # Main script
├── .env # Environment variables (MongoDB URI, secrets)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/network-security-ml.git
cd network-security-ml
2️⃣ Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
⚙ Environment Variables
Create a .env file in the root directory with:

env
Copy
Edit
mongo_db_url = "your_mongodb_connection_string"
DATA_INGESTION_DATABASE_NAME = "your_database"
DATA_INGESTION_COLLECTION_NAME = "your_collection"
▶ Running the Application
Start the FastAPI app using Uvicorn:

bash
Copy
Edit
uvicorn app:app --reload
API will be available at:
🔗 http://127.0.0.1:8000

📡 API Endpoints
Method	Endpoint	Description
GET	/	Home / Welcome Page
POST	/predict	Predict from input data
GET	/docs	Swagger UI for API testing
GET	/redoc	ReDoc API documentation

📦 Dependencies
css
Copy
Edit
python-dotenv
pandas
numpy
pymongo
certifi
pymongo[srv]
scikit-learn
mlflow
pyaml
dagshub
fastapi
uvicorn
python-multipart
Install them via:

bash
Copy
Edit
pip install -r requirements.txt
 ML Pipeline
Data Ingestion → Load from MongoDB / CSV.

Data Transformation → Feature engineering, scaling.

Model Training → Train and evaluate ML models.

Model Storage → Save model artifacts for prediction.

Prediction API → Serve predictions via FastAPI.

🖥 Example Usage
Request:
json
Copy
Edit
POST /predict
{
    "feature1": 0.45,
    "feature2": 1.23,
    "feature3": 0.67
}
Response:
json
Copy
Edit
{
    "prediction": "Safe"
}
📌 Notes
Make sure MongoDB is running or your Atlas connection string is correct.

MLflow will track your experiments locally or remotely.

Modify constants in networksecurity/constants/training_pipeline.py as needed.

🏗 Future Improvements
Add authentication for API.

Integrate with Docker for deployment.

Implement CI/CD pipeline.

Enhance feature engineering.


