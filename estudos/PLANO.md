# Plano de estudos — retomada AI-103

**Premissa:** 3 sessões/semana de ~1h → 35 sessões (28 do curso + 7 da trilha de certificação) ≈ **12 semanas**. Ajuste o ritmo se precisar.
Cada sessão: teoria (15 min) → ler código (15 min) → rodar (15 min) → exercício (15 min).
Material: [índice do Classroom](material/00-INDICE-CLASSROOM.md) · [resumo do Notion](material/01-RESUMO-NOTION.md)

Legenda: `[ ]` a fazer · `[~]` em andamento · `[x]` feito · *(portal)* = feito no portal Foundry, sem código

## Semana 0 — Preparar e medir
- [ ] S0. Ambiente: `uv`, Python 3.13, `az login`, `.env` dos labs; testar se Azure for Students / Skillable ainda funcionam
- [ ] S0b. **Simulado diagnóstico** (Forms do Classroom) → anotar nota no PROGRESSO
- [x] S0c. Material do Classroom indexado em `estudos/material/`
- [ ] S0d. Copiar do repo do professor os labs que faltam (3.3a, 3.3b, 3.4, 3.5, 3.6, 3.7)

## Módulo 1 — IA Generativa (`IA-Studio`) · slides PowerPoint_01
- [ ] S1. Labs 1.1/1.2 *(portal)* — Foundry, catálogo de modelos, avaliação
- [ ] S2. Lab 1.3 `chat-app` — Responses API, histórico, versão async
- [ ] S3. Lab 1.5 `tools-app` — `file_search`, `web_search`, `code_interpreter`, `function`
- [ ] S4. Labs 1.4/1.6 *(portal, novos)* — fine-tuning e guardrails (filtros de conteúdo)

## Módulo 2 — Agentes (`IA-Agents`) · slides PowerPoint_02
- [ ] S5. Lab 2.1 — Primeiro agente Foundry + code interpreter
- [ ] S6. Lab 2.2 — FunctionTool: agente chamando funções Python
- [ ] S7. Lab 2.3/2.4 — MCP (servidor remoto, aprovação de chamadas)
- [ ] S8. Foundry IQ + AI Search *(novo)* e Lab 2.5 (Teams — só leitura se não houver admin)
- [ ] S9. Workflow de agentes *(portal, novo)*
- [ ] S10. Lab 2.7 — Microsoft Agent Framework (`@tool`, `Agent`)
- [ ] S11. Lab 2.8 — Multiagente sequencial (`SequentialBuilder`)
- [ ] S12. Lab 2.9 — A2A: roteador + agentes remotos
- [ ] S13. Revisão Módulo 2 + `/quiz agentes`

## Módulo 3 — Linguagem e fala (`IA-Language`) · slides PowerPoint_03
- [ ] S14. Lab 3.1 — Text Analytics (sentimento, entidades)
- [ ] S15. Lab 3.2 — Agente de texto com MCP da Linguagem
- [ ] S16. Lab 3.3a/b *(novo)* — TTS e STT com `gpt-4o-mini-tts/transcribe`
- [ ] S17. Lab 3.4 *(novo)* — Speech SDK: correio de voz
- [ ] S18. Lab 3.5/3.6 *(novo)* — Speech em agente (MCP) e Voice Live
- [ ] S19. Lab 3.7 *(novo)* — Tradução de texto e fala
- [ ] S20. Revisão Módulo 3 + `/quiz linguagem`

## Módulo 4 — Visão (`IA-Vision`) · slides PowerPoint_04
- [ ] S21. Lab 4.1 — Chat com imagem (multimodal)
- [ ] S22. Lab 4.2/4.3 — Gerar imagem (`gpt-image-2`) e vídeo (`sora-2`)
- [ ] S23. Lab 4.4/4.5/4.6 — Content Understanding (portal + API)
- [ ] S24. Labs 4.7/4.8 *(novos, opcionais — custo AI Search)* — Document Intelligence e knowledge mining
- [ ] S25. Revisão Módulo 4 + `/quiz visao`

## Trilha Certificação AI-103 (lacunas dos simulados — ver [análise](material/02-ANALISE-SIMULADOS.md))
- [ ] C1. Observabilidade I — Application Insights + OpenTelemetry + tracing de agentes
- [ ] C2. Observabilidade II — métricas, logs de diagnóstico, cota/429, custos
- [ ] C3. Segurança — prompt shields (prompts × documentos), filtros de conteúdo, PII
- [ ] C4. Avaliação — evaluators (groundedness, RAG), temperature/top-p, system message × few-shot
- [ ] C5. Azure AI Search para agentes — retrieval, skills de indexação, conexões/credenciais
- [ ] C6. Tools OpenAPI 3.0 + connections com API key
- [ ] C7. Practice Assessment oficial da Microsoft + refazer os 3 simulados do curso

## Fechamento — Projeto final (`senai-ai-assistant`)
- [ ] S26. Arquitetura multi-provider (providers → services → tools → views), Aulas 01–03
- [ ] S27. RAG + OCR por dentro (Aulas 04–05)
- [ ] S28. Projeto: aba **"Tutor AI-103"** com RAG sobre `estudos/material/` + simulado final de novo (comparar nota)
