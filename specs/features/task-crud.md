# Feature: Task CRUD (Phase I)

## Purpose
Provide basic task management through a command-line interface.

## Task Entity
Each task contains:
- id: integer (auto-increment)
- title: string (required)
- description: string (optional)
- completed: boolean (default false)

## Functional Requirements

### Add Task
- Prompt user for title
- Prompt user for optional description
- Create a task with completed = false
- Assign unique incremental ID

### View Tasks
- Display all tasks
- Show:
  - ID
  - Title
  - Completion status (✔ / ✘)

### Update Task
- Prompt user for task ID
- Allow updating title and/or description
- Keep completion status unchanged

### Delete Task
- Prompt user for task ID
- Remove task from memory

### Toggle Completion
- Prompt user for task ID
- Toggle completed state

## CLI Behavior
- Show menu options continuously until user exits
- Validate user input
- Show friendly messages for success or failure

## Constraints
- No database
- No file system persistence
- Use in-memory Python data structures only
- Python 3.13+


## CLI Behavior (Mandatory)

- The application MUST be interactive
- The application MUST display a menu repeatedly until the user exits
- The application MUST use standard input/output (input(), print())

### Menu Options
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Task Completion
6. Exit

### Interaction Rules
- The user selects actions by entering a number
- The app prompts the user for required inputs
- No automated tests or test scripts are allowed
- No hardcoded test data
- No "All tests passed" output



## Explicit Constraints

- The application MUST NOT contain:
  - Automated test code
  - Hardcoded test cases
  - Debug or verification print statements
- All functionality must be triggered by user interaction only








