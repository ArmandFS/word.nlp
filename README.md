# 🚀 Word.NLP 🚀

![worddoto](https://github.com/ArmandFS/word.nlp/assets/68105213/4f48c0ed-e1ee-4705-ae3b-ece6056c5a59)

Welcome to Word.NLP! This is a simple **Natural Language Processing** project made using a .txt notebook file which contains the majority of words in the **English Langage**.

👇 Here's a simple rundown to how it works! 👇

1. **Load Vocabulary:** Word.NLP uses a pre-loaded notebook.txt file containing common words and their frequencies.
2. **Analyze Input:** When you enter a word, the application calculates the edit distance between it and every word in the vocabulary.
3. **Suggest Corrections:** Words with the lowest edit distance, indicating high similarity to your input, are prioritized as suggestions.
4. **Frequency Ranking:** The suggestions are further ranked based on their frequency in the vocabulary, ensuring commonly used words are suggested more prominently.
5. **Display Results:** The application displays your input word, along with any suggested corrections and their corresponding probabilities (optional, depending on your implementation).

A few downsides of this project is:
1. **A bit too simple:** This is a very simple streamlit project that can be improved upon later on.
2. **a limited dataset:** The dataset that was used is limited and doesn't contain all of the words in the English Language.


🚀 How to run the streamlit app if you ever find yourself modifying it 🚀

Streamlit is simple, all you need to do is to modify the main app.py code, next, you can run this in the terminal:

```
streamlit run app.py
```

And in the localhost server, your modified app will be up in no time!

To deploy this and make it useable, you will need to create your own github repository and follow what I've done here. This requires a requirements.txt file and the python app file.

The link for this streamlit app can be found [here](https://keyboard-auto-nlp-fpxbvtbyje6ibht3s5czkl.streamlit.app/)! 
