# Final Assessment: Agile & DevOps in Practice
**Project:** Milestone & Logbook Tracker API  
**Framework:** Django / Python  
**Author:** Dushimimana Prince 

---

## 1. Product Vision
To provide a reliable, lightweight REST service that allows students to record academic internship milestones and enables supervisors to review and verify entries in real time, streamlining logbook auditing.

---

## 2. Definition of Done (DoD)
A backlog item is declared "Done" if and only if:
1. All defined Acceptance Criteria for the story are fully implemented.
2. Code follows PEP8 guidelines without syntax errors or unhandled exceptions.
3. Automated unit/integration tests are implemented using Django's test framework with 0 test failures.
4. The GitHub Actions CI pipeline passes automatically (green checkmark).
5. Code is submitted through a feature branch and merged into `main` via a Pull Request.
6. The endpoint JSON response structure is documented.

---

## 3. Product Backlog (Prioritized & Estimated)
Estimations use relative sizing based on the Fibonacci scale (1, 2, 3, 5, 8) evaluating effort, complexity, and risk.

| ID | Priority | User Story | Story Points | Target Iteration |
|---|---|---|:---:|:---:|
| **US-01** | High | **As a student**, I want to submit a new milestone log (`title`, `description`, `student_id`), **so that** my work is stored for auditing. | 3 | **Sprint 1** |
| **US-02** | High | **As a student/supervisor**, I want to retrieve all logged milestones via `GET /api/milestones/`, **so that** I can review ongoing progress. | 2 | **Sprint 1** |
| **US-03** | Medium | **As a DevOps engineer**, I want a `/health/` endpoint returning JSON system status, **so that** automated health probes can verify service uptime. | 1 | **Sprint 2** |
| **US-04** | High | **As a supervisor**, I want to update the status of a log (`APPROVED` / `REJECTED`), **so that** I can formally verify student entries. | 3 | **Sprint 2** |
| **US-05** | Low | **As a user**, I want to query milestones filtered by status (`?status=APPROVED`), **so that** I can isolate verified logs. | 2 | Future Backlog |

---

## 4. Acceptance Criteria

### US-01: Create Milestone Log
- **Given** valid JSON `{"title": "Sprint 0 Setup", "description": "Configured repository", "student_id": "ST101"}`,
- **When** a `POST` request is sent to `/api/milestones/`,
- **Then** respond with HTTP `201 Created`, status `PENDING`, and auto-generated `id`.
- **Given** missing required fields (`title` or `student_id`),
- **Then** respond with HTTP `400 Bad Request`.

### US-02: Retrieve All Milestone Logs
- **When** a `GET` request is sent to `/api/milestones/`,
- **Then** respond with HTTP `200 OK` and a JSON array of all milestone objects.

### US-03: System Health Check Endpoint
- **When** a `GET` request is sent to `/health/`,
- **Then** respond with HTTP `200 OK` and payload `{"status": "healthy", "service": "milestone-tracker-api"}`.

### US-04: Update Milestone Status
- **When** a `PATCH` request is sent to `/api/milestones/<id>/` with `{"status": "APPROVED"}`,
- **Then** respond with HTTP `200 OK` and updated status.
- **Given** an invalid ID,
- **Then** respond with HTTP `404 Not Found`.

---

## 5. Sprint Breakdowns

### Sprint 1 Scope (Planned Effort: 5 Story Points)
- **Goal:** Deliver minimum viable log submission and retrieval with automated CI testing.
- **Selected Items:** US-01 (3 pts) and US-02 (2 pts).

### Sprint 2 Scope (Planned Effort: 4 Story Points)
- **Goal:** Add administrative audit controls, system health observability, and apply Sprint 1 retrospective fixes.
- **Selected Items:** US-03 (1 pt) and US-04 (3 pts).
