# Trading Tool Agent Guidance

## Repository shape

- This is a small, script-first Python project for MT5 trade risk calculation and journal analytics.
- Read [README.md](README.md) for the user-facing purpose and supported analytics.
- Keep changes focused on the script that owns the behavior. The `practice/` files are learning exercises, not shared application modules.

## Working conventions

- Preserve the existing straightforward Python style unless a change requires a clearer reusable function.
- Treat `trading_journal.py` as the journal entry surface, `risk_calculator.py` as the interactive risk calculator, and `Journal_analytics.py` as the MT5 Excel import and statistics surface.
- Keep calculations deterministic and separate from interactive input or file loading when adding reusable behavior.
- Validate numeric input explicitly. Handle empty input, malformed numbers, and invalid calculation states such as a zero stop distance without relying on a bare `except`.
- Do not invent MT5 column names or report structure; follow the mapping and import assumptions documented in the analytics script and README.

## Autofill behavior

When adding or changing autofill behavior:

- Autofill only fields that are missing or explicitly requested; never overwrite a value the user entered.
- Derive values from the current source fields using the existing calculation rules. Make the source-to-derived relationship clear in a named function where practical.
- Recompute dependent fields when a source field changes, while preserving manually edited dependent values if the feature supports overrides.
- Keep autofilled values type-valid and consistent with the surrounding field format. Reject or leave blank values that cannot be derived safely.
- Make defaults deterministic and local to the owning script; do not use hidden global state or external services.
- Test the important cases: all source fields present, one source field missing, explicit user override, malformed input, and division-by-zero or empty-data conditions.

## Validation

- Run `python -m py_compile <changed-file>.py` for every changed Python file.
- Run the changed script manually when its behavior is interactive or depends on an MT5 export; document any required input file or dependency.
- Avoid changing sample data, generated reports, or unrelated practice exercises while implementing a feature.