# Design Documents
(Diagrams are in Mermaid - GitHub renders them automatically.)

## System Architecture
```mermaid
flowchart LR
    U[User] --> G[gui.py - Tkinter UI]
    G --> V[validators.py]
    G --> C[calculator.py]
    G --> H[history.py]
    V --> CFG[config.py]
    C --> CFG
    H --> CFG
    H --> CSV[(data/results.csv)]
    G --> L[logger_setup.py] --> LOG[(logs/app.log)]
```

## Workflow
```mermaid
flowchart TD
    A[Start] --> B[Enter name and 4 marks]
    B --> C[Click Calculate]
    C --> D{Valid numbers 0-100?}
    D -- No --> E[Show error dialog] --> B
    D -- Yes --> F{Any mark < 35?}
    F -- Yes --> G[Result FAIL, Grade F]
    F -- No --> H[Result PASS, grade from percentage]
    G --> I[Display result]
    H --> I
    I --> J{Save record?}
    J -- Yes --> K[Append to CSV]
    J -- No --> L[End]
    K --> M[View History and analytics] --> L
```

## Use Case Diagram
```mermaid
flowchart LR
    T((Teacher / Student))
    T --- UC1[Enter marks]
    T --- UC2[Calculate result and grade]
    T --- UC3[Save record]
    T --- UC4[View history and class report]
    T --- UC5[Clear history]
```

## Sequence Diagram (Calculate & Save)
```mermaid
sequenceDiagram
    actor User
    participant GUI as AnalyzerApp
    participant V as validators
    participant C as calculator
    participant H as history
    User->>GUI: click Calculate
    GUI->>V: parse_marks(entries)
    V-->>GUI: marks / ValidationError
    GUI->>C: calculate_result(marks)
    C-->>GUI: Result
    GUI-->>User: show result text
    User->>GUI: click Save Record
    GUI->>H: save_record(name, marks, result)
    H-->>GUI: saved to CSV
```

## Class / Component Diagram
```mermaid
classDiagram
    class AnalyzerApp {
        +calculate()
        +clear()
        +save()
        +show_history()
    }
    class ValidationError { +title +message }
    class Result { +total +percentage +grade +result }
    AnalyzerApp ..> ValidationError
    AnalyzerApp ..> Result
    AnalyzerApp ..> validators
    AnalyzerApp ..> calculator
    AnalyzerApp ..> history
    class validators { +parse_marks() }
    class calculator { +calculate_result() +calculate_grade() +format_result() }
    class history { +save_record() +load_records() +summarize() +clear_history() }
```

## Storage Design (CSV schema) & ER
```mermaid
erDiagram
    STUDENT_RESULT {
        string timestamp
        string name
        float Physics
        float Chemistry
        float Mathematics
        float English
        float total
        float percentage
        string grade
        string result
    }
```

## Design decisions & rationale
- **GUI separated from logic:** `calculator` and `validators` have no Tkinter code, so they can be unit tested.
- **Config file:** pass mark, grade bands and colours live in one place.
- **CSV storage:** simple, human-readable, no database needed for this scale.
- **Custom exception:** the GUI shows the same dialog titles/messages as the original app.
