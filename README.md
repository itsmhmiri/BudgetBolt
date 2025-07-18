# 💰 BudgetBolt - Privacy-First Desktop Finance Tracker

**BudgetBolt** is a lightweight, offline-first desktop app to manage your personal finances — with a focus on **privacy**, **performance**, and **productivity**.

No cloud. No accounts. No subscription. Just your data, your way.

---

## 🚀 Features

- ✅ Track **income** and **expenses**
- 📅 Daily, weekly, monthly filtering
- 📊 Interactive **charts** and insights
- 📁 Export reports as **PDF** or **CSV**
- 🔐 Local-first with **SQLite**
- 🎯 Set and monitor **budget goals**
- 🌓 **Dark/light theme** support
- 🔒 Optional password lock & manual backups

---

## 🧰 Tech Stack

| Layer        | Stack                                |
|--------------|---------------------------------------|
| UI           | [Svelte](https://svelte.dev) + TailwindCSS |
| Runtime      | [Tauri](https://tauri.app) (Cross-platform desktop) |
| Local DB     | SQLite (via `rusqlite`)               |
| Charts       | Chart.js or ApexCharts (TBD)          |
| PDF Export   | pdf-lib or html-to-pdf (TBD)          |
| Optional API | FastAPI (for future sync/backup)      |

---

## 📦 Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/budgetbolt.git
cd budgetbolt
