# Bidaio Jagoy Translator: A Hybrid Client-Centric RAG System for Low-Resource Language Preservation

## 1. System Overview

The **Bidaio Jagoy Translator** is a specialized AI platform designed to preserve and document the **Bidaio Jagoy** language. Unlike generic translation systems, it employs a sophisticated **Retrieval-Augmented Generation (RAG)** architecture that prioritizes linguistic accuracy, grammatical reasoning, and "few-shot" learning from a curated corpus of examples.

The system is architected as a **hybrid client-server RAG application**, where the frontend plays an active role in context orchestration—using in-browser embeddings and local data processing—while the backend handles heavy-lifting vector search and LLM inference. This approach reduces latency for keyword lookups and ensures that the Generative AI (Google Gemini 2.5 Flash) is grounded in explicitly provided linguistic data.

## 2. Core Architecture

The system is built on a modern serverless stack, designed for scalability and minimal maintenance:

*   **Frontend**: Vanilla JavaScript + HTML5 (Zero-build framework approach for simplicity), styled with Tailwind CSS. It leverages **Transformers.js** (`@xenova/transformers`) to run embedding models directly in the user's browser.
*   **Backend**: **FastAPI** (Python) hosted on Vercel Serverless Functions. It acts as a bridge to the LLM and the vector database.
*   **AI Engine**: **Google Gemini 2.5 Flash** (via LangChain), chosen for its large context window and strong reasoning capabilities.
*   **Database & Vector Store**: **Supabase** (PostgreSQL) with `pgvector` extension for storing sentence embeddings and translation history.

## 3. The RAG Implementation (retrieval-Augmented Generation)

The core innovation of the Bidaio system is its **Multi-Staged Context Assembly**, which combines four distinct sources of truth to "teach" the LLM the language on-the-fly for every request.

### 3.1. The Hybrid Retrieval Pipeline

When a user submits a sentence for translation (e.g., via the Bulk Translation feature), the system triggers the `RAGPromptGenerator` which executes the following workflow:

1.  **Keyword Extraction**: The system identifies key content words in the English input.
2.  **Context A: Direct Glossary Lookup (Local)**:
    *   The browser queries a local JSON dictionary to find direct 1:1 translations for key terms.
    *   *Purpose:* Ensures vocabulary consistency and prevents "hallucination" of basic words.
3.  **Context B: Semantic Sentence Retrieval (Remote Vector Search)**:
    *   The client generates an embedding for the input sentence (or sends it to the backend).
    *   A request is made to `/api/search/by-vector` which queries Supabase using cosine similarity.
    *   It retrieves the top $k$ (e.g., 3-5) most semantically similar English-Bidaio sentence pairs from the corpus.
    *   *Purpose:* Provides the LLM with sentence structure patterns and idiomatic expressions.
4.  **Context C: Contextual Usage Examples (Local + In-Browser Re-ranking)**:
    *   The system searches the local corpus for sentences containing the extracted keywords.
    *   **Novelty**: It uses `Xenova/all-MiniLM-L6-v2` running *in the browser* to generate embeddings for these candidates and re-ranks them by similarity to the input.
    *   *Purpose:* Shows how specific words are used in different contexts (disambiguation).
5.  **Context D: Grammatical Constitution (Rule Injection)**:
    *   Relevant grammatical rules are injected directly into the prompt.
    *   *Purpose:* Acts as the "highest authority," creating a hierarchy where explicit rules override probabilistic patterns if they conflict.

### 3.2. Structured "Chain-of-Thought" Prompting

The system does not simply ask for a translation. It constructs a structured prompt that forces the LLM to follow a strict cognitive process:

1.  **Analyze**: Identify the applicable grammatical rules from Context D.
2.  **Vocabulary Selection**: Map words using Context A and C.
3.  **Synthesis**: Assemble the sentence following the patterns in Context B.
4.  **Output**: Return the result as a strict JSON object containing:
    *   `translation`: The final Bidaio text.
    *   `reasoning`: A step-by-step explanation of the decision process.
    *   `confidence_score`: A self-assessed metric of accuracy.

## 4. Key Features & Novelty

*   **Bulk Translation System**: The user interface supports splitting paragraphs into sentences (naïve splitting) and processing them in parallel batches (`/api/translate/bulk`), allowing for document-level translation while maintaining the precision of sentence-level RAG.
*   **Client-Side AI Processing**: By offloading embedding generation and re-ranking to the client (via WebAssembly/Transformers.js), the system reduces the computational load on the backend and enables instant feedback for "keyword usage" checks without a network round-trip for every sub-step.
*   **Ephemeral Correction System**: A feedback loop allows users to submit corrections, which are temporarily stored (ephemeral CSV) for review, enabling a "human-in-the-loop" improvement cycle.
*   **Low-Resource Language Adaptation**: The architecture is specifically tuned for languages with limited data. Instead of fine-tuning a model (which requires massive datasets), it uses a **dense context injection strategy** where the "knowledge" is provided at runtime.

## 5. Directory Structure Reference

*   `api/app.py`: FastAPI backend handling LLM orchestration and Supabase connections.
*   `public/js/rag-translator.js`: The "Brain" of the frontend, handling local embedding generation, context assembly, and prompt construction.
*   `public/js/script.js`: Main UI logic, including the Bulk Translation aggregator.
*   `data/`: JSON files acting as the static knowledge base (Dictionary, Corpus, Grammar).
