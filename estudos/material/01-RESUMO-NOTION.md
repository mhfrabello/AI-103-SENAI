# Resumo do Notion do professor (por lab)

> Síntese feita a partir do Notion do prof. Richard (lido em 2026-10-18). Links completos em [00-INDICE-CLASSROOM.md](00-INDICE-CLASSROOM.md).
> "Skillable Lab N" = número do laboratório no ambiente Skillable (Azure pronto, sem gastar crédito).

## Setup padrão de todo lab (receita do professor)
1. Clonar o repo da Microsoft do módulo (`git clone https://github.com/MicrosoftLearning/mslearn-ai-<modulo>`) e apagar o `.git` dele.
2. Copiar `Labfiles/<exercicio>/Python/*` para `IA-<Modulo>\LabX.Y`.
3. Na pasta do lab: `uv init --python 3.13 --vcs none; uv venv; uv add -r .\requirements.txt; code .`
4. Pré-requisitos gerais: VS Code, **Python 3.13** (3.14 quebra dependências), Azure CLI (`az login`), Git, uv.
   PowerShell: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`.

## Módulo 1 — IA Generativa (repo `mslearn-ai-studio`)
| Lab | Tema | Recursos | Skillable | Meu código |
|---|---|---|---|---|
| 1.1 | Preparar projeto de IA (portal Foundry, AI Toolkit VS Code) | Foundry resource + project, `gpt-5.2` | 1 | — (portal) |
| 1.2 | Selecionar, implantar e **avaliar** modelos | 2 modelos (ex. `gpt-5.2` × `gpt-5-mini`), Global Standard | 2 | — (portal) |
| 1.3 | App de chat com Foundry SDK | `azure-ai-projects`, `openai`, `azure-identity` | 3 | `IA-Studio/chat-app` |
| 1.4 | **Fine-tuning** | modelo com suporte a FT, deploy Developer, dataset JSONL | (usar 1) | — |
| 1.5 | App com **tools** (use your own data) | `gpt-5.2` + `text-embedding-3-large`, vector store gerenciado | 4 | `IA-Studio/tools-app` |
| 1.6 | **Guardrails** / filtros de conteúdo | content filters | 5 | — (portal) |

**Destaques do professor (1.5):** ponte entre IA generativa e RAG; usa a API OpenAI (endpoint Azure OpenAI), não a API Foundry como no 1.3; cobre as 4 tools built-in — `code_interpreter`, `web_search`, `file_search`, `function` — que voltam no Módulo 2.

## Módulo 2 — Agentes de IA (repo `mslearn-ai-agents`)
| Lab | Tema | Recursos / atenção | Skillable | Meu código |
|---|---|---|---|---|
| 2.1 | Construir e implantar agente (portal + VS Code) | `gpt-5.2`, AI Toolkit | 6 | Lab2.1 |
| 2.2 | Agente com **ferramentas customizadas** (funções) | Foundry project + agente | 7 | Lab2.2 |
| 2.3 | Conectar **MCP** a agentes | servidor MCP remoto, pacote `mcp`; checar rede | 8 | Lab2.3 / 2.4 |
| 2.4 | Integrar agente ao **Foundry IQ** (AI Search) | — | — | — |
| 2.5 | Publicar agente no **M365 / Teams** | Azure Bot Service, conta M365; precisa admin do tenant; **não roda no Skillable** | — | Lab2.5 |
| 2.6 | **Workflow** orientado a agentes (triagem → suporte) | múltiplos agentes | (testar no 6) | — (não fiz) |
| 2.7 | **Microsoft Agent Framework SDK** | `az login` obrigatório | 10 | Lab2.7 |
| 2.8 | Solução **multiagente** (Agent Framework) | — | 11 | Lab2.8 |
| 2.9 | Agentes remotos com protocolo **A2A** | vários agentes/projetos | (testar no 10) | Lab2.9 |

> Atenção: a numeração dos labs do Notion nem sempre bate com as pastas do meu repo (ex.: meu Lab2.4 é MCP com aprovação).

## Módulo 3 — Soluções de Linguagem Natural (repo `mslearn-ai-language`)
| Lab | Tema | Recursos / atenção | Skillable | Meu código |
|---|---|---|---|---|
| 3.1 | **Analisar texto** (Text Analytics) | `azure-ai-textanalytics`, endpoint `services.ai.azure.com` | 12 | Lab3.1 |
| 3.2 | Agente de análise de texto | MCP da Linguagem do Azure | 13 | Lab3.2 |
| 3.3 | Modelos de IA generativa com **fala** | `gpt-4o-mini-transcribe` (STT) + `gpt-4o-mini-tts` (TTS); 2 pastas: 3.3a e 3.3b | 14 | ❌ falta |
| 3.4 | App com **Azure Speech** | `azure-cognitiveservices-speech`, microfone; bloqueio comum: WebSocket | 15 | ❌ falta |
| 3.5 | Azure Speech dentro de um **agente** | Storage Account + URL SAS, MCP de Fala | 16 | ❌ falta |
| 3.6 | Agente **Voice Live** | SDK Voice Live, microfone; WebRTC/WebSocket | 17 | ❌ falta |
| 3.7 | **Traduzir** texto e fala | `azure-ai-translation-text` + Speech | (tentar 15) | ❌ falta |

## Módulo 4 — Dados Visuais (repos `mslearn-ai-vision` e `mslearn-ai-information-extraction`)
| Lab | Tema | Recursos / atenção | Meu código |
|---|---|---|---|
| 4.1 | App de chat com **visão** | multimodal `gpt-5.2` / `gpt-5.2-mini` | Lab4.1 |
| 4.2 | **Gerar imagens** | `gpt-image-2` | Lab4.2 |
| 4.3 | **Gerar vídeo** com Sora 2 | `sora-2`; disponibilidade regional limitada (Skillable 18) | Lab4.3 |
| 4.4 | Analisar imagens com **Content Understanding** | `azure-ai-contentunderstanding`, API `2025-11-01` | Lab4.4 |
| 4.5 | Extrair info de conteúdo **multimodal** | `gpt-4.1` + `text-embedding-3-large` | — (portal) |
| 4.6 | App cliente de Content Understanding | Entra ID (`DefaultAzureCredential`) | Lab4.6 |
| 4.7 | **Document Intelligence** (prebuilt: nota fiscal, recibo, documento, cartão) | `azure-ai-documentintelligence` | — (não fiz) |
| 4.8 | **Knowledge mining** | AI Search (Basic, custo à parte) + Blob + Knowledge Store | — (não fiz) |

## Streamlit — Projeto integrador `senai-ai-assistant`
| Aula | Conteúdo |
|---|---|
| 01 | O que é Streamlit, console × Streamlit, componentes básicos (texto, entradas, botão), exercício "cadastro de aluno", tela inicial do projeto |
| 02 | UX/UI e boas práticas; `sidebar`, `container`, `columns`, `metric`, `tabs`; versão 2 do assistente (sidebar, dashboard, sobre) |
| 03 | Arquitetura **multi-provider**: `.env`, provider Mock → service → views (dashboard, chat); provider **Groq** (criar conta/chave) |
| 04 | Providers Azure, Gemini e **Ollama**; **RAG** do zero: `sentence_embedding` → `embedding_service` → `pdf_service` → `chunk_service` → `vector_store` → `rag_service` → `views/rag` |
| 05 | Ajustes no RAG; **OCR** com EasyOCR (`ocr_service`, `views/ocr`); tela de configurações (`settings_service`) |
| 06 | Finalização: visão (Azure/Gemini/Groq/Ollama), agentes (`agent_service` + `tools/`), servidor local **llama.cpp** |

## Lacunas para cobrir no plano
- Labs que **não fiz**: 1.4 (fine-tuning), 1.6 (guardrails), 2.4 (Foundry IQ), 2.6 (workflow), 3.3–3.7 (fala/tradução), 4.5, 4.7, 4.8.
- Os **slides** (`AI-103T00-PowerPoint_01..04.pt-BR.pdf`) estão no Classroom; ainda não baixados.
- **Simulado final** (3 Google Forms) — ótimo para medir o nível antes e depois da revisão.
