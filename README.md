# RAG-Langchain-App-Using-Llama
Custom Trained LLM application with Llama, and grounding via RAG

Retrieval Augmented Generation (RAG) is a technique used to enhance the knowledge of large language models (LLMs) by incorporating additional, often private or real-time, data. While LLMs can reason about a wide range of topics, their knowledge is restricted to publicly available data up to a specific point in time when they were trained. However, if you aim to create AI applications capable of reasoning about private data or information introduced after a model’s training, you must augment the model’s knowledge with the specific details it requires. The process of integrating relevant information into the model prompt is referred to as Retrieval Augmented Generation (RAG). This approach allows LLMs to generate more contextually accurate and up-to-date responses. 😊

<h3>General Flow for an RAG Application</h3>
<ul>
<li>Reading Dataset, Data Cleaning, Dividing in Chunks</li>
<li>Encoding Each Source of Data, and Store it as a Dataframe, to prevent recomputation</li>
<li>Create an instance of Llama3. Take User prompt a input</li>
<li>Fetch K-Nearest-Neighbours for text matching with the prompt. Reframe the prompt accordingly</li>
<li>Encode the prompt and pass it to the model</li>
<ul>

<h3>Files to Compile<h3>
<ul>
<li>pdfReader - To read, chunk and encode PDF Data</li>
<li>rag-llama3-demo - To create instance of model, perform RAG and get output</li>
<ul>