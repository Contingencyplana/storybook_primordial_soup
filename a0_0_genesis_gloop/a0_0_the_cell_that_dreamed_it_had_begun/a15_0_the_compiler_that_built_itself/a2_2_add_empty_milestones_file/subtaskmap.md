# 📘 Subtask Map – a2_2_add_empty_milestones_file

This node creates an empty `milestones.md` file inside a specified `taskmaps/` folder, if one does not already exist. It ensures recursive trace logging and UTF-8 compatibility for extended character sets.

---

## ✅ Primary Function

| Subtask | Description |
|--------|-------------|
| Create file | Generate `milestones.md` in `taskmaps/` if missing |
| Write content | Insert header and note using UTF-8 encoding |
| Skip if exists | Detect and skip creation if file already present |
| Return trace | Include ISO 8601 timestamp and status metadata |

---

## 🧪 Test Coverage

| Test | Purpose |
|------|---------|
| `test_create_milestones_file` | Validates successful creation of new `milestones.md` file |
| `test_skip_existing_milestones` | Confirms skip behavior if file already exists |
| `--reset` flag | Removes `milestones.md` prior to test run |
| Interactive cleanup | Supports `[L]`eave or `[R]`emove post-test prompt |

---

## 🧩 Trace Metadata Example

```json
{
  "status": "success",
  "message": "Created milestones.md in: ...",
  "path": ".../taskmaps/milestones.md",
  "trace": {
    "event": "create_empty_milestones_file",
    "timestamp": "2025-07-26T08:00:00Z"
  }
}
```

---

## 📂 Output Location

The generated file will appear in the specified `taskmaps/` directory. For test scaffolding, the target path is:

```
a99_1_test_create_taskmaps/taskmaps/milestones.md
```

---
