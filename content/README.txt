VAULTSH
========

A read-only virtual shell for exploring backend work and project documentation.
Commands operate on mounted portfolio content, never on the host operating system.

VAULTS
------
cv/        Professional profile, skills, and experience
projects/  Project summaries and engineering decisions
docs/      Architecture, APIs, commands, deployment, and roadmaps

START HERE
----------
tree /cv
cat /cv/about.txt
cat /cv/skills.txt
cat /projects/vaultsh.txt
dashboard

This is not a Linux shell. It is a Go backend with a virtual filesystem,
session state, command parsing, pipelines, search, and telemetry integrations.
