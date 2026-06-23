---
execution: subagent
agent: squads/eliane-lima-shorts/agents/extrator-elite
model_tier: fast
inputFile: squads/eliane-lima-shorts/output/video-input.md
outputFile: squads/eliane-lima-shorts/output/clips-selecionados.md
---

# Step 02: Extração e Seleção Automática de Clips

## Context Loading

Load these files before executing:
- `squads/eliane-lima-shorts/output/video-input.md` — conteúdo do vídeo longo
- `squads/eliane-lima-shorts/pipeline/data/domain-framework.md` — critérios de seleção
- `squads/eliane-lima-shorts/pipeline/data/anti-patterns.md` — erros a evitar

## Instructions

### Process

1. Ler o conteúdo completo de `video-input.md`.
2. Mapear todos os tópicos com timestamps.
3. Avaliar cada trecho pelos 4 critérios: autonomia, hook natural, completude, valor imediato.
4. Classificar cada clip aprovado por tipo.
5. Ranquear de ★★★★★ a ★★★☆☆ — descartar abaixo de ★★★.
6. **Selecionar automaticamente os 3 melhores clips** (★★★★★ ou ★★★★☆ prioritários), garantindo variedade de tipos para a semana (Dica / Procedimento / Mito-Verdade ou Depoimento).
7. O output final contém APENAS os 3 clips selecionados, prontos para roteirização — sem necessidade de aprovação do usuário.

## Output Format

```
=== CLIPS SELECIONADOS PARA ROTEIRIZAÇÃO ===

Vídeo: [título]
Seleção automática: 3 clips — variedade garantida

CLIP 1 — [TÍTULO]
Timestamp: [início] – [fim]
Tipo: [tipo]
Hook natural: "[frase]"
Conteúdo resumido: [2-3 linhas]
Qualidade: ★★★★★
Motivo da seleção: [razão]

CLIP 2 — [TÍTULO]
[mesma estrutura]

CLIP 3 — [TÍTULO]
[mesma estrutura]
```

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 3 clips selecionados
2. Todos os clips são do mesmo tipo (sem variedade)
3. Algum clip contém promessa médica inadequada

## Quality Criteria

- [ ] Exatamente 3 clips selecionados
- [ ] Variedade de tipos (no mínimo 2 tipos diferentes)
- [ ] Todos têm hook natural identificado
- [ ] Nenhum contém promessa médica inadequada
