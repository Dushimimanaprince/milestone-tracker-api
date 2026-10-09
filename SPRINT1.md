# Sprint 1 Review & Retrospective

## 1. Sprint Review (Delivered Product Increment)
- **Sprint Goal:** Deliver core milestone submission and listing functionality with automated unit tests and CI integration.
- **Completed User Stories:**
  - **US-01:** Submit new milestone log via `POST /api/milestones/` (3 Story Points) - Status: **DONE**
  - **US-02:** Retrieve all milestone logs via `GET /api/milestones/` (2 Story Points) - Status: **DONE**
- **Velocity Delivered:** 5 Story Points.
- **Verification & Acceptance Criteria:**
  - `POST /api/milestones/` validates missing fields (returns HTTP 400) and stores valid logs with status `PENDING` (returns HTTP 201).
  - `GET /api/milestones/` serializes milestone records ordered by newest first (returns HTTP 200).
  - 4 automated unit tests executed with 0 failures (`Ran 4 tests in 0.043s - OK`).

---

## 2. Sprint 1 Retrospective (Process Inspection & Adaptation)

### What Went Well
- Slicing stories into small units allowed development and unit testing without blocking dependencies.
- Django's built-in `TestCase` and `Client` provided fast execution times (<0.1s) for regression testing.
- Feature branching kept work isolated from `main`.

### What Didn't Go Well (Bottlenecks)
1. **Lack of Operational Visibility (Logging):** The views process requests silently without console logging. In production, diagnosing failures or tracking request execution requires inspecting raw server state.
2. **Missing Uptime Observability:** There is no lightweight mechanism for monitoring services or load balancers to ping system health without querying the business database.

### Actionable Improvements Committed for Sprint 2
1. **Improvement 1 (Structured Request Logging):** Implement standard Python application logging in views to output ISO timestamps, request methods, paths, and response statuses to stdout.
2. **Improvement 2 (Dedicated Health Monitoring Endpoint):** Deliver `US-03` by building a `/health/` endpoint providing system status and service metadata for automated uptime checks.