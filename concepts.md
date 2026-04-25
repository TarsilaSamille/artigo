# Analysis of Technical Concepts and Explanations

This document tracks technical concepts used in the Bidayuh Jagoy Translator article that may require better clarification for a general academic reviewer.

| Concept | Status in Text | Current Explanation | Recommendation |
| :--- | :--- | :--- | :--- |
| **Vercel** | **Partially** | Mentioned as a "serverless platform" for the backend. | Explicitly state it is used for hosting stateless API functions without server maintenance. |
| **Supabase** | **Partially** | Defined as a database with `pgvector`. | Clarify it is a Backend-as-a-Service (BaaS) providing real-time PostgreSQL capabilities. |
| **Free Tier / Economic Sustainability** | **Well Explained** | Section 2.2 details how offloading compute allows staying within free cloud limits. | No change needed. |
| **HNSW Index** | **Not Explained** | Just mentioned as the retrieval mechanism. | Briefly define as a graph-based vector retrieval algorithm for high-speed similarity search. |
| **pgvector** | **Partially** | Described as a PostgreSQL extension. | Mention it enables vector similarity searches (Cosine, Euclidean) directly in SQL. |
| **Transformers.js** | **Well Explained** | Section 2.1 detailed it as browser-side execution via WebGPU/WASM. | No change needed. |
| **WASM / WebGPU** | **Well Explained** | Described as hardware acceleration for browser AI. | No change needed. |
| **IBM Model 2** | **Well Explained** | Section 4.4 details its role in probabilistic alignment and why it suits small datasets. | No change needed. |
| **RAG (Retrieval-Augmented Generation)** | **Well Explained** | Section 1 defines it as explicit memory versus implicit model parameters. | No change needed. |
| **Quantization (4-bit ONNX)** | **Partially** | Mentioned in Section 3.2. | Briefly explain it reduces model memory footprint for efficient browser loading. |
| **Land Dayak** | **Partially** | Mentioned in the Abstract. | Useful to note in Section 1 that "Bidayuh" and "Land Dayak" refer to the same ethnic cluster. |
| **HNSW vs Brute Force** | **Not Mentioned** | No comparison provided. | Optional: mention HNSW is used for scalability as the corpus grows. |

## Proposed Action Plan

1. **Clarify BaaS/Serverless**: Add 1 line in Section 2.1 about Vercel/Supabase as managed infrastructure.
2. **Define HNSW**: Add a short parenthetical in Section 4.1.
3. **Language Context**: Briefly note the synonymity of Land Dayak/Bidayuh in the introduction.
4. **Model Footprint**: Clarify the importance of 4-bit quantization for mobile/low-bandwidth users.
