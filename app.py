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

# Streamlit App
st.markdown("""
    <style>
    .title {
        color: yellow;
        text-align: center;
    }
    .info {
        background-color: #gray;
        border-radius: 5px;
        padding: 10px;
        margin-top: 20px;
        text-align: center;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #40444B;
        color: black;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Word.NLP</h1>', unsafe_allow_html=True)
st.markdown('<div class="info">Welcome to Word.NLP! Type a word and get suggestions if it\'s incorrect!</div>', unsafe_allow_html=True)

# Input from user
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

st.markdown("""
    <div class="info">
    <h3>About</h3>
    <p>This autocorrect app uses a simple text analysis approach to provide suggestions for misspelled words.
    It leverages the NLTK library for calculating edit distances and a frequency-based model for ranking suggestions. This is a relatively simple project that can be improved upon with implementing perhaps a larger dataset and/or updated NLP methods in the future!</p>
    </div>
""", unsafe_allow_html=True)

# Adding a footer
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
