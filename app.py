from collections import deque
import re
import streamlit as st

STUDENT_NAME = "Shah Shoaib"
ROLL_NO = "22CO43"
SUBJECT = "AI"

GRAPH = {
    "AI": ["Search Algorithms", "Machine Learning", "NLP"],
    "Search Algorithms": ["BFS", "DFS", "A* Search"],
    "Machine Learning": ["Regression", "Classification", "Clustering"],
    "NLP": ["Tokenization", "Text Similarity", "Chatbot"],
    "BFS": [], "DFS": [], "A* Search": [], "Regression": [],
    "Classification": [], "Clustering": [], "Tokenization": [],
    "Text Similarity": [], "Chatbot": []
}

FAQS = {
    "ai": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
    "bfs": "BFS explores a graph level by level using a queue.",
    "dfs": "DFS explores one branch deeply before backtracking.",
    "regression": "Regression predicts a continuous numeric value.",
    "classification": "Classification predicts a category or class.",
    "clustering": "Clustering groups similar data points without predefined labels.",
    "nlp": "NLP enables computers to process and analyze human language."
}

def bfs_path(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbour in GRAPH.get(node, []):
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))
    return None

def academic_advice(marks, attendance):
    advice = []
    if marks < 40:
        advice.append("Revise fundamentals and solve basic practice questions.")
    elif marks < 60:
        advice.append("Review weak topics and take a mock test.")
    else:
        advice.append("Practice advanced questions and past papers.")
    if attendance < 75:
        advice.append("Attendance is below 75%; review missed lectures and improve attendance.")
    else:
        advice.append("Your attendance is at least 75%. Keep it consistent.")
    return advice

def chatbot(question):
    words = re.findall(r"[a-z]+", question.lower())
    for word in words:
        if word in FAQS:
            return FAQS[word]
    return "I do not know that yet. Ask about AI, BFS, DFS, regression, classification, clustering, or NLP."

st.set_page_config(page_title="Student Academic Assistant", page_icon="🎓", layout="centered")

st.title("🎓 AI-Powered Student Academic Assistant")
st.caption("Experiment 10 · Mini Project · Artificial Intelligence")

with st.sidebar:
    st.subheader("Project details")
    st.write(f"**Student:** {STUDENT_NAME}")
    st.write(f"**Roll No.:** {ROLL_NO}")
    st.write(f"**Subject:** {SUBJECT}")
    st.divider()
    st.caption("A simple educational demo using BFS and rule-based responses.")

tab_search, tab_advice, tab_chat, tab_topics = st.tabs(
    ["🔎 Topic Search", "📘 Academic Advice", "💬 FAQ Chatbot", "🗂️ Topics"]
)

with tab_search:
    st.subheader("Find a topic path with Breadth-First Search (BFS)")
    topics = list(GRAPH.keys())
    start = st.selectbox("Start topic", topics, index=topics.index("AI"))
    goal = st.selectbox("Goal topic", topics, index=topics.index("BFS"))
    if st.button("Find path", type="primary"):
        path = bfs_path(start, goal)
        if path:
            st.success(" → ".join(path))
            st.caption(f"Path contains {len(path) - 1} edge(s).")
        else:
            st.warning(f"No path found from {start} to {goal} in the current graph.")

with tab_advice:
    st.subheader("Rule-based academic advice")
    marks = st.number_input("Test marks (%)", min_value=0.0, max_value=100.0, value=65.0, step=1.0)
    attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=80.0, step=1.0)
    if st.button("Get academic advice", type="primary"):
        for item in academic_advice(marks, attendance):
            st.write(f"- {item}")
        st.caption("This is general study guidance, not an official academic assessment.")

with tab_chat:
    st.subheader("Academic FAQ chatbot")
    question = st.text_input("Ask about AI, BFS, DFS, regression, classification, clustering, or NLP")
    if st.button("Ask assistant", type="primary"):
        if question.strip():
            st.info(chatbot(question))
        else:
            st.warning("Please enter a question first.")

with tab_topics:
    st.subheader("Available topics")
    for topic, children in GRAPH.items():
        if children:
            st.markdown(f"**{topic}**")
            st.write(", ".join(children))
        else:
            st.write(f"- {topic}")

st.divider()
st.caption("Built as a student mini project. The chatbot uses predefined FAQs and is not a generative AI model.")
