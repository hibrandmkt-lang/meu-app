---
execution: inline
agent: squads/john-knox-content/agents/compilador-html
format: html
inputFiles:
  - squads/john-knox-content/output/aula-input.md
  - squads/john-knox-content/output/analise-teologica.md
  - squads/john-knox-content/output/estrategia-editorial.md
  - squads/john-knox-content/output/posts-prontos.md
  - squads/john-knox-content/output/carrosseis.md
outputFile: /Users/walmirjunior/aios-core/Suporte/output/john-knox-{YYYY-MM-DD}.html
---

# Step 06: Compilação do Relatório HTML

## Context Loading

Carregar todos os outputs anteriores:
- `squads/john-knox-content/output/analise-teologica.md`
- `squads/john-knox-content/output/estrategia-editorial.md`
- `squads/john-knox-content/output/posts-prontos.md`
- `squads/john-knox-content/output/carrosseis.md`
- `squads/john-knox-content/pipeline/data/html-template.md` — guia de estilo visual

## Instructions

### Process

1. Ler todos os arquivos de output anteriores.
2. Obter a data atual no formato YYYY-MM-DD.
3. Compilar tudo em um único arquivo HTML com design profissional.
4. Salvar em `/Users/walmirjunior/aios-core/Suporte/output/john-knox-{DATA}.html`.

### HTML Structure

O HTML deve ter as seguintes seções, nesta ordem:

**Header**: título "Relatório de Conteúdo — John Knox", data, tema da aula
**Seção 1 — Análise da Aula**: tema, subtemas, arco narrativo, referências bíblicas
**Seção 2 — Citações Poderosas**: cards visuais com cada citação extraída
**Seção 3 — Linha Editorial**: linha editorial da semana + ângulos de conteúdo
**Seção 4 — Posts Prontos**: cada post em card separado com tipo indicado visualmente
**Seção 5 — Carrosséis**: cada carrossel com todos os slides detalhados
**Seção 6 — Hashtags e Calendário**: banco de hashtags + sugestão de calendário
**Footer**: data de geração, squad john-knox-content

### Design Visual

- Background: #1a1a2e (azul noturno escuro)
- Header: gradiente de #16213e a #0f3460
- Cards: #ffffff com borda sutil, sombra suave
- Accent color principal: #c9a227 (dourado)
- Accent color secundário: #4a90d9 (azul)
- Tipografia: Google Fonts — Playfair Display (títulos) + Inter (corpo)
- Citações: card especial com fundo azul escuro, texto dourado, fonte grande
- Posts: badge colorido por tipo (feed=verde, devocional=roxo, stories=laranja, citação=dourado)
- Carrosséis: cada slide como card numerado com borda esquerda colorida
- Responsivo: funciona em mobile e desktop
- Botão "copiar" em cada post (JavaScript simples)

### Quality Requirements

- Todo conteúdo dos steps anteriores DEVE aparecer no HTML
- Nenhuma seção pode estar vazia
- HTML deve abrir corretamente no browser sem dependências externas (exceto Google Fonts CDN)
- Usar Tailwind CDN ou CSS inline — sem arquivos externos locais

## Veto Conditions

Rejeitar e refazer se:
1. Alguma seção obrigatória está ausente
2. HTML tem erros de sintaxe
3. Posts não têm botão de cópia
4. Arquivo não salvo no caminho correto
