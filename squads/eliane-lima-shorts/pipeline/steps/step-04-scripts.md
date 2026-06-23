---
execution: subagent
agent: squads/eliane-lima-shorts/agents/roteirista-rapido
format: youtube-shorts
model_tier: powerful
inputFile: squads/eliane-lima-shorts/output/clips-selecionados.md
outputFile: /Users/walmirjunior/aios-core/paginas-html/Editorial/roteiros-eliane-{YYYY-MM-DD}.html
---

# Step 03: Criação dos Roteiros (automático)

## Context Loading

Load these files before executing:
- `/Users/walmirjunior/aios-core/paginas-html/Editorial/cortes-eliane-{YYYY-MM-DD}.html` — apelidos e nomes de arquivo de cada clip (usar esses mesmos nomes no HTML de roteiros)
- `squads/eliane-lima-shorts/output/clips-selecionados.md` — 3 clips selecionados
- `squads/eliane-lima-shorts/pipeline/data/tone-of-voice.md` — 6 tons disponíveis
- `squads/eliane-lima-shorts/pipeline/data/output-examples.md` — exemplos de qualidade
- `squads/eliane-lima-shorts/pipeline/data/anti-patterns.md` — erros a evitar

## Instructions

### Process

1. Para cada um dos 3 clips, selecionar o tom mais adequado.
2. Escrever o hook completo (0–2s): máximo 12 palavras faladas.
3. Escrever a entrega completa: fala na íntegra, direção de câmera, overlays com timestamps.
4. Escrever o punchline/loop com CTA específico (canal Bellolhar ou agendamento).
5. Escrever título (≤70 chars), descrição (≤150 chars) e hashtags (3–5, incluindo #Shorts).
6. Estimar duração total (base: 130 palavras/min).
7. Entregar os 3 roteiros completos sem necessidade de aprovação.

## Output Format

Salvar como HTML em `/Users/walmirjunior/aios-core/paginas-html/Editorial/roteiros-eliane-{YYYY-MM-DD}.html`.
Usar o mesmo estilo visual dos outros HTMLs do Editorial (fundo cinza claro, cards brancos, header roxo).
**Cada card de roteiro deve exibir o apelido do clip em destaque no topo** (ex: "Cauterização de Verruga") — o mesmo apelido definido no HTML de cortes — para que qualquer pessoa saiba de qual corte aquele roteiro trata sem precisar abrir outro arquivo.
Cada roteiro em um card separado com seções visuais distintas para Hook, Delivery e Punchline.

Conteúdo base de cada roteiro:
```
=== ROTEIRO SHORT [N] ===

Tom selecionado: [nome]
Clip de origem: [timestamp — título]
Duração estimada: [X segundos]

HOOK (0-2s):
[Visual]: [o que aparece na tela]
[Audio]: [fala exata ou silêncio]
[Text Overlay]: [CAIXA ALTA, máx 8 palavras]

DELIVERY ([tempo]s):
[Visual]: [descrição]
[Script]: [fala completa — sem lacunas]
[Text Overlays]:
  [[X:XX]] "[texto]"
  [[X:XX]] "[texto]"
  [[X:XX]] "[texto]"

PUNCHLINE/LOOP ([tempo]s):
[Visual]: [cena final]
[Script]: [fala de encerramento]
[Text Overlay]: [CAIXA ALTA]

=== TITLE ===
[título ≤70 chars]

=== DESCRIPTION ===
[≤150 chars]

#Shorts #JatoDePlasma #ElianeLima #[hashtag] #[hashtag]

=== LOOP NOTE ===
[como o final conecta ao início]

=== AUDIO NOTE ===
[orientação de áudio]
```

## Veto Conditions

Reject and redo if ANY are true:
1. Algum roteiro tem "..." ou lacunas na fala
2. Algum roteiro tem menos de 3 text overlays
3. Algum roteiro não tem CTA com destino específico

## Quality Criteria

- [ ] 3 roteiros completos entregues
- [ ] Hook escrito completo nos primeiros 2s para cada roteiro
- [ ] Fala escrita na íntegra — sem lacunas
- [ ] Mínimo 3 text overlays por roteiro
- [ ] CTA com destino específico em todos
- [ ] Título ≤70 caracteres
- [ ] #Shorts incluído nas hashtags
- [ ] Duração estimada entre 30–55 segundos
