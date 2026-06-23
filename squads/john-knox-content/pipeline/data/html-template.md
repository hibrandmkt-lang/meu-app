# Guia de Estilo HTML — John Knox Content

## Paleta de Cores

```css
--bg-primary: #0d1117;
--bg-surface: #161b22;
--bg-surface-light: #21262d;
--accent-gold: #d4a017;
--accent-blue: #388bfd;
--accent-purple: #bc8cff;
--accent-green: #3fb950;
--accent-orange: #f0883e;
--text-primary: #e6edf3;
--text-secondary: #8b949e;
--border: #30363d;
```

## Typography

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

- H1 (header do relatório): Playfair Display 700, 2.5rem
- H2 (título de seção): Playfair Display 700, 1.75rem, cor dourada
- H3 (subtítulo de card): Inter 600, 1.1rem
- Corpo: Inter 400, 0.95rem, line-height 1.7
- Citações: Playfair Display italic, 1.2rem, cor dourada
- Labels/badges: Inter 500, 0.75rem, uppercase, letter-spacing

## Badges por Tipo de Post

```css
.badge-feed    { background: #1a4731; color: #3fb950; border: 1px solid #3fb950; }
.badge-devocional { background: #2d1b4e; color: #bc8cff; border: 1px solid #bc8cff; }
.badge-stories { background: #4a2009; color: #f0883e; border: 1px solid #f0883e; }
.badge-citacao { background: #3d2e00; color: #d4a017; border: 1px solid #d4a017; }
```

## Botão de Cópia

```html
<button onclick="copyPost('post-id')" class="copy-btn">
  Copiar
</button>
```

```css
.copy-btn {
  background: #21262d;
  color: #8b949e;
  border: 1px solid #30363d;
  border-radius: 6px;
  padding: 4px 12px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.2s;
}
.copy-btn:hover { border-color: #388bfd; color: #388bfd; }
```

## Card de Post

```html
<div class="post-card" style="border-left: 3px solid #3fb950;">
  <div class="post-header">
    <span class="badge badge-feed">FEED</span>
    <button onclick="copyPost('post-1')" class="copy-btn">Copiar</button>
  </div>
  <div id="post-1" class="post-text">
    [conteúdo do post]
  </div>
</div>
```

## Card de Slide de Carrossel

```html
<div class="slide-card">
  <div class="slide-number">01</div>
  <div class="slide-content">
    <p class="slide-main-text">[texto principal]</p>
    <p class="slide-secondary-text">[texto secundário]</p>
    <span class="slide-design-badge">[instrução de design]</span>
  </div>
</div>
```

## Navegação Fixa

```html
<nav class="fixed-nav">
  <a href="#topo">Topo</a>
  <a href="#analise">Análise</a>
  <a href="#editorial">Editorial</a>
  <a href="#posts">Posts</a>
  <a href="#carrosseis">Carrosséis</a>
  <a href="#hashtags">Hashtags</a>
</nav>
```

## Responsividade

```css
@media (max-width: 768px) {
  .grid-2col { grid-template-columns: 1fr; }
  h1 { font-size: 1.8rem; }
  .fixed-nav a { font-size: 0.75rem; padding: 4px 8px; }
}
```

## Exemplo de Seção Completa

```html
<section id="posts" class="section">
  <h2 class="section-title">Posts Prontos</h2>
  <p class="section-subtitle">8 posts prontos para publicar — clique em Copiar para usar</p>
  
  <div class="posts-grid">
    <!-- cards de posts aqui -->
  </div>
</section>
```
