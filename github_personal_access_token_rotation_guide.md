<!-- Save to: storybook_primordial_soup/github_personal_access_token_rotation_guide.md -->

# 🔑 GitHub Personal Access Token (PAT) Rotation Guide – Storybook Primordial Soup

## 📅 Next Scheduled Rotation:
**01/01/2026**  
(*Token auto-expires in 5 months*)

---

## 🧭 Purpose:
This guide explains how to rotate the GitHub PAT for `storybook_primordial_soup` safely, avoiding service disruptions.

---

## 🔧 Step-by-Step Process:

### 1️⃣ Regenerate the Token:
- Go to: [GitHub PAT Settings](https://github.com/settings/personal-access-tokens)
- Click **Regenerate** for the current token.
- Copy the new token immediately.

---

### 2️⃣ Replace the Token Everywhere:

| **Where** | **Action** |
|-----------|------------|
| **Windows Credential Manager** | Delete `git:https://github.com` |
| **Git (VSC terminal)** | Run `git credential-manager-core erase`, or use Credential Manager GUI |
| **On next `git pull`/`git push`** | Enter `Contingencyplana` as username, paste new PAT as password |
| **Local `.env` files** | Replace old token |
| **GitHub Actions → Secrets** | Update token in repo settings |
| **Any automation scripts** | Replace token in config |

---

### 3️⃣ Test Git Access:

```bash
git pull
git push
