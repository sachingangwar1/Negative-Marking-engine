# Negative Marking Engine

## 📌 Overview

The Negative Marking Engine is a backend component that calculates a candidate's final score by applying penalties for incorrect answers. It is commonly used in online examinations, quizzes, and assessment platforms.

---

## 🎯 Objective

Calculate the final score based on:

- Number of correct answers
- Number of wrong answers
- Negative marking rules

This feature helps ensure fair evaluation and discourages random guessing.

---

## 🛠️ Scoring Logic

### Formula

Final Score = Correct Answers − (Wrong Answers × 0.25)

### Marking Scheme

| Answer Type | Marks |
|------------|--------|
| Correct | +1 |
| Wrong | -0.25 |

---

## 📥 Input Example

```json
{
  "correct": 8,
  "wrong": 2
}
```

## 📤 Output Example

```json
{
  "final_score": 7.5
}
```

### Calculation

```text
8 - (2 × 0.25)
= 8 - 0.5
= 7.5
```

---

## ⚙️ Edge Cases

### Missing Values

Input:

```json
{}
```

Output:

```json
{
  "final_score": 0
}
```

### Negative Final Score

Input:

```json
{
  "correct": 0,
  "wrong": 10
}
```

Output:

```json
{
  "final_score": -2.5
}
```

### No Wrong Answers

Input:

```json
{
  "correct": 5,
  "wrong": 0
}
```

Output:

```json
{
  "final_score": 5
}
```

---

## 🏗️ Project Structure

```text
negative-marking-engine/
│
├── app.py
├── score.py
├── test_score.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/negative-marking-engine.git
cd negative-marking-engine
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Server starts on:

```text
http://localhost:5000
```

---

## API Endpoint

### Calculate Score

**POST** `/calculate-score`

### Request Body

```json
{
  "correct": 8,
  "wrong": 2
}
```

### Response

```json
{
  "final_score": 7.5
}
```

---

## 🧪 Testing

Run unit tests:

```bash
python -m unittest test_score.py
```

Expected result:

```text
Ran 4 tests

OK
```

---

## ✅ Acceptance Criteria

- Consistent scoring logic
- Negative marking applied correctly
- Missing values handled
- Negative scores supported
- Input validation included
- Unit tests available

---

## 📅 Timeline

**Difficulty:** Easy

**Estimated Duration:** 1 Week

---

## Future Enhancements

- Configurable penalty values
- Support for multiple exam patterns
- Database integration
- Score analytics dashboard
- REST API authentication

---

## License

This project is available for educational and learning purposes.
