---
execution: subagent
agent: squads/john-knox-content/agents/estrategista-editorial
model_tier: powerful
inputFile: squads/john-knox-content/output/analise-teologica.md
outputFile: squads/john-knox-content/output/estrategia-editorial.md
---

# Step 03: Estratégia Editorial

## Context Loading

Carregar antes de executar:
- `squads/john-knox-content/output/analise-teologica.md` — análise da aula
- `squads/john-knox-content/pipeline/data/pilares-editoriais.md` — pilares
- `squads/john-knox-content/pipeline/data/tom-de-voz.md` — tom de voz

## Instructions

### Process

1. Ler a análise teológica completa.
2. Definir a **linha editorial** da semana com base na aula.
3. Sugerir **5 ângulos de conteúdo** diferentes para explorar o mesmo tema.
4. Para cada ângulo, definir:
   - Formato ideal (post, carrossel, reels, stories)
   - Gancho principal (hook)
   - Público primário
   - Objetivo (engajamento, salvação, reflexão, compartilhamento)
5. Sugerir **série de conteúdo** se o tema permitir (3–5 posts encadeados).
6. Listar **hashtags estratégicas** (20 hashtags — mix de nicho + alcance).
7. Sugerir **melhor horário/dia** de publicação por formato.
8. Identificar **oportunidades de trend** (o que está em alta que se conecta ao tema).

## Output Format

```
=== ESTRATÉGIA EDITORIAL ===

LINHA EDITORIAL DA SEMANA:
[descrição em 2-3 frases]

ÂNGULOS DE CONTEÚDO:

ÂNGULO 1 — [título]
Formato: [tipo]
Hook: "[frase de abertura]"
Público: [descrição]
Objetivo: [engajamento/reflexão/compartilhamento/salvação]

ÂNGULO 2 — [título]
[mesma estrutura]

... até 5 ângulos

SÉRIE SUGERIDA: "[nome da série]"
Post 1: [ideia]
Post 2: [ideia]
Post 3: [ideia]

HASHTAGS (20):
[lista]

CALENDÁRIO SUGERIDO:
Segunda: [formato + ângulo]
Quarta: [formato + ângulo]
Sexta: [formato + ângulo]
Domingo: [formato + ângulo]

OPORTUNIDADES DE TREND:
- [conexão com trend atual]
```

## Veto Conditions

Rejeitar e refazer se:
1. Menos de 5 ângulos entregues
2. Nenhuma sugestão de série
3. Menos de 15 hashtags
