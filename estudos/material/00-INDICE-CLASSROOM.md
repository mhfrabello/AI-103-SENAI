# Índice do Google Classroom — AI-103 (N26-AI103-01)

Turma: "Desenv. de Agentes com IA - AI-103" — conta mhfrabellopsf@gmail.com (`/u/1/`)
Atividades: https://classroom.google.com/u/1/w/Nzk4NDM0NTE2Nzg4/t/all
Extraído em 2026-10-18.

## Documentos gerais
- **Notion completo do curso:** https://app.notion.com/p/Desenv-de-Agentes-com-IA-AI-103-39ad3b9fea098075ad4fdc7ea1898f69
- **Curso oficial Microsoft (AI-103T00):** https://learn.microsoft.com/en-us/training/courses/ai-103t00
- **Certificação Azure AI Apps and Agents Developer Associate** (com simulado oficial):
  https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/?practice-assessment-type=certification
- **Trilha e voucher:** https://learn.microsoft.com/en-us/credentials/microsoft-credentials-ai-challenge · https://events.microsoft.com/
- **Labs Skillable** (ambiente Azure pronto): https://msle.learnondemand.net/User/Login?returnUrl=%2FClass%2F760773 (código da turma no Classroom)
- **Oportunidades SENAI:** http://oportunidades.sp.senai.br/
- **Azure for Students:** https://go.microsoft.com/fwlink/?linkid=2180964

### Preparação do ambiente (do professor)
1. Instalar `uv` (ver Notion: "instalando UV")
2. Pasta de trabalho → `git init` → ligar ao GitHub (`git remote add origin ...`)
3. Pastas: `IA-Studio`, `IA-Agents`, `IA-Language`, `IA-Vision`
4. No `.gitignore`: `mslearn-ai-studio`, `mslearn-ai-agents`, `mslearn-ai-language`, `mslearn-ai-vision`, `mslearn-ai-information-extraction`

## Módulo 1 — IA Generativa
- Slides: `AI-103T00-PowerPoint_01.pt-BR.pdf` (no Classroom)
- Notion: https://app.notion.com/p/IA-Generativa-39ad3b9fea098041a94fd5c3ff663222
- Labs Microsoft (`mslearn-ai-studio`):
  1. [Explorar o Foundry](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/01-Explore-ai-studio.html)
  2. [Catálogo de modelos e avaliação](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/02-model-catalog-evaluation.html)
  3. [Foundry SDK](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/03-foundry-sdk.html) → `IA-Studio/chat-app`
  4. [Usar seus próprios dados (RAG)](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/04a-use-own-data.html) → `IA-Studio/tools-app`
  5. [Fine-tuning](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/04b-finetune-model.html)
  6. [Filtros de conteúdo](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/06-Explore-content-filters.html)

## Módulo 2 — Agentes de IA
- Slides: `AI-103T00-PowerPoint_02.pt-BR.pdf`
- Notion: https://app.notion.com/p/Agentes-de-IA-39ad3b9fea0980398a14f76e5faf9a88
- Labs Microsoft (`mslearn-ai-agents`):
  1. [Agente no portal e VS Code](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/01-build-agent-portal-and-vscode.html) → Lab2.1
  2. [Ferramentas customizadas](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/02-agent-custom-tools.html) → Lab2.2
  3. [Integração MCP](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/03-mcp-integration.html) → Lab2.3/2.4
  4. [Foundry IQ](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/04-integrate-agent-with-foundry-iq.html)
  5. [M365 / Teams](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/05a-m365-teams-integration.html) → Lab2.5
  6. [Workflow no Foundry](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/06-build-workflow-ms-foundry.html) (Lab2.6 — feito no portal, sem código)
  7. [Agent Framework](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/07-agent-framework.html) → Lab2.7
  8. [Multiagentes com Agent Framework](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/08-agent-framework-multi-agents.html) → Lab2.8
  9. [Agentes remotos com A2A](https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/09-multi-remote-agents-with-a2a.html) → Lab2.9

## Módulo 3 — Soluções de Linguagem Natural
- Slides: `AI-103T00-PowerPoint_03.pt-BR.pdf`
- Notion: https://app.notion.com/p/Solu-es-de-Linguagem-Natural-39ad3b9fea098058b12fe88a867c6cf6
- Labs Microsoft (`mslearn-ai-language`):
  1. [Analisar texto](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/01-analyze-text.html) → Lab3.1
  2. [Agente de análise de texto](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/02-language-agent.html) → Lab3.2
  3. [Fala com IA generativa](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/03-gen-ai-speech.html) → Lab3.3a/b
  4. [Azure Speech](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/04-azure-speech.html) → Lab3.4
  5. [Azure Speech + MCP](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/05-azure-speech-mcp.html) → Lab3.5
  6. [Agente Voice Live](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/06-voice-live-agent.html) → Lab3.6
  7. [Tradução](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/07-translation.html) → Lab3.7

## Módulo 4 — Dados Visuais
- Slides: `AI-103T00-PowerPoint_04.pt-BR.pdf`
- Notion: https://app.notion.com/p/Dados-Visuais-39ad3b9fea098016b767eeeebe1711ed
- Labs Microsoft (`mslearn-ai-vision`):
  1. [Chat com visão](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Exercises/01-gen-ai-vision.html) → Lab4.1
  2. [Gerar imagens](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Exercises/02-generate-image.html) → Lab4.2
  3. [Gerar vídeo](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Exercises/03-generate-video.html) → Lab4.3
  4. [Content Understanding](https://microsoftlearning.github.io/mslearn-ai-vision/Instructions/Exercises/04-content-understanding.html) → Lab4.4
- Labs Microsoft (`mslearn-ai-information-extraction`):
  1. [Content Understanding (portal)](https://microsoftlearning.github.io/mslearn-ai-information-extraction/Instructions/Exercises/01-content-understanding.html) (Lab4.5 — portal)
  2. [Content Understanding API](https://microsoftlearning.github.io/mslearn-ai-information-extraction/Instructions/Exercises/02-content-understanding-api.html) → Lab4.6
  3. [Document Intelligence](https://microsoftlearning.github.io/mslearn-ai-information-extraction/Instructions/Exercises/03-document-intelligence.html)
  4. [Knowledge Mining](https://microsoftlearning.github.io/mslearn-ai-information-extraction/Instructions/Exercises/04-knowledge-mining.html)

## Streamlit — Projeto final (`senai-ai-assistant`)
- Site: https://streamlit.io/ · Repo do professor: https://github.com/richard-brosler-senai/n26-des-ia103-02
- [Aula 01 — Introdução](https://app.notion.com/p/Aula-1-Introdu-o-3b5d3b9fea098032aaa8f05d94636017)
- [Aula 02 — Construindo interfaces](https://app.notion.com/p/Aula-2-Construindo-Interfaces-Profissionais-com-Streamlit-3bad3b9fea0980749534c1ab484e30ac)
- [Aula 03 — Integração de modelos (multi-provider)](https://app.notion.com/p/Aula-03-Integra-o-de-Modelos-de-IA-Generativa-utilizando-Arquitetura-Multi-Provider-3bbd3b9fea09801d8265d5f5b3b0d6d0)
- [Aula 04 — RAG](https://app.notion.com/p/Aula-04-Implementa-o-de-RAG-3bcd3b9fea0980f9b6d3e32a11d15b12)
- [Aula 05 — RAG, OCR e configurações](https://app.notion.com/p/Aula-05-Ajustes-e-OCR-3c1d3b9fea09803ba61fd68e16ac1cda)
- [Aula 06 — Finalização](https://app.notion.com/p/Aula-06-Finaliza-o-do-projeto-3c2d3b9fea0980eabae2e5802a5c20fd)

## Simulado final (Google Forms)
- https://forms.gle/GRjpXhD3DnWDjmoD6
- https://forms.gle/jMngt6Bpx2QQaww1A
- https://forms.gle/sVGKeagcr8USCWrf6
