---
execution: inline
agent: squads/eliane-lima-shorts/agents/publicador-planejado
inputFile: /Users/walmirjunior/aios-core/paginas-html/Editorial/roteiros-eliane-{YYYY-MM-DD}.html
outputFile: /Users/walmirjunior/aios-core/paginas-html/Editorial/calendario-eliane-{YYYY-MM-DD}.html
---

# Step 04: Calendário de Publicação (automático)

## Context Loading

Load these files before executing:
- `squads/eliane-lima-shorts/output/roteiros-shorts.md` — 3 roteiros prontos
- `squads/eliane-lima-shorts/pipeline/data/domain-framework.md` — cadência Seg/Qua/Sex
- `squads/eliane-lima-shorts/pipeline/data/quality-criteria.md` — critérios de variedade

## Instructions

### Process

1. Ler os 3 roteiros e identificar o tipo de cada um.
2. Definir sequência: educativo na Segunda, procedimento/visual na Quarta, resultado/mito na Sexta.
3. Calcular próximas datas de Segunda, Quarta e Sexta a partir da data atual.
4. Para cada Short: atribuir data (09:00), nomear arquivo `YYYY-MM-DD-tipo-tema-eliane.mp4`.
5. Gerar checklist completo de edição e publicação por Short.
6. Entregar calendário formatado — sem necessidade de aprovação.

## Output Format

Salvar como HTML em `/Users/walmirjunior/aios-core/paginas-html/Editorial/calendario-eliane-{YYYY-MM-DD}.html`.
Usar o mesmo estilo visual dos outros HTMLs do Editorial (fundo cinza claro, cards brancos).
**Cada slot de publicação deve exibir o apelido do clip** (ex: "Cauterização de Verruga") e o nome do arquivo mp4 sugerido — os mesmos definidos no HTML de cortes — para fechar o ciclo: quem olha o calendário sabe exatamente qual arquivo cortar e publicar.
Cada slot da semana em um card com checklist interativo (checkboxes HTML funcionais).

Conteúdo base:
```
=== CALENDÁRIO EDITORIAL — CANAL ELIANE LIMA SHORTS ===
Semana de [data início] a [data fim]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[DIA] — DD/MM/AAAA às 09:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Short: "[título]"
Tipo: [tipo]
Arquivo: YYYY-MM-DD-tipo-tema-eliane.mp4
Origem: Canal Bellolhar — [timestamp]

Checklist de Edição:
  [ ] Cortar trecho [timestamp] do vídeo original
  [ ] Converter para formato vertical 9:16
  [ ] Adicionar text overlays conforme roteiro
  [ ] Ativar legenda automática
  [ ] Exportar como MP4 com nome correto

Checklist de Publicação (YouTube Studio):
  [ ] Canal: Eliane Lima (não Bellolhar)
  [ ] Título: "[título exato]"
  [ ] Descrição com #Shorts na primeira linha
  [ ] Hashtags adicionadas
  [ ] Agendamento: DD/MM/AAAA às 09:00

[repetir para cada slot]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total de Shorts: 3
Próxima sessão sugerida: [data]
```

## Veto Conditions

Reject and redo if ANY are true:
1. Algum slot não tem checklist completo de edição e publicação
2. Canal de publicação não está especificado como "Eliane Lima" em cada slot

## Quality Criteria

- [ ] 3 slots preenchidos (Seg / Qua / Sex)
- [ ] Cada slot tem data, hora, arquivo nomeado e dois checklists
- [ ] Canal "Eliane Lima" em todos os slots
- [ ] Próxima sessão sugerida no resumo
