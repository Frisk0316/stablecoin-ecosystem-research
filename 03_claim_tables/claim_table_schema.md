# Claim Table Schema

Every major research statement in the final report should be traceable to the master claim table.

Required fields:

- `claim_id`: Stable unique identifier.
- `claim`: The research claim written as a complete sentence.
- `source_id`: Must exist in `01_sources/source_registry.csv` or be explicitly marked as pending.
- `page_or_section`: Page number, section, or HTML heading.
- `evidence`: Short description of the supporting evidence.
- `confidence`: `high`, `medium`, or `low`.
- `notes`: Caveats, source quality, or next extraction step.

Rules:

1. Do not use news or issuer marketing alone for high-stakes conclusions unless marked as issuer claim.
2. Do not write `audit` when the source only supports `attestation`, `assurance`, or `reserve report`.
3. Do not treat SWIFT as a funds-settlement system.
4. Do not treat raw on-chain transfer volume as real payment volume.
5. If a claim relies on dynamic HTML, preserve access date or local HTML copy path.
