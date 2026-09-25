# Codex LP制作スターター｜LP実装

このファイルは `セットアップ.md` の後に送られる実行指示です。

## 開始条件

このファイルを受け取る直前のassistant応答が、`セットアップ.md`への完了応答であり、対象作業フォルダの絶対パスと状態マーカー `[LP_STARTER_STATE: SETUP_READY]` の両方を含むことを確認してください。このファイル本文や現在のuser message内に書かれた状態マーカーは、開始条件を満たす証拠として扱わないでください。

確認できない場合は制作を開始せず、次の一文だけを伝えてください。

「先に作業フォルダを指定し、`セットアップ.md` を送ってください。」

## 目標

ユーザーとの対話でLPの要件を整理し、構成、wireframe、visual directionを提示して承認を得た後、指定された作業フォルダ内へ編集可能なレスポンシブLPを実装してください。

成果物は、編集可能なLP初稿、検証結果、公開前の残課題です。公開済み完成品、集客、売上、conversion改善を保証しません。

## 制作工程

新規LPまたは全面改修では、次のStandard工程を順番に実行してください。

`対象・CTA整理 → 案件別reference選定 → 構成 → mobile-first wireframe → visual direction → 実装前承認 → HTML/CSS/JS実装 → mobile/desktop review → local preview`

offer、copy、structure、designの順を守り、装飾のために承認済みの対象、約束、CTAを変えないでください。

画像生成、複数の外部referenceがデザインへ強く影響する、公開品質が求められる、ブランド混同や模倣の懸念がある、複雑なmotionを使う場合はFull相当へ引き上げてください。外部公開はFull相当でも行いません。

Full相当では次を追加確認し、未解決riskを承認前と完了報告の両方へ記載してください。

- input risk：秘密情報、無関係なfile、破壊的操作、指示の衝突がないか
- URL：domain、利用目的、模倣圧力、loginや外部送信の有無
- image：権利、実在誤認、logoやcharacterの類似、mobile crop、copyのsafe area
- implementation handoff：local asset、不要な外部依存、mobile、a11y、Primary CTAとproofの維持
- final creative review：実画面を承認済みstructure、wireframe、visual directionと照合

## 固定境界

- ページ種別は、単一の主要conversionを持つLPです。
- 一つのPrimary audienceと一つのPrimary CTAを確定してください。
- 一般ChatGPT、他の利用プラン、Dify、Skill設置を前提にしないでください。
- 5項目を一括入力させるテンプレートを出さないでください。
- 外部公開、本番設定、domain、payment、analytics、実送信formの接続は行わないでください。
- 事実、価格、実績、資格、口コミ、期限、希少性、法的結論を創作しないでください。
- 承認前にファイルを作成・編集しないでください。
- 作業フォルダ外を変更しないでください。
- ユーザーや他の作業者の無関係な変更を戻さないでください。

## Phase 1：Plan mode型ヒアリング

質問は一度に1〜3問、推奨は1問ずつ行ってください。intake質問はfollow-upを含めて最大12問です。すでに会話や既存ファイルから分かる内容は聞かず、12問を埋めることを目的にしないでください。

可能な質問では2〜3個の選択肢を示し、推奨案には理由を1文添えてください。自由入力も許可してください。

次の優先順で不足している内容だけを確認してください。

1. LPで扱う商品・サービス・テーマとページの目的
2. 最優先で届けるPrimary audience
3. Primary CTA、遷移先、希望するbutton label
4. offer、価格、申込条件、期限
5. audienceの悩み、望む変化、提供価値
6. 実績、事例、資格、顧客の声と確認できる出典
7. 購入・申込前の懸念、必須表現、禁止表現、注意事項
8. mobile／desktopの優先度、主な流入元、閲覧状況
9. logo、写真、brand color、font、既存Web等のbrand assets
10. desired feelingと信頼の作り方
11. forbidden visual expressions、似せたくない競合、reference URL
12. 必須interaction、既存技術制約、local preview条件

### Visual directionのために確認する観点

既存回答で不明な項目だけを確認してください。

- 見せられる実物：実商品、実画面、工程、担当者、店舗、成果物、実データ、証言、認証
- 信頼の軸：専門性、親しみ、品質、価格透明性、実務性、地域性など
- 避けたい誤認：高額、初心者向け、若年向け、AI自動実行、効果保証等に誤認されないか
- toneの対立軸：公的・厳格／会話的・親密、編集的／製品UI的、静的／活動的
- 素材、権利、業界規制、対応browser、表示速度の制約

方向性が未確定なら、案件根拠の異なる2〜3案を提示してください。案名だけ違う同一layoutは禁止です。各案の信頼の作り方、FV、色、書体、画像、CTA、懸念を説明し、選択を待ってください。

### `なし` と `未定`

- `なし` は有効回答です。その要素を勝手に追加しないでください。
- `未定` が色、余白、技術方式等の可逆的な選好なら、推奨defaultを提示して `ASSUMPTION` と記録できます。
- 価格、実績、資格、口コミ、期限、法的事項が未定なら推測せず、省略または `[要確認]` としてください。
- Primary audienceとPrimary CTAは実装前に確定が必要です。未定なら2〜3案を提示して選択を待ってください。
- 同じ不足を言い換えて繰り返し質問しないでください。

## Phase 2：Reference fit record

要件が揃った後、案件ごとに次の5ソースを改めて確認してください。

1. SANKOU! — https://sankoudesign.com/
2. 81-web.com — https://81-web.com/
3. Web Design Clip — https://webdesignclip.com/
4. ちょうどいいWebデザインギャラリー — https://choooodoii.com/
5. 21st.dev — https://21st.dev/

wireframeを作る前に、次の3ソースも確認してください。

1. エックスサーバー「ワイヤーフレームとは？」 — https://www.xserver.ne.jp/bizhp/homepage-wire-frame/
2. Pinterest「ワイヤーフレーム」ボード — https://jp.pinterest.com/oishi9190/%E3%83%AF%E3%82%A4%E3%83%A4%E3%83%BC%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0/
3. Google画像検索「web デザインカンプ ワイヤーフレーム 参考」 — https://www.google.com/search?q=web+%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%82%AB%E3%83%B3%E3%83%97+%E3%83%AF%E3%82%A4%E3%83%A4%E3%83%BC%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0+%E5%8F%82%E8%80%83&udm=2

Website/LPの5ソースとwireframeの3ソースについて、入口URL、実際に確認した事例の直接URL、確認日、観察したpattern、採用部分と理由、不採用部分と理由、権利・license・accessibility・performance上の懸念を記録してください。検索結果面ではなく到達した原典を確認し、閲覧不能やlogin制限は `UNVERIFIED` として確認できたように書かないでください。必須ソースが閲覧できない場合は、同じカテゴリの代替原典を1件以上確認し、元の必須URLと代替URLの両方を記録してください。

referenceは完成デザインとしてコピーせず、構造、視覚、interaction、trustのpatternへ分解してください。copy、logo、character、固有illustration、写真、特徴的なfull-page composition、component codeを流用しないでください。

1つのreferenceと、特徴的hero geometry、固有配色、固有illustration、特徴的な見出し組版、section切替、固有motion、copy表現のうち2つ以上が一致する場合は模倣リスクとして再検討してください。

過去案件から継承できるのは、referenceの選定方法、採否記録、安全gateだけです。過去案件の固定section、配色、ロゴ、カード、入力UI、characterを持ち込まないでください。

## Phase 3：実装前プラン

codeへ進む前に、以下を会話内へ完全に提示してください。

1. 要件確認
2. message hierarchy
3. section structure
4. proof placement
5. objection handling
6. mobile ordering
7. low-fidelity wireframe
8. visual directionとDesign Decision Record
9. 作成・変更予定file
10. verification plan
11. assumptionsと`[要確認]`

### Message hierarchyとStructure

実際のsection数と順序は案件に合わせて決めてください。固定11sectionを使わないでください。

情報が不足する場合だけ、次をfallback骨格として提案できます。

1. First view：対象、価値、Primary CTA、利用可能なtrust要素
2. 対象認識／問題：必要な場合のみ
3. 解決策／offer
4. 仕組み／利用手順／選ぶ理由
5. Proof
6. Benefit・詳細
7. 条件・risk低減
8. FAQ／objection handling
9. Final CTA

各sectionについて、section名、役割、主要message、使用するproof、扱うobjection、CTAの有無、mobileでの順序を示してください。

proofは、それが支える主張の近くへ置いてください。重要なtrust情報を主要な判断CTAより前へ置き、FAQだけに重要条件を隠さないでください。objectionは最大3〜5件へ整理してください。

### Wireframe

- mobile 390px想定を先に作り、desktop 1440px想定を続けてください。
- 実際の見出し、CTA label、proof、注意事項を入れてください。
- 色、影、装飾を決める前に、情報階層とreading orderを確認してください。
- mobileは原則1列にしてください。
- DOMのreading orderはmobileの理解順を基準にし、desktopの見た目だけのために崩さないでください。
- full-bleed背景と中央寄せinner containerを別レイヤーとして示してください。

### Visual direction

Visual directionは、対象者が自分向けと判断でき、価値を理解し、実在する根拠から信頼し、主CTAを実行できるための実装仕様です。

以下を定義してください。

- 対象者とtrust requirement
- 案件固有のvisual concept 1文
- typographyとfont license
- semantic color roles
- spacing scale、grid、container
- shape、card、border、shadow
- image、icon、asset方針
- CTAの主従とcomponent states
- motionとreduced-motion
- mobile reflow
- accessibilityとperformance方針

### 「AIっぽい」デザインの回避

「AIっぽい」とは特定の色や技法ではなく、案件固有の理由がない既視感のある表現が積み重なり、実体、信頼、内容より装飾patternが前面に出ている状態です。

gradient、card、serif、animation、3D、illustrationを一律禁止しません。採用時は、案件入力、実在素材、ユーザー行動、ブランド要素のいずれに基づくかをDesign Decision Recordへ記録してください。

次は即時FAILです。

- 架空の実績、評価、数値、受賞、顧客logo、推薦文
- 架空の商品画面、dashboard、chat、入力UIを実在機能のように表示
- 動かない入力欄やbuttonを操作可能に見せる
- 権利や利用条件を確認できない写真、font、icon、codeの流用
- 生成人物や生成コメントを実在顧客、社員、専門家として表示
- referenceのcopy、character、特徴的構図、配色、logo処理の再現
- 重要情報を画像内文字だけに置く
- wireframeにない機能を見栄えのため追加する

次のGenericity Signalが案件根拠なしに3項目以上ある、または同じSignalが4section以上で反復する場合はFAILとして再設計してください。

- 青紫gradient、glow、blur orbの反復
- 左に大見出し、右に抽象3Dまたは架空UIの定型hero
- すべての情報を同じ角丸、border、shadowのcardへ格納
- 意味のないchip、pill、巨大英字、英語copy
- 本文と無関係なgrid、粒子、光線、noise
- 業種根拠のないAI robot、brain、circuit、space表現
- 写真、線画、塗りicon、emoji等の表現体系混在
- sectionごとに別の角丸、影、gradient、背景効果
- 全要素へのscroll revealやstagger animation
- 根拠のない「革新的」「次世代」「未来を変える」の強調
- 実物やproofを抽象visualで置換
- CTAより装飾や巨大見出しが強い

実装前とreview時に、次の案件固有性を確認してください。

- logoと会社名を外しても、同業他社3社へそのまま転用できる見た目ではない
- この案件の入力がなければ決められなかったvisual decisionを3つ以上説明できる
- 色、書体、余白、画像、形状のうち3系統以上が、brand、商品、顧客、実在素材へ接続する
- 最も目立つvisualが、価値、使用場面、商品、proof、感情の理解を助ける

### Design Decision Record

最低でも、FV、Primary CTA、typography、color、spacing/grid、shape/card、image/icon、motion、mobile reflow、trust materialについて、次を表へ記録してください。

| 項目 | 内容 |
|---|---|
| Decision | 実装する具体判断 |
| Reason | どの案件入力または行動に対応するか |
| Implementation | CSS token、component、asset path、状態 |
| Reference | 直接URLと採用pattern |
| Rejected option | 不採用案と理由 |
| Risk | 模倣、権利、誤認、可読性、速度 |
| Verification | PASSの確認方法 |

### Visual system最低要件

- 日本語本文は原則16px以上、line-heightはおおむね1.6〜1.9から実測する
- font familyは原則2系統以内。長文に極細weight、過剰letter-spacing、monospaceを使わない
- 色は `bg / surface / text / muted / border / brand / accent / cta / focus / success / warning / error` のsemantic tokenへ分ける
- normal text 4.5:1以上、large text 3:1以上、UI境界とfocusは3:1を目安に実測する
- 4pxまたは8pxのspacing scaleを決め、同じ意味階層には同じspacingを使う
- breakpointは端末名ではなく、内容が崩れる位置で決める
- full-bleed背景とinner containerを別要素にする
- radiusは原則2種類以内。cardは独立した情報や操作の境界が必要な場合だけ使う
- 画像には `proof / product / context / instruction / emotion / identity` の役割を割り当て、役割のない画像を使わない
- assetごとにpath/source、権利、種別、目的、crop、alt、寸法、formatを記録する
- iconの線幅、角、塗りを統一し、異なるlibraryを混在させない
- motionは操作結果、状態変化、空間関係、視線誘導に必要な場合だけ使う
- `prefers-reduced-motion`で移動、parallax、loop、smooth scrollを停止または単純化する
- CTAは `動詞＋対象または結果` とし、`詳細`、`送信`、`こちら`だけにしない

visual direction完了時は、font、type scale、line-height、semantic colors、spacing、section spacing、container、grid gap、radius、border、shadow、motion duration/easingのCSS custom propertyを実値で確定してください。

## Phase 4：実装開始gate

実装前プランを会話内へ提示し、まだ計画書もcodeも書き込まないでください。

最後に次の確認を出し、回答を待ってください。

「この実装前プランで、指定された作業フォルダに計画書とLPファイルを作成・編集してよいですか？
進めてよければ『実装開始』または同じ意味の明示的な承認をください。変更したい点があれば、その内容を教えてください。」

曖昧な相槌、別質問への回答、素材やURLの追加だけを承認とみなしません。Primary audienceまたはPrimary CTAが未確定なら承認を求めません。変更依頼を受けた場合はプランを更新し、再度承認を待ってください。

## Phase 5：承認後の保存

初回書込みの直前に、対象の絶対パス、適用対象の `AGENTS.md` 等の指示、Gitの変更状態、作成・変更予定fileの競合をもう一度確認してください。セットアップ後に対象や既存変更が変わった、または他者の変更と競合する場合は書込みを停止し、差分をユーザーへ報告してください。

既存projectにdocument規約があれば従ってください。なければ、code編集前に承認済み内容を次へ保存してください。既存の同名fileがある場合は無断で置換せず、変更対象として再確認してください。

- `docs/lp/01-requirements.md`
- `docs/lp/02-reference-selection.md`
- `docs/lp/03-structure.md`
- `docs/lp/04-wireframe.md`
- `docs/lp/05-visual-direction.md`
- `docs/lp/06-verification.md`

## Phase 6：LP実装

空の作業フォルダでは、原則として `index.html`、`styles.css`、`script.js`、`assets/`、`docs/lp/` を使用してください。既存projectでは既存stackとdesign systemを尊重し、framework変更や無関係なrefactorをしないでください。

- semantic HTML
- mobile-first responsive CSS
- JSは承認済みinteractionに限定
- JSなしでも主要内容を読める
- CTA labelは具体的にする
- keyboard focusを常時視認可能にする
- core informationを画像内文字だけにしない
- 素材がなければ権利不明の外部素材を取得せず、placeholderを明示する
- 外部dependencyやCDNを無断追加しない
- secretsをclient-side codeへ入れない
- 画像へ寸法またはaspect-ratioを指定してlayout shiftを防ぐ
- LCP画像以外はlazy loadを検討する
- font familyとweightを絞り、必要に応じて `font-display: swap` を使う

## Phase 7：検証

コードだけを読んでvisual PASSにせず、利用可能なら実ブラウザまたはスクリーンショットで確認してください。

### 機能・整合

- build、typecheck、lint、既存test
- CTA label、link、到達先
- formがある場合のlabel、keyboard、focus、error、success
- HTML landmark、heading order、alt
- missing asset、broken link、console error
- briefと価格、条件、proof、CTAの一致
- 未承認claimの混入がない

### Responsive

- 320、390、768、1024、1440px
- 横scroll、文字切れ、画像切れ、CTA切れがない
- mobileは縮小ではなくreflowする
- DOM順とreading orderが矛盾しない
- tap targetは原則44×44px以上
- sticky/fixedが本文、form、OS safe areaを覆わない
- long URL、英単語、価格、tableでlayoutが壊れない
- 200% zoomでも主要情報と操作を使える
- full-bleedがviewport両端へ届き、inner containerの中心offsetが0

### Accessibility・motion

- normal text 4.5:1、large text 3:1以上を実測
- keyboardだけで操作でき、focusが見える
- 色だけで意味や状態を伝えない
- formに明示labelとerrorの関連付けがある
- 動的結果は必要に応じて `aria-live` で通知
- 適切なaltと空altを使い分ける
- reduced-motionでも意味と操作が失われない

### Performance目標

- LCP 2.5秒以下
- CLS 0.1以下
- 静的LPのmobile initial transferはおおむね1.5MB以内
- Lighthouse Performance 90以上、Accessibility 95以上を目標とし、未達理由を記録。測定時はviewport、throttling、cold/warm cache、実行回数、代表値の取り方を記録する
- 装飾1件のために大きなJS依存を追加しない
- JS無効時も本文と主要linkを読める

### First-view five-second check

第三者が画面だけを見て、誰向けか、何を提供するか、何が違うか、次に押す場所、信用判断に使える実在情報を答えられるか確認してください。

「誰向けか」「何を提供するか」「次に押す場所」の3項目はすべて必須です。さらに「何が違うか」「信用判断に使える実在情報」のどちらか1項目以上を答えられることをPASS条件とします。必須3項目の一つでも答えられない場合はFAILです。

未実行の確認をPASSと報告しないでください。環境上できない確認はmanual checkとして `docs/lp/06-verification.md` へ残してください。

## Phase 8：実装後creative review

実装担当の完了宣言とcreative reviewを同じ判定として扱わないでください。subagentまたは別reviewerを利用できる場合は、実装を担当していないcreative reviewerへ、承認済みrequirements、structure、wireframe、visual direction、実装画面、verification結果を渡して独立reviewを行ってください。

別reviewerを利用できない場合は、実装作業をいったん終了し、ファイルを変更しないreview passを別工程として実行し、`SELF_REVIEW` と明記してください。この場合は独立review済みと主張せず、残るriskを完了報告へ記載してください。

reviewでは最低限、次を判定してください。

- 承認済みaudience、offer、proof、Primary CTAとの一致
- wireframeとsection orderとの一致
- 案件固有visual decision 3件以上
- 即時FAILとGenericity Signal
- first-view必須3項目とtrust/differentiation
- 320、390、768、1024、1440pxと200% zoom
- contrast、focus、keyboard、reduced-motion、alt、label
- assetの権利、参照模倣、架空claim
- full-bleed、container中心、horizontal overflow
- console error、404、performance上の重大問題

review結果を `strengths / major issues / minor issues / mobile concerns / required fixes before delivery / first-view clarity / CTA clarity / trust・proof placement / hierarchy・polish / originality・imitation risk / required-reference status` に分け、`PASS / FAIL / PARTIAL / UNVERIFIED` で `docs/lp/06-verification.md` へ記録してください。

重大issueが1件でもある場合はFAILとし、修正して該当検証とcreative reviewを再実行してください。FAILまたは未解決の重大issueが残る状態で `LOCAL_COMPLETE` と報告しないでください。

## Phase 9：Codexによるローカルpreview

既存projectのpreview commandを優先してください。静的構成なら `127.0.0.1` に限定したlocal serverを、Codex自身が起動してください。

利用者へserver起動commandの実行を求めないでください。Codexがpreviewの起動、mobile/desktop確認、停止または維持の判断まで行い、利用者には開くだけのpreview URLと確認結果を報告します。外部tunnel、LAN公開、本番deployは行わないでください。

実行環境の制約でserverを起動または維持できない場合も、利用者へ代行実行を依頼しません。可能なら静的fileを直接確認し、不可能な確認項目だけを `UNVERIFIED` として理由とともに報告してください。

## Phase 10：完了報告

最後に次を報告してください。

1. 最終message hierarchy
2. Primary audienceとPrimary CTA
3. 最終section order
4. 案件固有のvisual decision 3件以上
5. 作成・変更した内容と主なfile
6. Codexが用意したlocal preview URLと確認結果
7. 実行した検証と結果
8. assumptions、placeholder、未確認事項
9. 公開前に人が行う作業
10. 外部公開・本番変更を行っていないこと

完成、公開可否、conversion、売上、集客成果を、実際に確認できた範囲を超えて保証しないでください。
