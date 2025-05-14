![Banner](static/banner.png)

# Khmer Mood Predictor

A lightweight Flask web application that predicts the emotional tone of Khmer text using a simple AI model. Input a single Khmer sentence (10 words or fewer) to receive a mood prediction: **Happy**, **Sad**, or **Motivational**.

## Features

- Accepts Khmer text input
- Analyzes emotional tone using AI
- Outputs a mood label (**Happy**, **Sad**, or **Motivational**)
- Optimized for single sentences under 10 words

## Tech Stack

- **Python**: Core programming language
- **Flask**: Web framework for the application
- **AI Model**: Custom logic trained on 600+ Khmer sentences
- **HTML/CSS**: Frontend interface

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/phalchanouksa/Khmer-Sentences-Mood-Based-Predictor
   cd Khmer-Sentences-Mood-Based-Predictor
   ```

2. **Install dependencies**:
   Ensure Python 3.8+ is installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```
   The app will start at `http://localhost:5000`.

## How to Use

1. **Access the app**:
   Open your browser and navigate to `http://localhost:5000`.

2. **Enter text**:
   Type a single Khmer sentence (10 words or fewer) into the provided text box.

3. **Submit**:
   Click the "Predict" button to analyze the text.

4. **View results**:
   The predicted mood (**Happy**, **Sad**, or **Motivational**) will display on the page.

**Example**:

- Input: "ខ្ញុំសប្បាយចិត្តណាស់ថ្ងៃនេះ។"
- Output: **Happy**

## Notes

- For best results, use concise sentences.
- The model is trained on a limited dataset (600+ sentences), so accuracy may vary.
- Ensure your system supports Khmer script rendering.
