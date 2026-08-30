# Directive Template: [Task Name]

## 1. Goal
Provide a clear, high-level description of what this workflow accomplishes.

## 2. Inputs
- Parameters, files, environment variables, or URLs required to run the task.
- Example: Target URL, output destination, API keys needed.

## 3. Execution Tools & Scripts
- Script(s) in `execution/` used to perform this task deterministically.
- Example: `execution/sample_task.py`

## 4. Expected Outputs & Deliverables
- **Deliverables**: Cloud-based links, Google Sheets, Google Slides, or target destination.
- **Intermediates**: Any files temporarily saved in `.tmp/` during processing.

## 5. Step-by-Step Procedure (SOP)
1. Step 1: Validate prerequisites and required environment variables in `.env`.
2. Step 2: Run execution script with appropriate arguments.
3. Step 3: Handle output and save intermediate processing data to `.tmp/`.
4. Step 4: Verify results and publish/upload deliverable.

## 6. Edge Cases & Learnings (Self-Annealing)
- Record API rate limits, timeouts, common error responses, and mitigation strategies learned over time.
