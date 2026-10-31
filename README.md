<!-- Header and stats images are built by build_assets.py. Edit the copy there, not in the SVGs. -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Prince Gupta. I lead social and partnerships at Lyzr AI, and I build the systems that run it. Bengaluru, from Nepal.">
</picture>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=2800&pause=900&color=C4FF1A&center=true&vCenter=true&width=640&lines=Creative+strategist+at+Lyzr+AI;Documentary+storyteller+at+decodedbyprince;When+the+work+repeats%2C+I+write+the+tool;Bengaluru%2C+from+Nepal">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=2800&pause=900&color=1F2120&center=true&vCenter=true&width=640&lines=Creative+strategist+at+Lyzr+AI;Documentary+storyteller+at+decodedbyprince;When+the+work+repeats%2C+I+write+the+tool;Bengaluru%2C+from+Nepal" alt="Creative strategist at Lyzr AI. Documentary storyteller at decodedbyprince. When the work repeats, I write the tool. Bengaluru, from Nepal.">
</picture>

<br>

<a href="https://linkedin.com/in/pr1ncegupta"><img src="https://img.shields.io/badge/LinkedIn-1f2120?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2M0ZmYxYSIgZD0iTTIwLjQ0NyAyMC40NTJoLTMuNTU0di01LjU2OWMwLTEuMzI4LS4wMjctMy4wMzctMS44NTItMy4wMzctMS44NTMgMC0yLjEzNiAxLjQ0NS0yLjEzNiAyLjkzOXY1LjY2N0g5LjM1MVY5aDMuNDE0djEuNTYxaC4wNDZjLjQ3Ny0uOSAxLjYzNy0xLjg1IDMuMzctMS44NSAzLjYwMSAwIDQuMjY3IDIuMzcgNC4yNjcgNS40NTV2Ni4yODZ6TTUuMzM3IDcuNDMzYy0xLjE0NCAwLTIuMDYzLS45MjYtMi4wNjMtMi4wNjUgMC0xLjEzOC45Mi0yLjA2MyAyLjA2My0yLjA2MyAxLjE0IDAgMi4wNjQuOTI1IDIuMDY0IDIuMDYzIDAgMS4xMzktLjkyNSAyLjA2NS0yLjA2NCAyLjA2NXptMS43ODIgMTMuMDE5SDMuNTU1VjloMy41NjR2MTEuNDUyek0yMi4yMjUgMEgxLjc3MUMuNzkyIDAgMCAuNzc0IDAgMS43Mjl2MjAuNTQyQzAgMjMuMjI3Ljc5MiAyNCAxLjc3MSAyNGgyMC40NTFDMjMuMiAyNCAyNCAyMy4yMjcgMjQgMjIuMjcxVjEuNzI5QzI0IC43NzQgMjMuMiAwIDIyLjIyMiAwaC4wMDN6Ii8+PC9zdmc+" alt="LinkedIn"></a>
<a href="https://x.com/pr1ncegupta"><img src="https://img.shields.io/badge/X-1f2120?style=for-the-badge&logo=x&logoColor=c4ff1a" alt="X"></a>
<a href="https://instagram.com/decodedbyprince"><img src="https://img.shields.io/badge/decodedbyprince-1f2120?style=for-the-badge&logo=instagram&logoColor=c4ff1a" alt="Instagram"></a>
<a href="https://hiiprince.com"><img src="https://img.shields.io/badge/hiiprince.com-c4ff1a?style=for-the-badge&logo=vercel&logoColor=1f2120" alt="hiiprince.com"></a>
<a href="https://www.lyzr.ai"><img src="https://img.shields.io/badge/@_Lyzr_AI-1f2120?style=for-the-badge" alt="Lyzr AI"></a>

</div>

I am a creative strategist at [Lyzr AI](https://www.lyzr.ai), an enterprise agentic AI platform. I studied computer science engineering at Jain University, so when the content work starts repeating itself, I write the tool that takes the repetition away.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/numbers-dark.svg">
  <img src="assets/numbers-light.svg" width="100%" alt="9M views on the Architect creator campaign at Lyzr. Close to 100K followers for decodedbyprince across platforms. 1.5 years to build it, after a few channels that did not work.">
</picture>

> [!TIP]
> **The short version:** I am a marketer who writes code. The numbers above come from systems I built, not from posting harder. Below is how each one works.

---

## 🚀 Featured work

### 1. The content engine &nbsp; ![Claude](https://img.shields.io/badge/Claude_skills-1f2120?logo=claude&logoColor=c4ff1a)

**Problem.** A documentary channel needs a hook, a script, an edit plan and an upload pack for every episode, and doing it by hand capped how often I could ship.
**What I built.** A chain of Claude skills, one per stage, where each skill's output is the next one's input. Hooks get scored on a fixed rubric and only the ones above 80 move on.
**Result.** [decodedbyprince](https://instagram.com/decodedbyprince) at close to 100K followers across platforms in 1.5 years.

```mermaid
flowchart LR
    A([💡 hook-writer]) --> B{{🎯 hook-scorer<br/>80+ only}}
    B -- pass --> C([✍️ script-writer])
    B -. below 80 .-> A
    C --> D([🧹 anti-ai-writing])
    D --> E([🎞️ broll-sourcer])
    E --> F([📦 youtube-packaging])
    F --> G((🚀 Publish))

    classDef step fill:#1f2120,stroke:#c4ff1a,stroke-width:2px,color:#ffffff
    classDef ship fill:#c4ff1a,stroke:#1f2120,stroke-width:2px,color:#1f2120
    class A,B,C,D,E,F step
    class G ship
```

<details>
<summary><b>🤖 Every skill in the engine</b></summary>
<br>

| Stage | Skill | Job |
| :-- | :-- | :-- |
| Hooks | `hook-writer` | Writes a pool of 6 to 10 openers from a topic or rough notes |
| Hooks | `hook-scorer` | Scores each hook on a rubric and only passes the ones above 80 |
| Script | `nas-daily-script-writer` | Turns a picked hook into a one-minute talking-to-camera script |
| Script | `final-script-polish` | Rewrites a single line or beat without regenerating the whole thing |
| Edit | `anti-ai-writing` | Strips the tells that make copy read machine-written |
| Edit | `patchnote-broll-sourcer` | Gives the editor a shot list with a source for every line |
| Social | `carousel-architect` | Picks three carousel formats for a source and writes every slide |
| Ship | `decodedbyprince-youtube-packaging` | Thumbnail text, title, tags and description in one pass |

</details>

### 2. Generative engine optimisation at Lyzr &nbsp; ![GEO](https://img.shields.io/badge/GEO-1f2120)

Search is moving into chat answers, so I track how LLMs cite Lyzr in their answers and feed what I find back into the content plan.[^geo]

### 3. The Architect creator campaign &nbsp; ![9M views](https://img.shields.io/badge/9M-views-c4ff1a?labelColor=1f2120)

A creator and influencer campaign I ran for Lyzr that reached **9M views**.

### 4. TL;DR, a product demo on Lyzr agents &nbsp; ![TypeScript](https://img.shields.io/badge/TypeScript-1f2120?logo=typescript&logoColor=c4ff1a)

[TL;DR](https://github.com/pr1ncegupta/TLDR-P) turns any text into a summary and action points using four AI agents running on Lyzr. It is a marketing asset that is also working software: [try it live](https://tldr-p.vercel.app).

### 5. Second brain &nbsp; ![Notion](https://img.shields.io/badge/Notion-1f2120?logo=notion&logoColor=c4ff1a)

One Notion task table across work and life, with Slack digests twice a day, so nothing from a campaign falls through between meetings.

---

## 🧭 At Lyzr

```mermaid
timeline
    title Lyzr, so far
    April 2025 : Joined as an intern
    January 2026 : Full time as creative strategist
                 : Leading social and partnerships
```

- [x] Organic social across **LinkedIn, X, Instagram and Reddit**
- [x] Personal branding and podcast outreach for Lyzr's leadership
- [x] Creator and influencer partnerships, including the **Architect** campaign
- [x] Generative engine optimisation
- [x] Hiring and running a team of interns

---

## 🏛️ decodedbyprince

A documentary channel on archaeology, mythology and sacred places, made with the content engine above.

<details>
<summary><b>📍 Recent stories</b> (click to open)</summary>
<br>

| | Story | Where |
| :-: | :-- | :-- |
| 🗿 | **Göbekli Tepe** | Şanlıurfa, Türkiye |
| 💀 | **Roopkund**, the skeleton lake | Uttarakhand, India |
| 🛕 | **Kailasa Temple**, cut from one rock | Ellora, India |
| 🕳️ | **Derinkuyu**, the underground city | Cappadocia, Türkiye |
| 🦁 | **Sigiriya**, the lion rock | Central Province, Sri Lanka |

</details>

---

## 💻 Code I ship

| Build | What it is | Stack |
| :-- | :-- | :-- |
| [**hiiprince.com**](https://hiiprince.com) | My portfolio site | ![Next.js](https://img.shields.io/badge/Next.js-1f2120?logo=nextdotjs&logoColor=c4ff1a) |
| [**voicemind-public**](https://github.com/pr1ncegupta/voicemind-public) | A voice-first AI mental health companion with emotion fusion, crisis detection and an offline coping engine | ![Flutter](https://img.shields.io/badge/Flutter-1f2120?logo=flutter&logoColor=c4ff1a) ![FastAPI](https://img.shields.io/badge/FastAPI-1f2120?logo=fastapi&logoColor=c4ff1a) |
| [**deforestation-ml**](https://github.com/pr1ncegupta/deforestation-ml) | Deforestation monitoring from satellite imagery, with a Streamlit front end | ![Python](https://img.shields.io/badge/Python-1f2120?logo=python&logoColor=c4ff1a) |
| [**ai-bharat-teacherOS**](https://github.com/pr1ncegupta/ai-bharat-teacherOS) | Classroom management tools for rural teachers | ![AI](https://img.shields.io/badge/AI-1f2120) |
| **Cobra** | A scorekeeper for the Cobra card game | ![React](https://img.shields.io/badge/React-1f2120?logo=react&logoColor=c4ff1a) |

---

## 🧰 Tools

<table>
  <tr>
    <td><b>Code</b></td>
    <td><img src="https://skillicons.dev/icons?i=ts,nextjs,react,tailwind,py,fastapi&perline=6" alt="TypeScript, Next.js, React, Tailwind, Python, FastAPI"></td>
  </tr>
  <tr>
    <td><b>AI and ops</b></td>
    <td>
      <img src="https://img.shields.io/badge/Claude-1f2120?style=for-the-badge&logo=claude&logoColor=c4ff1a" alt="Claude">
      <img src="https://img.shields.io/badge/Notion-1f2120?style=for-the-badge&logo=notion&logoColor=c4ff1a" alt="Notion">
      <img src="https://img.shields.io/badge/Slack-1f2120?style=for-the-badge" alt="Slack">
    </td>
  </tr>
  <tr>
    <td><b>Design and video</b></td>
    <td>
      <img src="https://img.shields.io/badge/Figma-1f2120?style=for-the-badge&logo=figma&logoColor=c4ff1a" alt="Figma">
      <img src="https://img.shields.io/badge/Final_Cut_Pro-1f2120?style=for-the-badge" alt="Final Cut Pro">
    </td>
  </tr>
</table>

---

## 📈 On GitHub

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=pr1ncegupta&hide_border=true&background=1f2120&ring=c4ff1a&fire=c4ff1a&currStreakNum=ffffff&sideNums=ffffff&currStreakLabel=c4ff1a&sideLabels=e4e7e5&dates=acafad&stroke=414342">
  <img src="https://streak-stats.demolab.com?user=pr1ncegupta&background=ffffff&border=e4e7e5&ring=1f2120&fire=1f2120&currStreakNum=1f2120&sideNums=1f2120&currStreakLabel=1f2120&sideLabels=545655&dates=707271&stroke=e4e7e5" alt="GitHub contribution streak for pr1ncegupta">
</picture>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/pr1ncegupta/pr1ncegupta/output/snake-dark.svg">
  <img src="https://raw.githubusercontent.com/pr1ncegupta/pr1ncegupta/output/snake-light.svg" width="100%" alt="A snake eating my GitHub contribution graph">
</picture>

</div>

---

## 📬 Find me

<div align="center">

**Partnerships, podcasts, or a creator collab with Lyzr?** <kbd>LinkedIn</kbd> is fastest.

[LinkedIn](https://linkedin.com/in/pr1ncegupta) &nbsp;·&nbsp; [X](https://x.com/pr1ncegupta) &nbsp;·&nbsp; [Instagram](https://instagram.com/decodedbyprince) &nbsp;·&nbsp; [hiiprince.com](https://hiiprince.com)

<br>

<img src="https://komarev.com/ghpvc/?username=pr1ncegupta&color=1f2120&style=flat-square&label=profile+views" alt="Profile views">

</div>

[^geo]: Generative engine optimisation is the search-engine-optimisation idea applied to LLM answers instead of search results.
