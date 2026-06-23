---
execution: subagent
agent: squads/john-knox-content/agents/redator-de-posts
model_tier: powerful
inputFile: squads/john-knox-content/output/estrategia-editorial.md
outputFile: squads/john-knox-content/output/posts-prontos.md
---

# Step 04: Geração de Posts Prontos

## Context Loading

Carregar antes de executar:
- `squads/john-knox-content/output/analise-teologica.md` — análise da aula
- `squads/john-knox-content/output/estrategia-editorial.md` — estratégia e ângulos
- `squads/john-knox-content/pipeline/data/tom-de-voz.md` — tom de voz
- `squads/john-knox-content/pipeline/data/pilares-editoriais.md` — pilares

## Instructions

### Process

Gerar **8 posts completos e prontos para publicar**, distribuídos nos formatos:
- 3 posts de feed (Instagram/Facebook) — legendas completas com CTA e hashtags
- 2 posts de reflexão/devocional — mais profundos, texto longo
- 2 stories de texto — diretos, impactantes, máx 3 telas
- 1 post de citação — apenas a frase + referência bíblica

Para cada post:
1. Selecionar o ângulo mais adequado
2. Escrever o hook (primeira linha — deve parar o scroll)
3. Desenvolver o corpo
4. Escrever o CTA (chamada para ação específica)
5. Incluir hashtags relevantes do banco gerado

### Output Format

```
=== POSTS PRONTOS ===

--- POST 1 — FEED ---
Ângulo: [nome]
Tom: [reflexivo/provocativo/encorajador/educativo]
---
[HOOK — primeira linha]

[Corpo do post]

[CTA]

[Hashtags]

--- POST 2 — FEED ---
[mesma estrutura]

--- POST 3 — FEED ---
[mesma estrutura]

--- POST 4 — DEVOCIONAL ---
[texto mais longo, 300-500 palavras]

--- POST 5 — DEVOCIONAL ---
[texto mais longo]

--- POST 6 — STORIES (3 telas) ---
Tela 1: [texto curto + instrução visual]
Tela 2: [texto curto + instrução visual]
Tela 3: [CTA + pergunta ou swipe-up]

--- POST 7 — STORIES (3 telas) ---
[mesma estrutura]

--- POST 8 — CITAÇÃO ---
"[citação exata]"
— [referência/pastor/John Knox]
[hashtags]
```

## Veto Conditions

Rejeitar e refazer se:
1. Algum post não tem CTA
2. Algum hook tem mais de 15 palavras
3. Menos de 8 posts entregues
4. Algum post de feed está sem hashtags
