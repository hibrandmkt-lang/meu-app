---
execution: subagent
agent: squads/john-knox-content/agents/teologo-analista
model_tier: powerful
inputFile: squads/john-knox-content/output/aula-input.md
outputFile: squads/john-knox-content/output/analise-teologica.md
---

# Step 02: Análise Teológica da Aula

## Context Loading

Carregar antes de executar:
- `squads/john-knox-content/output/aula-input.md` — texto completo da aula
- `squads/john-knox-content/pipeline/data/pilares-editoriais.md` — pilares disponíveis
- `squads/john-knox-content/pipeline/data/tom-de-voz.md` — tom de comunicação

## Instructions

### Process

1. Ler o texto completo da aula.
2. Identificar o **tema central** (máximo 1 frase).
3. Mapear os **subtemas** (máximo 5).
4. Extrair **citações poderosas** (mínimo 5, máximo 10) — frases que funcionam sozinhas.
5. Identificar as **aplicações práticas** mencionadas na aula.
6. Mapear o **arco narrativo**: problema → tensão → solução/esperança.
7. Identificar **referências bíblicas** utilizadas com contexto.
8. Classificar o **pilar editorial** principal da aula.
9. Listar **perguntas que o público provavelmente tem** sobre o tema.
10. Identificar **momentos de virada** ou insights marcantes.

## Output Format

```
=== ANÁLISE TEOLÓGICA ===

Tema central: [frase]
Data da aula: [se informado]
Pastor: [se informado]

SUBTEMAS:
1. [subtema]
2. [subtema]
3. [subtema]

CITAÇÕES PODEROSAS:
1. "[citação]"
2. "[citação]"
...

REFERÊNCIAS BÍBLICAS:
- [livro cap:versículo] — [aplicação na aula]

APLICAÇÕES PRÁTICAS:
- [aplicação 1]
- [aplicação 2]

ARCO NARRATIVO:
Problema: [descrição]
Tensão: [descrição]
Solução/Esperança: [descrição]

PILAR EDITORIAL: [Fé / Transformação / Comunidade / Missão / Identidade]

PERGUNTAS DO PÚBLICO:
1. [pergunta]
2. [pergunta]
3. [pergunta]

MOMENTOS DE VIRADA:
- [insight 1]
- [insight 2]
```

## Veto Conditions

Rejeitar e refazer se:
1. Menos de 5 citações extraídas
2. Arco narrativo não identificado
3. Nenhuma aplicação prática listada
