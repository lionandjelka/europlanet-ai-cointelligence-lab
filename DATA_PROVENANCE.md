# Data provenance and redistribution note

## What is included

This teaching repository contains:

- `data/student_metadata.csv` — 1,457 simulation-metadata rows used in the exercise;
- `data/student_bls_results.csv` — precomputed BLS outputs;
- short deterministic teaching windows (`*.npz`) used for the local-event and mission-board exercises;
- derived classroom scores and challenge tables.

## What is not included

The original large raw simulation products (including the large HDF5 light-curve dataset referenced in the source student project) are **not** present in this teaching package.

## Teaching derivation

The short local-event windows used by the classroom neural sections are generated from the supplied simulation parameters for the purpose of this practical. They must not be described as the original raw simulated light curves.

## Before public redistribution

The scientific data here are synthetic/derived teaching data rather than personal data. Nevertheless, because they originate from a supplied student/project workflow, the repository owner should ensure that they have permission from the relevant project/student contributors to redistribute these derivative tables/windows publicly.

The repository's software license does not override ownership or attribution obligations attached to upstream student/project material.
