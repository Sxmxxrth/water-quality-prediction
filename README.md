# Water Quality Prediction

A machine learning application that predicts whether water is safe to drink based on various water quality parameters.

## Features

- 🎯 Predicts water safety using a trained ML model
- 💧 Analyzes 9 water quality parameters:
  - pH
  - Hardness
  - Solids
  - Chloramines
  - Sulfate
  - Conductivity
  - Organic Carbon
  - Trihalomethanes
  - Turbidity

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd water
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run water_project/app.py
```

Then open your browser to `http://localhost:8501` and enter water parameters to get a prediction.

## Project Structure

```
water/
├── Water_Quality_Prediction_.ipynb  # Model training notebook
├── water_project/
│   ├── app.py                       # Streamlit application
│   ├── model.pkl                    # Trained ML model
│   └── scaler.pkl                   # Feature scaler
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## Model Details

- **Training Data**: Water quality dataset with 3276 samples
- **Algorithm**: Classification model
- **Output**: Binary prediction (Safe / Not Safe to Drink)

## Technologies Used

- **Streamlit** - Web application framework
- **Scikit-learn** - Machine learning
- **NumPy/Pandas** - Data processing

## License

This project is open source and available under the MIT License.
