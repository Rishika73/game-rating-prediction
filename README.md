# Game Rating Prediction

A Data Intensive Computing project for predicting video game ratings using player metrics, review statistics, game engines, and SDK information.

## Overview

This project explores how game technologies and player engagement metrics relate to video game ratings.

The system uses information such as:

- peak players
- positive and negative reviews
- total reviews
- review percentage
- current players
- 24-hour peak
- all-time peak
- game engine and SDK selection

The prediction model is connected to a Flask web application where users can enter these values and receive a predicted game rating.

## How It Works

1. The user enters game and player statistics in the web form.
2. The Flask app collects the form values.
3. `model.py` preprocesses the inputs and prepares the feature columns.
4. The trained model from `model.pkl` generates a rating prediction.
5. The predicted rating is displayed on the same web page.

## Models Explored

During the project, multiple regression models were evaluated, including:

- Linear Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

The ensemble models performed better overall than the simpler baseline models.

## Web Application

The Flask application uses:

- `app.py` for routing
- `model.py` for preprocessing and prediction
- `templates/index.html` for the user interface
- `static/index.css` for styling

## Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- HTML
- CSS
- Bootstrap

## Repository Structure

```text
game-rating-prediction/
├── app.py
├── model.py
├── model.pkl
├── dic_project.ipynb
├── game_data_all.csv
├── project_report.pdf
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── index.css
└── .gitignore
