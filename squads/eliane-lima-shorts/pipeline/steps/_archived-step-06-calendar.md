---
execution: inline
agent: squads/eliane-lima-shorts/agents/publicador-planejado
inputFile: squads/eliane-lima-shorts/output/roteiros-aprovados.md
outputFile: squads/eliane-lima-shorts/output/calendario-publicacao.md
---

# Step 06: Calendário de Publicação

## Context Loading

Load these files before executing:
- `squads/eliane-lima-shorts/output/roteiros-aprovados.md` — roteiros aprovados pelo usuário
- `squads/eliane-lima-shorts/pipeline/data/domain-framework.md` — cadência (Seg/Qua/Sex) e tipos por dia
- `squads/eliane-lima-shorts/pipeline/data/quality-criteria.md` — critérios de variedade semanal

## Instructions

### Process

1. Contar quantos roteiros foram aprovados e identificar o tipo de cada um (Dica / Procedimento / Resultado / Mito / Depoimento).
2. Definir a sequência semanal: educativo na Segunda, procedimento/visual na Quarta, resultado/depoimento na Sexta.
3. Calcular as próximas datas de Segunda, Quarta e Sexta a partir da data atual.
4. Para cada Short: atribuir data (09:00), nomear o arquivo com padrão `YYYY-MM-DD-tipo-tema-eliane.mp4`.
5. Gerar checklist completo de edição e publicação para cada Short.
6. Entregar o calendário formatado visualmente por semana.

## Output Format

```
=== CALENDÁRIO EDITORIAL — CANAL ELIANE LIMA SHORTS ===
Semana de [data início] a [data fim]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[DIA DA SEMANA] — DD/MM/AAAA às 09:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Short: "[título]"
Tipo: [tipo]
Arquivo: YYYY-MM-DD-tipo-tema-eliane.mp4
Origem: Canal Bellolhar — [vídeo] — [timestamp]

Checklist de Edição:
  [ ] Cortar trecho [timestamp] do vídeo original
  [ ] Converter para formato vertical 9:16
  [ ] Adicionar text overlays conforme roteiro
  [ ] Ativar legenda automática
  [ ] Exportar como MP4 com nome correto

Checklist de Publicação (YouTube Studio):
  [ ] Canal selecionado: Eliane Lima (não Bellolhar)
  [ ] Título digitado: "[título exato]"
  [ ] Descrição com #Shorts na primeira linha
  [ ] Hashtags adicionadas
  [ ] Agendamento confirmado: DD/MM/AAAA às 09:00

[repetir para cada slot da semana]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMO DA SEMANA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total de Shorts: [N]
Tipos na semana: [lista sem repetição]
Próxima sessão sugerida: [data para produzir a próxima semana]
```

## Output Example

```
=== CALENDÁRIO EDITORIAL — CANAL ELIANE LIMA SHORTS ===
Semana de 21 a 25 de Abril de 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEGUNDA — 21/04/2026 às 09:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Short: "Fez plasma e a mancha voltou? Provavelmente foi isso"
Tipo: Dica Rápida / Educativo
Arquivo: 2026-04-21-dica-protetor-solar-eliane.mp4
Origem: Canal Bellolhar — "Tratamento Completo de Melasma" — 02:14 a 02:58

Checklist de Edição:
  [ ] Cortar trecho 02:14–02:58 do vídeo original
  [ ] Converter para formato vertical 9:16 (reframing no CapCut ou Premiere)
  [ ] Adicionar text overlay: "SE NÃO USAR PROTETOR, PERDE TUDO" (0–2s)
  [ ] Adicionar text overlay: "pele em reconstrução por 30 dias" (0:05)
  [ ] Adicionar text overlay: "FPS 50 — obrigatório por 30 dias" (0:30)
  [ ] Adicionar text overlay: "PROTOCOLO COMPLETO = RESULTADO GARANTIDO" (final)
  [ ] Ativar legenda automática no CapCut
  [ ] Exportar como MP4: 2026-04-21-dica-protetor-solar-eliane.mp4

Checklist de Publicação (YouTube Studio):
  [ ] Canal selecionado: Eliane Lima (não confundir com Bellolhar)
  [ ] Título: "Fez plasma e a mancha voltou? Provavelmente foi isso"
  [ ] Descrição: "O protetor solar não é opcional no pós-plasma. #Shorts #JatoDePlasma #ElianeLima #Estética #CuidadosDaPele"
  [ ] Agendamento: 21/04/2026 às 09:00

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUARTA — 23/04/2026 às 09:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Short: "Olha o que acontece com a pele durante o plasma"
Tipo: Procedimento
Arquivo: 2026-04-23-procedimento-reacao-pele-eliane.mp4
Origem: Canal Bellolhar — "Tratamento Completo de Melasma" — 07:30 a 08:10
[...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMO DA SEMANA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total de Shorts: 3
Tipos na semana: Dica Rápida / Procedimento / Antes-Depois
Próxima sessão sugerida: 28/04/2026 (pegar novo vídeo do Bellolhar)
```

## Veto Conditions

Reject and redo if ANY are true:
1. Algum slot não tem checklist completo de edição e publicação
2. Canal de publicação não está especificado como "Eliane Lima" em cada slot

## Quality Criteria

- [ ] 3 slots preenchidos (Seg / Qua / Sex)
- [ ] Cada slot tem data, hora, arquivo nomeado e dois checklists
- [ ] Variedade de tipo na semana confirmada
- [ ] Canal "Eliane Lima" especificado em todos os slots
- [ ] Data da próxima sessão sugerida no resumo
