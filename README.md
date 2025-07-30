# AI-CHATBOT-WITH-NLP
This is a simple NLP-based chatbot built using Python and NLTK. It responds to user queries with pre-defined answers using pattern matching. Ideal for basic conversation and internship-level projects.


**COMPANY**: CODETECH IT SOLUTIONS

**NAME**: MISBAH FIRDOSE H

**INTERN ID**: CT04DZ187

**DOMAIN**: PYTHON PROGRAMMING

**DURATION**: 4 WEEKS

**MENTOR**: NEELA SANTOSH


This Python project demonstrates how to build a basic rule-based AI chatbot using the Natural Language Toolkit (**NLTK**) library. The chatbot is capable of engaging in simple conversations with users by identifying specific patterns in their queries and responding with predefined replies. The main objective of this chatbot is to showcase natural language processing (NLP) techniques and how they can be implemented to simulate a conversational experience.

---

### 🔍 Project Overview

The project begins by importing essential libraries:

* **nltk.chat.util** for using Chat and reflections, which support conversational logic,
* **reflections**, a dictionary that helps the bot understand first- and second-person changes (e.g., “I” to “you”).

The chatbot is designed using a list of `pairs`, where each pair consists of a **regular expression pattern** and a corresponding list of **responses**. When a user enters a message, the chatbot scans for a matching pattern and replies with a suitable response. If no specific pattern is matched, a generic fallback response is provided.

The chatbot handles greetings (e.g., "hello", "hi"), basic questions (like "how are you", "what can you do"), and custom queries related to the internship. This script is interactive, allowing real-time conversation through the console. The use of regular expressions allows basic flexibility in recognizing input patterns.

---

### 💡 Features Implemented

* **Pattern Matching**: Uses regex to identify and respond to predefined user intents.
* **Reflections Handling**: Automatically switches pronouns for a more natural reply flow.
* **Interactive Console Chat**: User inputs and chatbot responses are handled in real-time.
* **Internship Awareness**: Customized to respond to queries about CodTech and the internship task.
* **Exit Condition**: Typing "bye" or "exit" gracefully ends the conversation.

---

### 🧠 Natural Language Processing

The bot uses **basic NLP** through the `nltk.chat` module, making it ideal for beginners. Though not powered by machine learning, it introduces core concepts of:

* Rule-based intent recognition,
* Tokenization and reflections in dialogue,
* Simple regex-based conversation control.

For more advanced implementations, this framework can be expanded using libraries like **spaCy**, **transformers**, or integrated with a trained intent classification model.

---

### 🖥️ How to Run

1. Install the required library:

   ```bash
   pip install nltk
   ```
2. Save the chatbot script as `chatbot.py`
3. Run the chatbot from terminal:

   ```bash
   python chatbot.py
   ```
4. Start chatting with the bot. Type "bye" to exit.

---

### ✅ Conclusion

This chatbot provides a foundational understanding of how natural language processing works in a Python environment. It showcases how developers can build rule-based conversational systems using libraries like NLTK. While simple, this project offers an excellent entry point into NLP and chatbot development, and demonstrates how conversational agents can be built using core Python techniques.


### OUTPUT 
<img width="954" height="156" alt="image" src="https://github.com/user-attachments/assets/2f680ce2-8351-422d-ad49-d588adec6a28" />
