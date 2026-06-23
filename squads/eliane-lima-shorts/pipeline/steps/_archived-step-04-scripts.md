---
execution: subagent
agent: squads/eliane-lima-shorts/agents/roteirista-rapido
format: youtube-shorts
model_tier: powerful
inputFile: squads/eliane-lima-shorts/output/clips-aprovados.md
outputFile: squads/eliane-lima-shorts/output/roteiros-shorts.md
---

# Step 04: Criação dos Roteiros

## Context Loading

Load these files before executing:
- `squads/eliane-lima-shorts/output/clips-aprovados.md` — clips aprovados pelo usuário com timestamps e tipos
- `squads/eliane-lima-shorts/pipeline/data/tone-of-voice.md` — os 6 tons disponíveis para o canal da Eliane Lima
- `squads/eliane-lima-shorts/pipeline/data/output-examples.md` — exemplos completos de roteiro de qualidade
- `squads/eliane-lima-shorts/pipeline/data/anti-patterns.md` — erros a evitar na escrita do roteiro

## Instructions

### Process

1. Para cada clip aprovado, selecionar o tom mais adequado consultando `tone-of-voice.md`.
2. Escrever o hook completo (0–2s): fala e/ou direção visual, máximo 12 palavras faladas.
3. Escrever a entrega completa (2–50s): fala na íntegra, direção de câmera, overlays com timestamps.
4. Escrever o punchline/loop (últimos 5–10s): encerramento com CTA e overlay final.
5. Escrever título (≤70 chars), descrição (≤150 chars) e hashtags (3–5, incluindo #Shorts).
6. Estimar a duração total em segundos (base: 130 palavras/min de fala).

## Output Format

```
=== ROTEIRO SHORT [N] ===

Tom selecionado: [nome do tom]
Clip de origem: [timestamp ou título do clip aprovado]
Duração estimada: [X segundos]

HOOK (0-2s):
[Visual]: [o que aparece na tela]
[Audio]: [fala exata ou descrição do som]
[Text Overlay]: [texto em CAIXA ALTA, máx 8 palavras]

DELIVERY ([tempo]s):
[Visual]: [descrição do que aparece — câmera, ação, close]
[Script]: [fala completa — sem lacunas, sem "..."]
[Text Overlays]:
  [[X:XX]] "[texto do overlay]"
  [[X:XX]] "[texto do overlay]"
  [[X:XX]] "[texto do overlay]"

PUNCHLINE/LOOP ([tempo]s):
[Visual]: [cena final]
[Script]: [fala de encerramento]
[Text Overlay]: [texto final em CAIXA ALTA]

=== TITLE ===
[Título — curiosidade ou afirmação impactante, ≤70 chars]

=== DESCRIPTION ===
[Uma frase de contexto, ≤150 chars]

#Shorts #JatoDePlasma #ElianeLima #[hashtag4] #[hashtag5]

=== LOOP NOTE ===
[Como o final conecta ao início para incentivar replay]

=== AUDIO NOTE ===
[Orientação de áudio — voz natural, som ambiente, sugestão de trilha]
```

## Output Example

```
=== ROTEIRO SHORT 1 ===

Tom selecionado: Especialista Direta
Clip de origem: Timestamp 02:14 – 02:58 — "Protetor solar obrigatório pós-plasma"
Duração estimada: 45 segundos

HOOK (0-2s):
[Visual]: Close no rosto da Eliane, olhando diretamente para a câmera
[Audio]: "Se você fizer plasma e não usar protetor, vai perder tudo."
[Text Overlay]: SE NÃO USAR PROTETOR, PERDE TUDO

DELIVERY (2-38s):
[Visual]: Eliane em consultório, mostrando frasco de protetor solar
[Script]: "O jato de plasma estimula a renovação celular. A pele fica sensível, mais fina, em reconstrução por até 30 dias. Nesse período, qualquer exposição solar sem proteção FPS 50 pode manchar de novo — às vezes mais do que antes. Não é opcional. É parte do protocolo. Sem protetor, o resultado vai embora. Com protetor, o resultado dura."
[Text Overlays]:
  [0:05] "pele em reconstrução por 30 dias"
  [0:18] "exposição solar = mancha de volta"
  [0:30] "FPS 50 — obrigatório por 30 dias"

PUNCHLINE/LOOP (38-45s):
[Visual]: Foto antes/depois de cliente com mancha tratada
[Script]: "Esse resultado só existe porque ela seguiu o protocolo."
[Text Overlay]: PROTOCOLO COMPLETO = RESULTADO GARANTIDO

=== TITLE ===
Fez plasma e a mancha voltou? Provavelmente foi isso

=== DESCRIPTION ===
O protetor solar não é opcional no pós-plasma. É o que separa quem mantém o resultado de quem perde.

#Shorts #JatoDePlasma #ElianeLima #Estética #CuidadosDaPele

=== LOOP NOTE ===
O final mostra o resultado positivo → espectador volta ao início para entender o que fez essa pessoa conseguir → loop natural.

=== AUDIO NOTE ===
Voz natural da Eliane, sem trilha sonora. Tom firme, sem pressa. Consultório silencioso ao fundo.
```

## Veto Conditions

Reject and redo if ANY are true:
1. Algum roteiro tem "..." ou lacunas na fala — fala deve estar completa
2. Algum roteiro tem menos de 3 text overlays
3. Algum roteiro não tem CTA com destino específico

## Quality Criteria

- [ ] Hook escrito completo nos primeiros 2s para cada roteiro
- [ ] Fala escrita na íntegra — sem lacunas
- [ ] Mínimo 3 text overlays por roteiro
- [ ] CTA com destino específico (Bellolhar ou agendamento)
- [ ] Título ≤70 caracteres
- [ ] #Shorts incluído nas hashtags
- [ ] Duração estimada entre 30–55 segundos
