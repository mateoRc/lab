# Sentinel

## Purpose

A Python CI release guardian that turns engineering evidence into explainable release-risk assessments.

## Implemented

- Change-aware check planning, allowlisted check adapters, deterministic policy, and centralized evidence redaction.
- Markdown, JSON, pull-request, and sanitized runtime reports.
- An analysis-provider interface with a mock provider.

## Design decisions

Deterministic policy owns pass/fail decisions. The analysis provider can explain evidence but cannot override policy or deploy. Sentinel runs in CI, outside the production runtime.

## Status and limits

Active, pre-1.0. The Lab policy is advisory. Production LLM analysis and a protected approval workflow are roadmap items; the current analysis provider is a mock.

Source: [Sentinel](https://github.com/mateoRc/sentinel) · [Architecture](../docs/architecture/sentinel.md) · [Roadmap](../docs/roadmaps/sentinel.md)
