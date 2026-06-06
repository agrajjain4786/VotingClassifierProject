# 🛡️ Voting Classifier Project — Malware & Bot Detection

A full-stack **Machine Learning web application** that uses an ensemble **Voting Classifier** to detect malware and bots from CSV datasets. Upload your data, get instant predictions, model accuracy, and a detailed classification report — all from the browser.

---

## 🧠 What is a Voting Classifier?

A **Voting Classifier** is an ensemble learning technique that combines multiple ML models and uses their combined predictions (majority vote) to produce a more accurate and robust final result. This project applies that technique to **cybersecurity threat detection** — identifying malware samples and bot activity from feature-rich datasets.

---

## ✨ Features

- 📂 **CSV Upload** — Upload any compatible dataset directly from the browser
- 🤖 **Ensemble ML Model** — Voting Classifier combining multiple base estimators for higher accuracy
- 📊 **Accuracy Score** — Instantly see how well the model performs on your data
- 📋 **Classification Report** — Precision, recall, F1-score breakdown per class
- 🦠 **Malware Detection** — Trained on real malware feature datasets (`MalwareData_1/2/3.csv`)
- 🤖 **Bot Detection** — Also supports bot activity classification (`bot_detection_data.csv`)
- 🌐 **Browser-based UI** — No installation needed on the frontend side

---

## 🗂️ Project Structure

```
VotingClassifierProject/
├── backend/
│   ├── app.py              # Flask API server with ML logic
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Main UI — upload CSV & view results
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic & API calls
├── MalwareData_1.csv       # Malware dataset (part 1)
├── MalwareData_2.csv       # Malware dataset (part 2)
├── MalwareData_3.csv       # Malware dataset (part 3)
├── bot_detection_data.csv  # Bot detection dataset
└── README.txt              # Basic run instructions
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **ML Library** | scikit-learn (VotingClassifier) |
| **Data Processing** | pandas, NumPy |
| **Frontend** | HTML, CSS, JavaScript |
| **API** | REST (Flask endpoints) |

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation & Running

```bash
# 1. Clone the repository
git clone https://github.com/agrajjain4786/VotingClassifierProject.git
cd VotingClassifierProject

# 2. Navigate to the backend
cd backend

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Start the Flask server
python app.py
```

The Flask server will start at `http://localhost:5000`.

### Open the Frontend

Open `frontend/index.html` directly in your browser (no extra setup needed).

---

## 🚀 How to Use

1. Start the Flask backend (`python app.py`)
2. Open `frontend/index.html` in your browser
3. Upload one of the CSV files (e.g., `MalwareData_1.csv` or `bot_detection_data.csv`)
4. Click **Predict / Analyze**
5. View the **accuracy score** and **classification report** on screen

---

## 📊 Datasets

| File | Description |
|---|---|
| `MalwareData_1.csv` | Malware features dataset — part 1 |
| `MalwareData_2.csv` | Malware features dataset — part 2 |
| `MalwareData_3.csv` | Malware features dataset — part 3 |
| `bot_detection_data.csv` | Network/user behaviour data for bot detection |

---

## 🤝 Contributing

Contributions and improvements are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-idea`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Agraj Jain** — AI Engineer | Generative AI | RAG Systems | Agentic AI

- 🌐 Website: [agraj.unaux.com](https://agraj.unaux.com/)
- 💼 LinkedIn: [agraj-jain-a784a427a](https://www.linkedin.com/in/agraj-jain-a784a427a/)
- 🐙 GitHub: [@agrajjain4786](https://github.com/agrajjain4786)

---

## 📄 License

This project is open source and free to use for educational and research purposes.

---

> *"Ensemble learning — where many models think together better than one."* 🤝🧠
