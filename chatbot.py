import os
from embedchain import App
import absl.logging
import re
import streamlit as st
from fuzzywuzzy import process
from streamlit_chat import message  # For chat-style UI

# Initialize absl logs
absl.logging.set_verbosity(absl.logging.INFO)

# Set Google API key securely
os.environ["GOOGLE_API_KEY"] = "AIzaSyCjxO8VHUVLtKLSgvzDfIh4xmAcDCNa7ZI"

# Create the EmbedChain app
app = App.from_config(config_path="config.yaml")
app.add("https://www.boat-lifestyle.com")

# Mock FAQ dataset
faq_data = {
    "What is your return policy?": "Our return policy allows returns within 7 days of purchase with a valid receipt.",
    "How can I track my order?": "You can track your order by entering the order ID on our tracking page.",
    "What payment methods do you accept?": "We accept credit cards, UPI, PayPal, and bank transfers.",
    "Do you offer international shipping?": "Yes, we offer international shipping to selected countries.",
    "What is your customer service contact?": "You can contact our customer service at support@ourstore.com or call us at +1-800-123-4567.",
    "How do I cancel my order?": "You can cancel your order within 24 hours of placing it by visiting your orders page.",
    "Can I modify my order after placing it?": "Yes, you can modify your order within 12 hours of placing it.",
    "What are your working hours?": "Our working hours are Monday to Friday, 9 AM to 6 PM.",
    "Do you have a physical store?": "Yes, we have a flagship store located at 123 Main Street, Cityname.",
    "Do you offer gift wrapping?": "Yes, we offer gift wrapping services for an additional fee.",
    "What/Providedelivery status of order #12345?":"Your order is on the way and arriving on 25th Jan 2025"
}
# Mock order tracking data
mock_order_data = {
    "12345": "Your order is scheduled to be delivered on January 20, 2025.",
    "67890": "Your order was delivered on January 15, 2025.",
}

# Function to classify query
def classify_and_extract(query):
    if "order" in query.lower():
        intent = "Order Tracking"
        order_id = re.findall(r'\b\d{5}\b', query)
        return intent, [(id, "ORDER_ID") for id in order_id]
    elif "return policy" in query.lower():
        return "FAQ Inquiry", []
    return "General Chat", []

# Function to track order
def track_order(order_id):
    return mock_order_data.get(order_id, "Order ID not found.")

# Function to query LLM
def query_llm(prompt):
    return app.query(prompt)

######
def find_best_faq_match(user_query):
    closest_match = process.extractOne(user_query, faq_data.keys())
    if closest_match and closest_match[1] > 90:  # Only respond for highly relevant matches
        return faq_data[closest_match[0]]
    return None

###### Streamlit UI
st.set_page_config(page_title="E-Commerce Chatbot", page_icon="🛍️", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput > div {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 8px;
    }
    .stButton button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .chat-container {
        height: 200px;
        overflow-y: auto;
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 10px;
        background-color: #ffffff;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🛍️ Interactive E-Commerce Chatbot")
st.subheader("Get instant help with orders, FAQs, and more!")
st.markdown(
    """
    Chat with our AI assistant to:
    - Track your orders 📦
    - Get product recommendations 🎧
    - Find answers to FAQs ❓
    """
)

# Chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Display chat history above the input
st.markdown("### 💬 Chat History")
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    

    for index, message_item in enumerate(st.session_state["chat_history"]):
        if "user" in message_item:
            message(message_item["user"], is_user=True, key=f"user_{index}")
        else:
            message(message_item["bot"], is_user=False, key=f"bot_{index}")
    st.markdown("</div>", unsafe_allow_html=True)



# Initialize session state variables
if "user_query" not in st.session_state:
    st.session_state["user_query"] = " "  # User input state


# Text input for user query
user_query = st.text_input("Ask me anything:", st.session_state["user_query"], key="user_query_input",placeholder="Type your question here...")

if st.button("Send") and user_query.strip():
    # Add user query to chat history
    st.session_state["chat_history"].append({"user": user_query.strip()})

    # Check FAQ match first
    faq_response = find_best_faq_match(user_query)
    if faq_response:
        response = f"FAQ Response: {faq_response}"
    else:
        # Handle complex queries using classification and LLM
        intent, entities = classify_and_extract(user_query)
        if intent == "Order Tracking":
            order_id = entities[0][0] if entities else None
            response = track_order(order_id)
        else:
            # Default to querying the LLM
            response = query_llm(user_query)

    # Add bot response to chat history
    st.session_state["chat_history"].append({"bot": response})

    # Clear input and force rerun
    st.session_state["user_query"] = " "  # Clear input
    st.rerun()  # Force rerendering of the app


# Add FAQ section for user exploration
with st.expander("📋 Frequently Asked Questions"):
    st.markdown("Here are some common questions you can ask:")
    for question, answer in faq_data.items():
        st.write(f"**Q: {question}**")
        st.write(f"A: {answer}")
        st.markdown("---")  # Divider for readability
