---
execution: inline
agent: squads/eliane-lima-shorts/agents/cortador-automatico
model_tier: fast
inputFile: squads/eliane-lima-shorts/output/clips-selecionados.md
outputFile: /Users/walmirjunior/aios-core/paginas-html/Editorial/cortes-eliane-{YYYY-MM-DD}.html
---

# Step 03: Script de Cortes (sem execução automática)

## Context Loading

Load before executing:
- `squads/eliane-lima-shorts/output/clips-selecionados.md` — 3 clips com timestamps e URL do vídeo

## Instructions

### Process

1. Extrair do arquivo de input:
   - URL do vídeo original (Bellolhar)
   - Para cada clip: timestamp início, timestamp fim, tipo, título descritivo

2. Para cada clip, definir primeiro um **apelido curto em português** (2–4 palavras, ex: "cauterização de verruga", "plasma no quisto"). Esse apelido é o fio condutor que conecta os 3 HTMLs — o roteiro e o calendário vão referenciar os clips por esse nome.
3. Para cada clip, gerar:
   - **Apelido** (português claro, 2–4 palavras) — exibido em destaque no card
   - Nome do arquivo sugerido: `YYYY-MM-DD-{apelido-kebab}-eliane.mp4` (derivado do apelido)
   - Comando ffmpeg completo pronto para copiar e colar
   - Descrição curta do clip (para uso no YouTube)
   - Observações de edição (texto de overlay, punchline etc.)

3. Gerar arquivo HTML completo em:
   `/Users/walmirjunior/aios-core/paginas-html/Editorial/cortes-eliane-{YYYY-MM-DD}.html`

### NÃO executar
- **NÃO** baixar o vídeo com yt-dlp
- **NÃO** rodar ffmpeg
- **NÃO** criar pastas de cache
- Apenas gerar o HTML com o roteiro de cortes

## Output Format (HTML)

Gerar um arquivo HTML completo e bonito com este template:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Roteiro de Cortes — Eliane Lima Shorts — {DATA}</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f4f4f5; color: #18181b; padding: 2rem; }
    h1 { font-size: 1.6rem; font-weight: 700; margin-bottom: 0.25rem; }
    .meta { color: #71717a; font-size: 0.9rem; margin-bottom: 2rem; }
    .clip-card { background: #fff; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; box-shadow: 0 1px 4px rgba(0,0,0,0.08); border-left: 4px solid #6366f1; }
    .clip-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem; }
    .clip-num { background: #6366f1; color: white; border-radius: 50%; width: 2rem; height: 2rem; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; flex-shrink: 0; }
    .clip-title { font-size: 1.1rem; font-weight: 600; }
    .clip-type { font-size: 0.75rem; background: #ede9fe; color: #6366f1; padding: 0.2rem 0.6rem; border-radius: 99px; font-weight: 500; }
    .row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem; }
    .field label { font-size: 0.75rem; font-weight: 600; color: #71717a; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.25rem; }
    .field .value { font-size: 0.95rem; color: #18181b; }
    .field .value a { color: #6366f1; text-decoration: none; }
    .timestamps { display: flex; gap: 0.5rem; align-items: center; }
    .ts { background: #f4f4f5; padding: 0.3rem 0.75rem; border-radius: 6px; font-family: monospace; font-size: 1rem; font-weight: 600; }
    .arrow { color: #71717a; }
    .filename { font-family: monospace; font-size: 0.85rem; background: #f4f4f5; padding: 0.4rem 0.75rem; border-radius: 6px; word-break: break-all; }
    .cmd-block { margin-top: 1rem; }
    .cmd-block label { font-size: 0.75rem; font-weight: 600; color: #71717a; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.5rem; }
    pre { background: #18181b; color: #a3e635; padding: 1rem; border-radius: 8px; font-size: 0.8rem; overflow-x: auto; white-space: pre-wrap; word-break: break-all; line-height: 1.6; }
    .desc-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 0.75rem 1rem; margin-top: 1rem; font-size: 0.9rem; line-height: 1.5; }
    .obs-box { background: #fefce8; border: 1px solid #fde68a; border-radius: 8px; padding: 0.75rem 1rem; margin-top: 0.75rem; font-size: 0.85rem; line-height: 1.5; }
    .obs-box strong { display: block; margin-bottom: 0.25rem; color: #92400e; font-size: 0.75rem; text-transform: uppercase; }
    .footer { margin-top: 2rem; text-align: center; color: #a1a1aa; font-size: 0.8rem; }
    @media print { body { background: white; } .clip-card { box-shadow: none; border: 1px solid #e4e4e7; } }
  </style>
</head>
<body>
  <h1>✂️ Roteiro de Cortes — Canal Eliane Lima Shorts</h1>
  <p class="meta">Vídeo de origem: <a href="{URL_VIDEO}">{URL_VIDEO}</a> &nbsp;|&nbsp; Gerado em {DATA}</p>

  <!-- CLIP 1 -->
  <div class="clip-card">
    <div class="clip-header">
      <div class="clip-num">1</div>
      <div class="clip-title">{TITULO_CLIP_1}</div>
      <span class="clip-type">{TIPO_CLIP_1}</span>
    </div>
    <div class="row">
      <div class="field">
        <label>Corte</label>
        <div class="timestamps">
          <span class="ts">{INICIO_1}</span>
          <span class="arrow">→</span>
          <span class="ts">{FIM_1}</span>
        </div>
      </div>
      <div class="field">
        <label>Nome do arquivo</label>
        <div class="filename">{FILENAME_1}</div>
      </div>
    </div>
    <div class="cmd-block">
      <label>Comando ffmpeg (copiar e colar no terminal)</label>
      <pre>yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" \
  --merge-output-format mp4 \
  -o "~/Downloads/{FILENAME_1_SEM_EXT}-original.mp4" \
  {URL_VIDEO}

ffmpeg -ss {INICIO_1} -to {FIM_1} \
  -i "~/Downloads/{FILENAME_1_SEM_EXT}-original.mp4" \
  -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920" \
  -c:v libx264 -preset fast -crf 23 \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  -y "~/Downloads/{FILENAME_1}"</pre>
    </div>
    <div class="desc-box">📝 <strong>Descrição YouTube:</strong> {DESCRICAO_1}</div>
    <div class="obs-box"><strong>⚡ Observações de edição</strong>{OBSERVACOES_1}</div>
  </div>

  <!-- CLIP 2 — mesma estrutura -->
  <!-- CLIP 3 — mesma estrutura -->

  <div class="footer">Eliane Lima Shorts · Gerado por AIOS Squad · {DATA}</div>
</body>
</html>
```

Preencher todos os valores reais extraídos de `clips-selecionados.md`.
Salvar o arquivo em `/Users/walmirjunior/aios-core/paginas-html/Editorial/` com nome `cortes-eliane-{YYYY-MM-DD}.html`.

## Veto Conditions

Reject and redo if ANY are true:
1. HTML gerado não contém os 3 clips
2. Algum clip está sem comando ffmpeg completo
3. Arquivo salvo fora de `paginas-html/Editorial/`

## Quality Criteria

- [ ] HTML salvo em `/Users/walmirjunior/aios-core/paginas-html/Editorial/`
- [ ] 3 clips com timestamps corretos
- [ ] 3 comandos ffmpeg completos e prontos para copiar
- [ ] 3 nomes de arquivo sugeridos no padrão YYYY-MM-DD-tipo-tema-eliane.mp4
- [ ] 3 descrições para YouTube
- [ ] HTML abre corretamente no navegador
