# Codex LP制作スターター 配布サイト v2.0.2

Codex専用LINE登録特典「Codex LP制作スターター」の公開用静的サイトです。受取者側のインストールやローカルサーバー起動は不要です。2つのMarkdownを個別にダウンロード／コピーし、作業フォルダ指定、セットアップ送付、LP実装送付、対話ヒアリング、HTML/CSS/JSレスポンシブ実装、Codexによるpreview確認の6段階を案内します。Step 4から5へ進むには実装前プランの明示承認が必要です。

## ローカルプレビュー

```bash
cd /home/aru/projects/codex-lp-starter-site
python3 -m http.server 4173 --bind 127.0.0.1
```

ブラウザで <http://127.0.0.1:4173/> を開きます。停止は起動したterminalで Ctrl+C です。

## 構成

```text
.
├── index.html
├── help/index.html
├── changelog/index.html
├── privacy/index.html
├── 404.html
├── assets/styles.css
├── assets/site.js
├── assets/codex-ai-creator-logo.png
├── assets/セットアップ.md
├── assets/lp実装.md
├── assets/codex-lp-starter-v2.0.2.zip
└── scripts/check-site.py
```

## 実装上の境界

- Skill設置や5項目一括入力を主導線にしません。
- 2つのMarkdownを個別に取得・コピーでき、順番を明示します。
- JavaScript無効時も個別ファイル、ZIP、説明、主要リンクを利用できます。
- ページ上ではLPを生成せず、独自analyticsを接続しません。
- LP制作時のpreview serverはCodexが起動し、受取者へcommand実行を求めません。
- 「AIっぽい見た目」を、案件固有の根拠より装飾patternが優先される状態として説明し、架空実績や成果保証を使いません。
- 既存の正規ロゴをローカルassetとして継続使用します。外部font、CDN、framework、package dependencyはありません。

## 配布artifact

- File: `assets/codex-lp-starter-v2.0.2.zip`
- Version: `2.0.2`
- Size: `21274 bytes`
- SHA-256: `315e9b19e44377c10054299d215b288b1a7d061776b800fc0894f0639be368e1`

## 検証

```bash
cd /home/aru/projects/codex-lp-starter-site
python3 scripts/check-site.py
node --check assets/site.js
```

ローカルHTTP応答の確認：

```bash
python3 -m http.server 4173 --bind 127.0.0.1
curl -I http://127.0.0.1:4173/
curl -I http://127.0.0.1:4173/help/
curl -I http://127.0.0.1:4173/changelog/
curl -I http://127.0.0.1:4173/privacy/
curl -I http://127.0.0.1:4173/assets/セットアップ.md
curl -I http://127.0.0.1:4173/assets/lp実装.md
curl -I http://127.0.0.1:4173/assets/codex-lp-starter-v2.0.2.zip
```

実ブラウザでの最終認証は別担当が行います。320、390、768、1024、1440px、200% zoom、keyboard、Clipboard API、download UI、JavaScript-off、iOS Safari、Android Chrome、LINE内ブラウザは公開前の確認対象です。

## 公開後の確認事項

- ロゴ利用権、商標、サービス名称の表示条件
- LINEからPCへの再訪方法と実機browser確認
- 本番404設定、セキュリティヘッダー、キャッシュ方針
