main2.pdf
- Prolo
	- Coisas
		- **Abstract**
		  collapsed:: true
			- "Client centric RAG", "Vercel"
			- "Land Dayak language" adicionar/explicar a "família de linguagens".
			- "local Glossary lookups", "remote vector retrieval" COLOCAR embedding retrieval, e "client-side neural re-ranking".
			- Dúvida: "O que é Transformers.js ??. explicar melhor
			- "Utilizing" - trocar por using
			- neural re-ranking - melhorar
			- "really?" tirar high-fidelity
			- ajeitar se portugues e ingles mesmo texto
		-
		  collapsed:: true
			* **1. Introduction:**

			- **Falta de Referências:** ref - transaformers, gap e majority of tokens.
			- mais informações sobre o dialeto Bidaio Jagoy.
			- "implicit memory -ou seja model parameters  / explicit memory - context information provided to the remote model
			- "Utilize" - trocar por use
			- trocar curriculum por, bunch of helper information like vocabulary,s sentence partern ...
		-
		  collapsed:: true
			2. Related Work:**

			- colocar to the browser depois de offloading
		- **2.1. The Stack Overview:**
			- "O que é Transformers.js ?"
		- **2.2. The "Fat Client" Philosophy:**
		  collapsed:: true
			- "Small" em vez de "quantized" -  e explicar o q faz
			- explicar local-reranking
			- "explicar" Supabase
			- free tier limits - explicar
			- Figure 1 = Aumentar a fonte
			- "explicar" partes específicas do diagrama (Cloud Infrastructure e Supabase pgvector).
		-
		  collapsed:: true
			* **3. Instructional Orchestration:**

			- "multi dimensional context" - especificar ou tirar pq dimensional pq não é bem isso, um contexto com informações de naturezas bastante diversas
			- mudar sintetizador linguistico pra outra coisa
		-
		  collapsed:: true
			* **3.1. Composition of the Instructional Context:**

			- **"ANCORAR EM UM EXEMPLO"**
			- we will depict this point using the exemple of figure y ... e explicar cada contexto no exemplo, colocar setinhas no exemplo...
			- HNSW, supabase- explicar
			- explicar - reranked localy
			- *Context C:** explicar melhor.
			- * *Context D:**- explicar melhor
			- *dense context injection*.  - tirar dense ?
		- * **3.2. Model Management and Caching:**
			- explicar - *CacheStorage API*.
			- *"zero network overhead"* - explicar
		-
		  collapsed:: true
			* **4.1. The Hybrid Retrieval Pipeline:**

			- contextos explicar melhor como fucniona
			- * **Figure 2 :** aumentar fonte
		-
		  collapsed:: true
			* **4.2. Client-Side Re-ranking Algorithm:**

			- tirar conta de similarity
			- * **Listing 1 (Código Python):** aumentar fonte
			- explicar melhor essa parte como funciona
			- explicar webGPU/WASM
		-
		  collapsed:: true
			* **4.3. Structured "Chain-of-Thought" Prompting:**

			- Mostrar em exemplo
			- *Chain-of-Thought*. - REF
			- itens 1, 2 e 3:  referenciar a "section 4.1". EXPLICITAR "instruir Gemini do zero".
			- * **Listing 2 (JSON):** 1) Tamanho (da fonte), 2) Não ficou claro, - referenciar no texto
			- explicar o curated - de onde veio etc
			- the Instructions EXPLICITLY mandate GEMINI TO ...
			- ref - *"IBM Model 2"*.
			- * **Figure 3 e Figure 4:** As imagens extremamente pequenas e ilegíveis.
			- "distortion model"  "?".
			- "??"  "latent variable problem". - EXPLICA como se encaixa q variaveis
			- ibm model**"Prove ou ref!"**  afirmação de que o modelo permanece robusto com apenas alguns milhares de pares de sentenças.
			- explicar melhor heuristic refinment
			- * Falta exemplo ("exemplo") ao lado das 15 regras gramaticais.
			- **  ("O que é?"):**  *Zero-Shot prompting*, *static "black box"*, e *exposed observational patterns*.
		- 5.1. Latency Breakdowns:
			- tirar de introduces to induz
			- comparar a latência com outros sistemas - EXPLICAR
			- "O que é?" *round-trip time*.*
		- **5.2. Community-Driven Correction Loop:**
			- no momento um dos parrticipantes da traducao da biblia
			- * **"explicar a interface"**  (Validate, Correct, Annotate).
			- TIRAR AUTORITATIVO NO CORRECT
		- **5.3. The System Prompt:**
			- **Listing 3 (Prompt):**"TAMANHO da font"* - "Não é um exemplo de verdade"**.
		- 5.4. Qualitative Case Study:
			- Não tem contexto nenhum pra por os ID "Validation ID: 57 and 54".
			- **"DISCUTIR"**
			- COLOCAR OUTPUT DO THE SYSTEM E CORRIGIDO PELO USUARIO
			- Explicar q a linguagem tem possessive suffix - foot note -
		- **5.5. Error Analysis and Fallback Mechanisms:**
			- *"Quem faz a Analysis?"*-  eu pq tava no prompt colocar ??? e colocou - the analisys was made by the author based on output information
		- * **6. Conclusion:**
			- (**"refs!"**)  (*Gemma 2B* ou *TinyLlama*). e outras coisas
			- refs pra as linguagens
		- A. vai no texto talvez na conclusão
- Bruno
	- ![main-2-2.pdf](../assets/main-2-2_1776380907795_0.pdf)
	- Local Infer. - Linguistic Ref. sem abreviação em tabela
	- aspas
	- reference 2.2
	- Listing 2 - feio
	- reference IBM Mmodel
	- We claim that this is an appropriate approach given the characteristics of low resources languages. Reescrever em vez de  ensures ”Human-in-the-loop” accountability,
	- ??? fonte errada - use fonte normal
	- colocar link do endereço no artigo clicar abrir
	- Como fazer uma validação mais consistente? Teria que envolver a comunidade falante e analisar como o sistema evolui. Incluir como trabalho futuro. - estou criando um sistema de validacao por whatsap as pessoas recebem 5 palavras ou frases por dia pra validar quem se interecar sistema em construcao
	-
	-