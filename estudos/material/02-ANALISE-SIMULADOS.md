# Análise dos simulados do curso (AI-103)

Arquivos com as perguntas (sem gabarito): `simulados/ai103-simulado-1.md` (30 q.), `-2.md` (23 q.), `-3.md` (estudo de caso Contoso, ~8 q.).
Fora do git (conteúdo de terceiros). **Nenhum formulário foi enviado.**
Para treinar de verdade: responder os Forms pelo link no [índice](00-INDICE-CLASSROOM.md) — eles dão a nota.

## O que o exame cobra (contagem aproximada pelos enunciados, ~61 questões)
| Tema | Simulado 1 | Simulado 2 | Simulado 3 | Coberto nos labs? |
|---|---|---|---|---|
| **Observabilidade e monitoramento** (Application Insights, OpenTelemetry, tracing, métricas, logs de diagnóstico, erro 429/cota, custos) | ~11 | 1 | — | ⚠️ quase nada |
| **Agentes: tools e conexões** (OpenAPI 3.0 + API key em *connection*, MCP, workflows, Agent Service SDK) | ~8 | ~4 | 1 | ✅ parcial (Labs 2.x) |
| **Grounding / RAG com Azure AI Search** (estratégia de retrieval, credenciais centralizadas, skills de indexação, chunking) | ~4 | ~2 | 2 | ⚠️ só no projeto Streamlit e Lab 1.5 |
| **Segurança e IA responsável** (prompt shields p/ docs × prompts, filtros de conteúdo, PII, groundedness) | ~2 | ~2 | 2 | ⚠️ Lab 1.6 não feito |
| **Avaliação** (evaluators: groundedness, RAG; parâmetros temperature/top-p; system message × few-shot) | ~3 | ~1 | 2 | ⚠️ Lab 1.2 só portal |
| **Fala** (custom speech, real-time STT/TTS, Voice Live, project ID do custom speech) | — | ~5 | — | ❌ Labs 3.3–3.7 faltando |
| **Visão e documentos** (Content Understanding: analyzers prebuilt × custom + confiança, imagens: `input_fidelity`, OCR) | — | ~7 | — | ✅ parcial (Labs 4.x) |

## Conclusões
- **Maior risco:** observabilidade/operação (≈ 1 em cada 5 questões) e quase não aparece nos labs do curso.
- **Segundo risco:** fala (labs 3.3–3.7 não feitos) e segurança/avaliação (labs 1.2/1.6 só de portal).
- Ponto forte provável: agentes e tools (Labs 2.x) e visão (Labs 4.x).
- Estilo das questões: cenário "You have a Microsoft Foundry project that contains an agent..." + escolher serviço/parâmetro/componente. Decorar **qual recurso resolve qual problema** vale mais que código.

## Fontes oficiais para fechar lacunas
- Habilidades medidas / curso: https://learn.microsoft.com/en-us/training/courses/ai-103t00
- Simulado oficial gratuito (Practice Assessment): https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/?practice-assessment-type=certification
