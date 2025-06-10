# Movie Recommendation System

![Movie Recommendation System](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Content%20Based-FF6F00)

Welcome to the **Movie Recommendation System** project! This system suggests five similar movies based on a given movie name using a content-based recommendation approach. It leverages the TMDB 5000 Movie Dataset, Python, and Streamlit to create an interactive web application.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to build a movie recommendation system that suggests five similar movies based on a user's input. The system uses a content-based approach, comparing features like genres, keywords, cast, and crew to find movies that are alike. The workflow includes:

1. **Data Collection**: Using the TMDB 5000 Movie Dataset.
2. **Data Preprocessing**: Cleaning and preparing the data for analysis.
3. **Model Development**: Building a recommendation engine using cosine similarity.
4. **Web Interface**: Creating an interactive web app using Streamlit.

## Features

- **Content-Based Recommendation**: Suggests movies based on similarity in genres, keywords, cast, and crew.
- **Interactive Web Interface**: Built with Streamlit for a user-friendly experience.
- **Movie Details**: Displays movie posters, overviews, release dates, ratings, and genres.
- **Deployment**: Hosted on Streamlit Sharing for easy access.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   Open your browser and go to [http://localhost:8501](http://localhost:8501).

## Usage

1. **Select a Movie**: Choose a movie from the dropdown menu.
2. **Get Recommendations**: Click the "Recommend" button to see five similar movies.
3. **Explore Movie Details**: View movie posters, overviews, release dates, ratings, and genres for each recommended movie.

## Deployment

The app is deployed using Streamlit Sharing. You can access it here:

[Movie Recommendation System](https://subhashbisnoi-automobile-price-predictor-app-vrwn5r.streamlit.app)

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. **Open a pull request**.

Please ensure your code follows the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
