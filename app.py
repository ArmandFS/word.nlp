import streamlit as st
import pandas as pd
import numpy as np
import textdistance
import re
from collections import Counter
import nltk

# Load the data and prepare the vocabulary and probabilities
with open("autocorrect book.txt", 'r', encoding='utf-8') as f:
    data = f.read().lower()
    words = re.findall('\w+', data)

V = set(words)
words_freq_dict = Counter(words)
Total = sum(words_freq_dict.values())
probs = {k: v / Total for k, v in words_freq_dict.items()}

def autocorrect(word):
    word = word.lower()
    if word in V:
        return ('Your word seems to be correct', word)
    else:
        suggestions = []
        for correct_word in V:
            if nltk.edit_distance(word, correct_word) <= 2:
                suggestions.append((correct_word, probs[correct_word]))
        suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)[:3]
        if suggestions:
            return ('Suggestions:', *suggestions)
        else:
            return ('No close matches found.')

#Streamlit App
st.title("Word.NLP")
st.write("Welcome to Word.NLP Type a word and get suggestions if it's incorrect!")

#Input from user
user_input = st.text_input("Enter a word:", "")

if user_input:
    result = autocorrect(user_input)
    if result[0] == 'Your word seems to be correct':
        st.success(f"✅ {result[1]} is correct!")
    elif result[0] == 'Suggestions:':
        st.warning("🔍 Did you mean:")
        for suggestion in result[1:]:
            st.write(f"• {suggestion[0]} (Probability: {suggestion[1]:.4f})")
    else:
        st.error("❌ No close matches found.")

# Add some enhancements
st.sidebar.title("About")
st.sidebar.info("""
This autocorrect app uses a simple text analysis approach to provide suggestions for misspelled words.
It leverages the NLTK library for calculating edit distances and a frequency-based model for ranking suggestions.
""")


#Adding a footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #40444B;
        color: white;
        text-align: center;
    }
    </style>
    <div class="footer">
        <p>Made with ❤️ using Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)


