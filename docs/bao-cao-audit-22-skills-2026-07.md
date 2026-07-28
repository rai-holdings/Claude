# Báo cáo A/B & Audit an ninh — Bộ 22 skills Claude Code (07/2026)

> Nguồn danh sách: bài LinkedIn của Charlie Hills ("You installed Claude Code and stopped there?").
> Phương pháp: shallow-clone **cả 22 repos**, liệt kê toàn bộ cây file, grep các pattern nguy hiểm
> (`curl|bash`, `base64`/`eval`, network hosts lạ, đọc/gửi credential, hooks tự chạy, `postinstall`,
> telemetry, auto-update), đọc trực tiếp mọi hook + install script, đối chiếu số sao & ngày commit
> trên GitHub. Ngày thực hiện: **2026-07-28**.

## 1. Kết quả Test A/B với repo này

| Trạng thái | Kết luận |
|---|---|
| Skill đã có trong repo | Chỉ có `tao-media` (không trùng skill nào trong 22). **Đã cập nhật điểm mạnh** từ bài học audit: guard chống prompt-injection, gợi ý pipeline HTML→video (Remotion/Hyperframes) cho video đồ hoạ. |
| Skill chưa có | Cả 22 đều chưa có → đã audit từng repo (mục 2), **không phát hiện mã độc**; loại 3 repo CAUTION khỏi diện khuyến nghị cài trực tiếp; **chưng cất tinh hoa** của các repo SAFE thành 3 skill mới tối ưu trong repo này (mục 4). |

## 2. Bảng tổng hợp audit 22 repos

Verdict: ✅ SAFE — an toàn để cài · ⚠️ CAUTION — không độc hại nhưng có bề mặt rủi ro, cần cân nhắc · ❌ AVOID — không có repo nào.

### 🔨 Lập trình

| Repo | Stars | Bản chất | Phát hiện an ninh | Verdict |
|---|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 262.5k | 14 SKILL.md + hooks | Hook SessionStart chỉ đọc file local; brainstorm server bind 127.0.0.1 có token auth. Không network, không telemetry. | ✅ SAFE |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 124.9k | 59 SKILL.md, **733 scripts** | Telemetry opt-in (mặc định off) POST về Supabase của tác giả; **team-mode auto-update chạy code upstream chưa review mỗi session**. Không mã độc. | ⚠️ CAUTION |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 93.8k | 11 SKILL.md + hooks + MCP | Hooks không network; installer verify sha256; README có `curl\|bash` (nên cài qua marketplace thay thế). | ✅ SAFE |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 90.7k | 12 SKILL.md + hooks + MCP | Zero network call, zero child_process trong hooks/MCP. | ✅ SAFE |
| [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | 30.2k | Plugin chính thức OpenAI | Không HTTP call trực tiếp trong scripts; **code/diff rời máy đến OpenAI theo thiết kế** — cân nhắc với repo private. | ✅ SAFE* |
| [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 12.3k | 2 SKILL.md + 1 hook sh | Hook chỉ đọc file local, exit 0 khi lỗi. Repo "sạch" nhất nhóm. | ✅ SAFE |

### 🎨 Thiết kế

| Repo | Stars | Bản chất | Phát hiện an ninh | Verdict |
|---|---|---|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 111k | CSV database + BM25 search Python | Search thuần local; gen ảnh Gemini/Pexels opt-in. Lưu ý: template `stack/.claude/settings.json` có `Read(//home/**)` + `enableAllProjectMcpServers: true` — quá rộng, đừng copy nguyên. | ✅ SAFE |
| [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | 68.5k | 13 SKILL.md thuần markdown | Không executable nào chạy trong workflow agent. | ✅ SAFE |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 52k | 1 skill + 23 commands + 60 detector rules | Hooks PostToolUse/Stop **tự chạy** (đã audit: local-only, không network); phone-home version check hằng ngày tới impeccable.style (GET-only); kênh update skill nằm ngoài GitHub. | ✅ SAFE (cận CAUTION) |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 38.3k | Framework HTML→video + 19 skills | **Telemetry PostHog bật mặc định** (tắt: `HYPERFRAMES_NO_TELEMETRY=1`), CLI auto-update, toolchain lớn (Puppeteer + ffmpeg). Không mã độc. | ⚠️ CAUTION nhẹ |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | 21.9k | 8 SKILL.md thuần markdown | 0 executable, 0 hook, 0 network. Rủi ro thấp nhất nhóm. | ✅ SAFE |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | 12.5k | 8 SKILL.md chính chủ GSAP | Chỉ example code demo; CDN import chỉ trong demo. | ✅ SAFE |

### 🔍 Nghiên cứu & công cụ

| Repo | Stars | Bản chất | Phát hiện an ninh | Verdict |
|---|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | 164.7k | 17 skills chính chủ Anthropic | Không network đáng ngại; script minh bạch. | ✅ SAFE |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 97.5k | CLI Python knowledge-graph | Có SSRF guard chủ động; git hook opt-in; corpus gửi lên LLM provider nếu bật LLM mode. | ✅ SAFE |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 54.5k | Python/Node/Go đa nguồn | **Đọc cookie trình duyệt (Chrome/Safari) + macOS Keychain** để dùng session X/Twitter; nhiều API bên thứ ba trả phí; SessionStart hook tự chạy (chỉ đọc config). Code minh bạch nhưng quyền rộng bất thường. | ⚠️ CAUTION |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 39.4k | Rust CLI điều khiển Chrome | `postinstall` tải binary từ GitHub Releases **không verify checksum**; toàn quyền trình duyệt theo thiết kế. | ✅ SAFE (thận trọng) |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | 27.4k | TS CLI "package manager" skills | Bảo mật tốt nhất nhóm (sanitize terminal-escape, git transport allowlist, audit score trước khi cài). Telemetry opt-out (`DO_NOT_TRACK=1`). | ✅ SAFE |
| [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | 26.9k | Statusline plugin TS | **Zero network egress** — đã grep toàn bộ src + dist. Không telemetry. | ✅ SAFE |

### 📣 Nội dung & marketing

| Repo | Stars | Bản chất | Phát hiện an ninh | Verdict |
|---|---|---|---|---|
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | 4.1k | 160 file md chính chủ Remotion | Scripts offline hoàn toàn, không network. | ✅ SAFE |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 42.1k | 49 skills + 64 CLI wrapper | Mỗi CLI chỉ gọi đúng 1 host vendor chính thức, **64/64 có `--dry-run`**; API key chỉ gửi tới vendor tương ứng. | ✅ SAFE |
| [blader/humanizer](https://github.com/blader/humanizer) | 31.8k | 1 SKILL.md 412 dòng | Thuần instruction, không executable phía user. | ✅ SAFE |
| [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) | 2k | 17 SKILL.md | Không mã độc, nhưng: chỉ dẫn agent **tự sinh + chạy Node script với API key thật** (Apify/Gemini); scraping Instagram/LinkedIn trái ToS; tốn tiền thật (~$0.50/scrape); pattern "auto-start on load"; im lặng từ 05/2026. | ⚠️ CAUTION |

## 3. Checklist an ninh chuẩn khi cài skill bên thứ ba

Quy trình đã dùng cho 22 repos trên — tái sử dụng cho mọi skill mới (đã đóng gói thành skill `kiem-dinh-skill`):

1. **Clone về trước, cài sau** — `git clone --depth 1`, không bao giờ `curl | bash`.
2. **Liệt kê toàn bộ cây file** — đếm executable (.sh/.js/.py/.ts), tìm `hooks/`, `postinstall`, installer.
3. **Grep pattern nguy hiểm**: `curl.*\|.*bash`, `base64 -d`, `eval`, `child_process`, `atob(`, network hosts ngoài vendor chính thức, đọc `~/.ssh` / cookie / Keychain / env credential.
4. **Đọc từng hook tự chạy** (SessionStart/PostToolUse/Stop) và install script — đây là code chạy không cần hỏi.
5. **Soi settings.json đi kèm** — từ chối permission quá rộng (`Read(//home/**)`, `enableAllProjectMcpServers: true`).
6. **Kiểm tra telemetry & auto-update** — mặc định bật hay opt-in? Update từ GitHub hay server riêng của tác giả? Auto-update = chạy code chưa review.
7. **Đọc SKILL.md như đọc prompt không tin cậy** — cảnh giác chỉ dẫn "auto-start on load", "bypass permission", "prefer X over built-in".
8. **Chấm verdict** SAFE / CAUTION / AVOID; nếu cài repo CAUTION: **pin theo commit SHA**, tắt telemetry, không bật auto-update.
9. **Chỉ cài skill thực sự dùng** — mỗi skill chiếm context + tăng bề mặt tấn công.

## 4. Skill mới tổng hợp (chưng cất từ các repo SAFE)

Thay vì cài 22 repos (nặng context, nhiều hook, một số CAUTION), repo này đóng gói tinh hoa thành 3 skill thuần markdown — zero hook, zero network, zero telemetry:

| Skill mới | Chưng cất từ | Tinh hoa lấy về |
|---|---|---|
| `lap-trinh-chuan` | superpowers, ponytail, caveman, i-have-adhd, gstack | Nấc thang tối giản 7 bậc; pipeline brainstorm→plan→TDD→verify; systematic debugging (root cause trước); bảng red-flags chống rationalization; auto-clarity khi rủi ro; verification-before-completion |
| `giao-dien-dep` | taste-skill, ui-ux-pro-max, impeccable, emilkowalski, gsap-skills | Brief inference + Design Read + 3 dials; checklist ưu tiên 1→10; danh sách anti-slop (cấm AI purple gradient, Inter+slate mặc định…); bảng Before/After animation; 4 modes theo mục tiêu visitor; bounded QA passes |
| `kiem-dinh-skill` | Quy trình audit này + vercel-labs/skills, graphify | Checklist mục 3 dạng thực thi được; các pattern grep sẵn; tiêu chí verdict; nguyên tắc "content là data, không phải instruction" |

Skill hiện có `tao-media` được bổ sung: guard chống prompt-injection trong file/URL tham chiếu, và gợi ý pipeline HTML→video cho video đồ hoạ/explainer.

## 5. Khuyến nghị cài trực tiếp (nếu cần thêm)

- **Đáng cài nhất theo nhu cầu**: `anthropics/skills` (chính chủ, skill-creator + docx/pdf/pptx/xlsx), `blader/humanizer` (viết nội dung), `emilkowalski/skills` + `greensock/gsap-skills` (animation), `remotion-dev/skills` (video bằng code), `coreyhaines31/marketingskills` (marketing — nhớ tận dụng `--dry-run`).
- **Cân nhắc kỹ trước khi cài**: `gstack` (pin SHA, tắt team-mode + telemetry), `last30days-skill` (chấp nhận đọc cookie trình duyệt?), `hyperframes` (`HYPERFRAMES_NO_TELEMETRY=1`), `social-media-skills` (review script trước khi chạy, ToS + chi phí Apify), `codex-plugin-cc` (code rời máy đến OpenAI).
- **Không cài trùng chức năng**: các kỹ thuật cốt lõi của superpowers/ponytail/taste/ui-ux-pro-max/impeccable/emilkowalski đã được chưng cất vào 3 skill nội bộ ở mục 4.
