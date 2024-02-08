# Language Detection Web Application

This repository contains a simple web application for language detection built using Flask, NLTK for word tokenization, and a Multinomial Naive Bayes model trained on a Count Vectorizer. The application allows users to input text, and it returns the predicted language.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/language-detection-app.git
   cd language-detection-app
   ```

2. **Install Dependencies:**
```bash
pip install flask nltk
```

3. **Run the Application:**
```bash
python app.py

Open your web browser and go to http://127.0.0.1:5000/ to use the language detection application.
```

4. **How to Use:**

- Enter text in the provided input box.
- Click the "Detect Language" button.
- The predicted language will be displayed.

5. **Code Structure**

- app.py: Flask application file containing the code for initializing the Flask app, loading the model and vectorizer, and defining the route for language detection.

- templates/home.html: HTML template for the home page of the web application.

- model_all.pkl: Pickle file containing the trained Multinomial Naive Bayes language detection model.

- cv_all.pkl: Pickle file containing the CountVectorizer used for text vectorization.

## Acknowledgments
This application uses the Flask framework for web development. Learn more about Flask here.

NLTK is used for word tokenization. Explore NLTK here.

The language detection model is based on the Multinomial Naive Bayes algorithm and utilizes a Count Vectorizer for text representation.

Feel free to explore, modify, and adapt the code for your specific use case. If you have any questions or suggestions, please open an issue or reach out to kvedant451@gmail.com.



