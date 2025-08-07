# Neo-Stats-AI-Chat-Bot-
This project implements an AI-powered chatbot designed to enable interactive and dynamic querying of static, domain-specific reports. By leveraging retrieval-augmented generation (RAG) techniques, the chatbot extracts precise information directly from uploaded report data and delivers both concise summaries and detailed answers.

The chatbot strictly limits responses to only the content within the uploaded dataset to ensure accuracy and avoid hallucination. A modular architecture integrates OpenAI embeddings, FAISS vector search, and a chunking strategy for efficient semantic retrieval and natural language answer generation. The web-based interface offers an intuitive user experience with toggles for answer detail levels.

Future enhancements include live web search integration to supplement the dataset insights with up-to-date information, further expanding the chatbot's usefulness.
