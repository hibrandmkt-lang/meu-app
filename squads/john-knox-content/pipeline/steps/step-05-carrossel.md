---
execution: subagent
agent: squads/john-knox-content/agents/arquiteto-de-carrossel
model_tier: powerful
inputFile: squads/john-knox-content/output/estrategia-editorial.md
outputFile: squads/john-knox-content/output/carrosseis.md
---

# Step 05: Criação dos Carrosséis

## Context Loading

Carregar antes de executar:
- `squads/john-knox-content/output/analise-teologica.md` — análise da aula
- `squads/john-knox-content/output/estrategia-editorial.md` — ângulos e linha editorial
- `squads/john-knox-content/pipeline/data/estrutura-carrossel.md` — templates de estrutura
- `squads/john-knox-content/pipeline/data/tom-de-voz.md` — tom de voz

## Instructions

### Process

Criar **3 carrosséis completos** com slides detalhados:

**Carrossel 1 — Ensino** (7–10 slides): baseado no conteúdo principal da aula
**Carrossel 2 — Provocação/Reflexão** (5–7 slides): baseado em uma pergunta ou tensão da aula
**Carrossel 3 — Lista Prática** (5–8 slides): aplicações práticas em formato de lista

Para cada carrossel, detalhar:
- Título do carrossel (capa)
- Slide por slide: texto principal + texto secundário (se houver) + instrução de design
- Último slide: CTA + instrução de design

### Output Format

```
=== CARROSSÉIS ===

=== CARROSSEL 1 — [TIPO: ENSINO] ===
Tema: [tema]
Tom: [reflexivo/educativo/provocativo]
Número de slides: [N]

CAPA (Slide 1):
Título: "[texto principal — máx 8 palavras]"
Subtítulo: "[texto secundário — opcional]"
Design: [instrução: fundo escuro, tipografia grande, imagem de fundo etc.]

SLIDE 2:
Texto principal: "[máx 20 palavras]"
Texto secundário: "[detalhe ou citação bíblica]"
Design: [instrução]

SLIDE 3:
[mesma estrutura]

... até o último slide

ÚLTIMO SLIDE:
CTA: "[chamada para ação]"
Pergunta de engajamento: "[pergunta para comentários]"
Design: [instrução]

---

=== CARROSSEL 2 — [TIPO: REFLEXÃO] ===
[mesma estrutura completa]

---

=== CARROSSEL 3 — [TIPO: LISTA PRÁTICA] ===
[mesma estrutura completa]
```

## Veto Conditions

Rejeitar e refazer se:
1. Menos de 3 carrosséis entregues
2. Algum carrossel tem menos de 5 slides
3. Algum carrossel não tem instrução de design na capa
4. Algum carrossel não tem CTA no último slide
