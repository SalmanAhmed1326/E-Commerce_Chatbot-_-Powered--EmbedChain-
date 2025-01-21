# EmbedChain-Powered E-Commerce Chatbot

## Overview
This project showcases a multi-functional chatbot designed for e-commerce applications. The chatbot uses the EmbedChain platform for advanced natural language understanding and integrates several machine learning and natural language processing techniques for product recommendations, order tracking, FAQ handling, and general user interactions. It is equipped to interact with a website's content and provide dynamic, real-time responses to user queries.

## Features

1. **Product Search and Recommendations:**
   - Users can search for products by providing specific criteria (e.g., "Recommend the best wireless headphones under $100").
   - The chatbot uses EmbedChain's LLM capabilities to generate relevant recommendations.

2. **Order Tracking:**
   - Recognizes order IDs using custom entity extraction (e.g., `#12345`).
   - Provides order delivery status based on predefined mock data.

3. **FAQ Handling:**
   - Retrieves answers to frequently asked questions using fuzzy string matching (FuzzyWuzzy).
   - Generates responses using EmbedChain's LLM when a match is not found in the FAQ database.

4. **Intent Classification and Entity Recognition:**
   - Classifies user queries into predefined intents (e.g., Product Search, FAQ Inquiry, Order Tracking, or General Chat).
   - Extracts named entities and custom patterns using `spaCy`.

5. **Database Management:**
   - Allows resetting of the database to focus on specific data sources (e.g., website URLs).
   - Supports content embedding for websites.

6. **Fallback Mechanism:**
   - If no direct intent match or FAQ is found, the chatbot queries EmbedChain's LLM to ensure a response is always provided.

---

## How It Works

### 1. EmbedChain Integration
- **Website Content Embedding:**
  The chatbot extracts and embeds content from a specified URL (e.g., `https://www.boat-lifestyle.com`).

- **Query Processing:**
  Queries are sent to the EmbedChain app, which uses its embedded database and LLM to generate responses.

### 2. Intent Classification
- **Model:** Naive Bayes Classifier
- **Training Data:** Simple labeled text examples for classifying intents like Product Search, FAQ Inquiry, and Order Tracking.
- **Text Vectorization:** Implemented using `CountVectorizer`.

### 3. Entity Extraction
- **Tool:** `spaCy` for named entity recognition (NER).
- **Custom Pattern Matching:** Regular expressions for identifying order IDs (e.g., `#12345`).

### 4. FAQ Matching
- **Tool:** FuzzyWuzzy for approximate string matching.
- **Threshold:** Retrieves FAQ answers if similarity score exceeds 80%.

### 5. Order Tracking
- Mock order data is stored in a dictionary.
- Extracted order IDs are used to retrieve order status.

---

## Technologies Used

- **EmbedChain:** LLM-powered chatbot platform for contextual responses.
- **spaCy:** Named entity recognition and custom pattern matching.
- **Scikit-learn:** Intent classification using Naive Bayes.
- **FuzzyWuzzy:** FAQ retrieval through fuzzy string matching.
- **Google API:** API key for secure data integration.
- **Python Libraries:**
  - `os`, `shutil` for file and database management.
  - `re` for regular expressions.

---

## Installation

### Prerequisites
- Python 3.8+
- Required libraries: `embedchain`, `spacy`, `scikit-learn`, `fuzzywuzzy`

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. Set up your EmbedChain configuration in `config.yaml`.

5. Run the chatbot script:
   ```bash
   python chatbot.py
   ```

---

## Usage

1. **Reset Database:**
   If you want to focus the chatbot on a new website, reset the EmbedChain database:
   ```python
   reset_embedchain_data()
   ```

2. **Add a Website:**
   ```python
   app.add("https://www.boat-lifestyle.com")
   ```

3. **Query Examples:**
   - Product Search: "Recommend the best wireless headphone under $100."
   - Order Tracking: "What is the delivery status of order #12345?"
   - FAQ Inquiry: "What is your return policy?"

4. **Simulated User Interaction:**
   Run the `user_interaction()` function for a complete walkthrough of chatbot functionality.

---

## Mock Data
- **Order Tracking:** Predefined delivery statuses for demonstration purposes.
- **FAQs:** A dictionary of commonly asked questions and answers.

---

## Future Enhancements
1. **Dynamic FAQ Database:**
   - Connect to a live FAQ database for real-time updates.
2. **Multi-language Support:**
   - Extend language capabilities using additional spaCy models and translation APIs.
3. **Advanced Recommendation System:**
   - Integrate collaborative filtering or content-based recommendation algorithms.
4. **Voice Interaction:**
   - Add voice-to-text functionality for seamless user interaction.

---

## Contributing
Feel free to fork this repository and submit pull requests for enhancements or bug fixes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For questions or support, please contact:
- **Name:** Salman Ahmed
- **Email:** [sh13jj2648@gmail.com](mailto:sh13jj2648@gmail.com)
- **LinkedIn:** [https://www.linkedin.com/in/salman-ahmed13/](https://www.linkedin.com/in/salman-ahmed13/)
- **Phone:** +91-7410965431

