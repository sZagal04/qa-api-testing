# 🔌 QA API Testing — Urban Grocers Backend

Automated API test suite for the Urban Grocers backend, built with **Python** and **pytest**. Validates kit creation endpoint behavior using boundary value analysis, equivalence partitioning, and negative testing.

---

## 🎯 What was tested

The Urban Grocers API allows users to create grocery kits. This project tests the `/api/v1/kits/` endpoint to confirm it handles valid and invalid `name` field inputs correctly and returns the expected HTTP status codes.

**Tested areas:**
- Boundary value analysis on kit name length (1 char, 511 chars, 512 chars)
- Equivalence partitioning: valid strings, empty string, missing field, wrong data type
- Special characters and spaces in kit name
- Numeric strings as kit name
- Authentication flow: user creation → auth token → kit POST
- Status code verification (201 Created, 400 Bad Request)
- Response body validation (name field matches input)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Test scripting language |
| pytest | Test runner |
| requests | HTTP client for API calls |
| PyCharm | IDE |
| Postman | Manual verification and test design aid |
| apiDoc | API documentation reference |

---

## 📁 Project Structure

```
qa-api-testing/
│
├── create_kit_name_kit_test.py   # All test functions (pytest)
├── sender_stand_request.py       # HTTP request functions (post_new_user, post_new_kit)
├── configuration.py              # Base URL and API endpoint paths
├── data.py                       # Request headers, user body, kit body templates
└── README.md
```

---

## ▶️ How to run

**1. Clone the repository**
```bash
git clone https://github.com/sZagal04/qa-api-testing.git
cd qa-api-testing
```

**2. Install dependencies**
```bash
pip install requests pytest
```

**3. Run all tests**
```bash
pytest create_kit_name_kit_test.py -v
```

---

## ✅ Test Cases

| Test | Scenario | Kit Name Input | Expected Status | Result |
|------|----------|---------------|-----------------|--------|
| `test_1_char` | Minimum valid length | `"a"` (1 char) | 201 | ✅ Pass |
| `test_511_chars` | Maximum valid length | `"a" * 511` chars | 201 | ✅ Pass |
| `test_empty_name` | Empty string | `""` | 400 | ✅ Pass |
| `test_512_chars` | Exceeds max length | `"a" * 512` chars | 400 | ✅ Pass |
| `test_special_chars` | Special characters | `"N%@"` | 201 | ✅ Pass |
| `test_spaces` | Spaces in name | `" A Aaa"` | 201 | ✅ Pass |
| `test_numbers` | Numeric string | `"123"` | 201 | ✅ Pass |
| `test_no_name` | Missing name field | `{}` (empty body) | 400 | ✅ Pass |
| `test_wrong_type` | Wrong data type | `123` (integer) | 400 | ✅ Pass |

**9/9 tests passing — 100% pass rate**

---

## 🧪 Test Design Techniques Applied

- **Boundary Value Analysis** — tested at 1, 511, and 512 characters for the `name` field
- **Equivalence Partitioning** — grouped valid inputs (strings, special chars, numbers) vs invalid (wrong type, empty, missing)
- **Authentication chaining** — each test creates a user via `/api/v1/users/` to obtain an auth token before testing kit creation

---

## 🔗 Related projects

- [UI Automation](https://github.com/sZagal04/qa-automation-urban-routes)
- [Manual Testing](https://github.com/sZagal04/qa-manual-testing)
- [Database Testing](https://github.com/sZagal04/qa-database-testing)
