# Meta Ads — Campanhas de Distribuição
**Conta:** Revit - Conta Oficial (Rafael Zaccari)
**Ad Account:** `234097094341643`
**Data de criação:** 13/06/2026

---

## Campanha 1 — TOPO
**Nome:** `Dist. | br | topo`
**ID:** `120245091903630570`
**Objetivo:** OUTCOME_ENGAGEMENT
**Orçamento:** ABO — R$6,00/dia por conjunto
**Otimização:** POST_ENGAGEMENT
**Destino:** ON_POST
**Targeting:** Brasil | Cargo: Engineer (work_positions)
**Status:** PAUSADO (ativar quando adicionar criativos)

> ⚠️ **Ação necessária:** Adicionar cargo **Arquiteto** manualmente em cada conjunto.
> Ads Manager → Conjunto → Targeting → Job Title → pesquisar "Arquiteto"

| # | Conjunto | Reel (shortcode) | Ad Set ID |
|---|----------|-----------------|-----------|
| 1 | [TOPO] DW6EFM6jWic | engenheiros/arquitetos \| BR | 120245092005890570 |
| 2 | [TOPO] DXKe1_njbQK | engenheiros/arquitetos \| BR | 120245092048210570 |
| 3 | [TOPO] DXZ7htrgcHC | engenheiros/arquitetos \| BR | 120245092049940570 |
| 4 | [TOPO] DXcgmHjD3a5 | engenheiros/arquitetos \| BR | 120245092052780570 |
| 5 | [TOPO] DXxGxc1DLp0 | engenheiros/arquitetos \| BR | 120245092054310570 |
| 6 | [TOPO] DXr9GjsAVGC | engenheiros/arquitetos \| BR | 120245092056160570 |
| 7 | [TOPO] DY0DjBeDjJk | engenheiros/arquitetos \| BR | 120245092061440570 |
| 8 | [TOPO] DXuiCx2ETk0 | engenheiros/arquitetos \| BR | 120245092063220570 |
| 9 | [TOPO] DXq_6KwiJwC | engenheiros/arquitetos \| BR | 120245092065190570 |
| 10 | [TOPO] DW7CSdSjB4a | engenheiros/arquitetos \| BR | 120245092066040570 |

---

## Campanha 2 — RMKT
**Nome:** `Dist. | br | rmkt 365d`
**ID:** `120245091913790570`
**Objetivo:** OUTCOME_ENGAGEMENT
**Orçamento:** ABO — R$6,00/dia por conjunto
**Otimização:** POST_ENGAGEMENT
**Destino:** ON_POST
**Targeting:** Brasil | Custom Audience: [IG] Envolvimento - 365D (`120245083726010570`)
**Status:** PAUSADO (ativar quando adicionar criativos)

| # | Conjunto | Reel (shortcode) | Ad Set ID |
|---|----------|-----------------|-----------|
| 1 | [RMKT] DZU03nTEX5k | IG envolvimento 365d \| BR | 120245092074420570 |
| 2 | [RMKT] DXEXjYAjkxk | IG envolvimento 365d \| BR | 120245092075640570 |
| 3 | [RMKT] DZVoyjtkpwI | IG envolvimento 365d \| BR | 120245092076900570 |
| 4 | [RMKT] DX7VFTQIX6g | IG envolvimento 365d \| BR | 120245092077900570 |
| 5 | [RMKT] DZYGawADvV6 | IG envolvimento 365d \| BR | 120245092078790570 |
| 6 | [RMKT] DXH6JZgiRY9 | IG envolvimento 365d \| BR | 120245092080880570 |
| 7 | [RMKT] DXwfPw0InRe | IG envolvimento 365d \| BR | 120245092081840570 |
| 8 | [RMKT] DYcMLrDxJ05 | IG envolvimento 365d \| BR | 120245092082640570 |
| 9 | [RMKT] DYpwgUJCYAP | IG envolvimento 365d \| BR | 120245092084410570 |
| 10 | [RMKT] DZdQKBNGov6 | IG envolvimento 365d \| BR | 120245092087720570 |

---

## Entidades de suporte

| Entidade | Nome | ID |
|----------|------|----|
| Custom Audience | [IG] Envolvimento - 365D | 120245083726010570 |
| Page ID (promoted_object) | Revit - Conta Oficial | 107373191713794 |
| IG Business ID | @rafaelzaccari | 3754303454669775 |

---

## Checklist para ativar as campanhas

### Para cada conjunto do TOPO
- [ ] Adicionar cargo "Arquiteto" no targeting (Job Title)
- [ ] Criar anúncio → "Usar publicação existente" → colar URL do reel (`https://www.instagram.com/p/{shortcode}/`)
- [ ] Revisar preview do anúncio

### Para cada conjunto do RMKT
- [ ] Criar anúncio → "Usar publicação existente" → colar URL do reel (`https://www.instagram.com/p/{shortcode}/`)
- [ ] Revisar preview do anúncio

### Final
- [ ] Ativar os conjuntos (mudar status de PAUSADO para ATIVO)
- [ ] Arquivar campanha antiga: `120245083731540570` (Dist. | br | rmkt 365d Feed Test)

---

## Observações técnicas

- **Targeting como sinal:** A Meta ativou automaticamente o Advantage+ Audience (`targeting_as_signal: 3`), o que significa que o cargo de Engineer é tratado como sinal, não restrição rígida. O Meta pode expandir o alcance além dos engenheiros se julgar relevante.
- **Criativos orgânicos via API:** A API bloqueia o uso de `instagram_media_id` para posts orgânicos (erro 2875108). Os reels precisam ser vinculados manualmente via Ads Manager usando "Usar publicação existente".
- **Sem exclusão de público:** Configurado sem nenhum `excluded_custom_audiences`, conforme solicitado.
