<div align="center">

<img src="./assets/profile/header.svg" width="100%" alt="Leon — Dr.Lnx, Developer at N3XT Agency"/>

<br><br>

<img src="./assets/profile/typing.svg" width="620" alt="Discord systems · Automation · Internal tooling"/>

<br><br>

<a href="https://n3xt-agency.com"><img src="./assets/profile/btn-website.svg" height="46" alt="Website: n3xt-agency.com"/></a>
&nbsp;
<a href="mailto:leon.holetz@n3xt-agency.com"><img src="./assets/profile/btn-contact.svg" height="46" alt="Contact: leon.holetz@n3xt-agency.com"/></a>

<br><br>

<a href="#overview"><img src="./assets/profile/nav-overview.svg" height="34" alt="Overview"/></a>
<a href="#work"><img src="./assets/profile/nav-work.svg" height="34" alt="Work"/></a>
<a href="#stack"><img src="./assets/profile/nav-stack.svg" height="34" alt="Stack"/></a>
<a href="#how-i-build"><img src="./assets/profile/nav-how-i-build.svg" height="34" alt="How I build"/></a>
<a href="#contact"><img src="./assets/profile/nav-contact.svg" height="34" alt="Contact"/></a>

</div>

<br>

<a name="overview"></a>
<img src="./assets/profile/h-overview.svg" width="100%" alt="01 — Overview"/>

I work on systems that a community actually runs on — support, moderation, recruitment,
engagement — rather than one-off scripts bolted onto someone else's bot. The through-line
is **consolidation**: one codebase and one set of data instead of five third-party services
that each know a fifth of the story.

The same instinct shows up in the small stuff. *If a job runs twice, it should run on a
cron; if a decision is a setting, it should not be a rebuild.*

```ts
const leon = {
  handle:   "Dr.Lnx",
  role:     "Developer @ N3XT Agency",
  building: "N3XT.sys — a complete Discord server operating system",
  focus:    ["bot platforms", "automation", "developer tooling"],
  approach: "one system per client, deployed and managed end to end",
} as const;
```

<br>

<a name="work"></a>
<img src="./assets/profile/h-work.svg" width="100%" alt="02 — Work"/>

### [N3XT.sys](https://github.com/n3xtpy/N3XT.sys) — Discord server operating system

> *One bot, one dedicated instance per community, replacing the usual stack of five or six.*

<div align="center">
  <a href="https://github.com/n3xtpy/N3XT.sys"><img src="./assets/profile/terminal.svg" width="88%" alt="N3XT.sys boot sequence"/></a>
</div>

<br>

Support tickets, moderation, staff recruitment, engagement, temporary voice, surveys,
anti-raid, ban appeals, audit logs and presentation — all on one codebase and one dataset,
so a member's ticket history, moderation record, staff status and activity level can appear
in the same place.

| | |
| :-- | :-- |
| 🧱 **Stack** | TypeScript · discord.js 14 · Node 20 · better-sqlite3 |
| 🖥️ **Interface** | Native Discord panels, plus an Ink/React operator console in the terminal |
| ✅ **Quality** | Typecheck, lint and tests on every push |
| 🔒 **Deployment** | Dedicated instance per server, hard-locked to that guild |

<br>

<a name="stack"></a>
<img src="./assets/profile/h-stack.svg" width="100%" alt="03 — Stack"/>

<div align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,py,nodejs,react,discord,sqlite,githubactions,bash,linux&perline=10&theme=dark" alt="Tech stack"/>
</div>

<br>

| Area | What I reach for |
| :-- | :-- |
| **Languages** | TypeScript · Python · JavaScript |
| **Runtime** | Node 20 · discord.js · React (Ink) |
| **Data** | SQLite / better-sqlite3 |
| **Automation** | GitHub Actions · cron · shell |
| **Quality** | ESLint · Vitest · `tsc --noEmit` |

<br>

<a name="how-i-build"></a>
<img src="./assets/profile/h-how-i-build.svg" width="100%" alt="04 — How I build"/>

<table>
<tr>
<td width="50%" valign="top">

#### ⚙️ Configuration over hardcoding

Channels, roles, thresholds, timers and wording are settings. Changing how many warnings
trigger a ban, or where tickets open, is a config change — not a release.

</td>
<td width="50%" valign="top">

#### ♻️ Built to survive restarts

Timed actions, scheduled jobs and in-progress state are restored from storage. A reboot
mid-task is an inconvenience, not data loss.

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🛡️ Failure is a no-op

When an upstream is rate-limited or unreachable, jobs log a skip and exit clean. A bad
network day leaves yesterday's good state in place instead of writing a broken one.

</td>
<td width="50%" valign="top">

#### 🔍 Checked before it ships

Typecheck, lint and tests run on every push. The interesting bugs are the ones a compiler
cannot catch, so the boring ones should never reach a review.

</td>
</tr>
</table>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/drlnx/drlnx/output/snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/drlnx/drlnx/output/snake-light.svg"/>
    <img src="https://raw.githubusercontent.com/drlnx/drlnx/output/snake-dark.svg" width="100%" alt="Contribution snake"/>
  </picture>
</div>

<br>

<a name="contact"></a>
<img src="./assets/profile/h-contact.svg" width="100%" alt="05 — Contact"/>

Work enquiries, custom systems, or a scoping call for a deployment — either channel reaches
me directly.

<div align="center">
<br>

<a href="mailto:leon.holetz@n3xt-agency.com"><img src="./assets/profile/btn-contact.svg" height="46" alt="Contact: leon.holetz@n3xt-agency.com"/></a>
&nbsp;
<a href="https://n3xt-agency.com"><img src="./assets/profile/btn-website.svg" height="46" alt="Website: n3xt-agency.com"/></a>

<br><br>

<img src="./assets/profile/footer.svg" width="100%" alt=""/>

</div>
