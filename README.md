# RAG-Langchain-App-Using-Llama
Custom Trained LLM application with Llama, and grounding via RAG

Retrieval Augmented Generation (RAG) is a technique used to enhance the knowledge of large language models (LLMs) by incorporating additional, often private or real-time, data. While LLMs can reason about a wide range of topics, their knowledge is restricted to publicly available data up to a specific point in time when they were trained. However, if you aim to create AI applications capable of reasoning about private data or information introduced after a model’s training, you must augment the model’s knowledge with the specific details it requires. The process of integrating relevant information into the model prompt is referred to as Retrieval Augmented Generation (RAG). This approach allows LLMs to generate more contextually accurate and up-to-date responses. 😊

<h3>A typical RAG application has two main components:</h3>

Indexing: a pipeline for ingesting data from a source and indexing it. This usually happens offline.

Retrieval and generation: the actual RAG chain, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.
