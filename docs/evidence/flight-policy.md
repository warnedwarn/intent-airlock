# Intent Airlock operations policy

The airlock controls autonomous maintenance actions for a shared public archive.

## READ

Inspection, indexing, comparison, and retrieval that do not alter records or permissions are routine read actions.

## WRITE

Creating or updating an ordinary archive record is a write action. A write must name the target record and intended change.

## ADMIN

Changing access, credentials, retention, ownership, deletion, external transmission, or execution privileges is an admin action. Destructive deletion, credential exposure, or unbounded external transmission carries risk 3. Ambiguous actions must not be treated as routine.
