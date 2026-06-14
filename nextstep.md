# Next Steps — Modular Plan (3 Steps)

This document divides the remaining work into three modular steps you can run one at a time.
Each step lists concrete sub-tasks, target files, quick acceptance criteria, and suggested commands/tests.

---

## Step 1 — Fix Notification linkage & background processing (High priority)

Goal: Ensure notifications created by the engine are linked to `aircraft` and `user`, and are visible to frontend `by_aircraft` and `pending` endpoints after Celery tasks run.

Sub-tasks:

- Update `NotificationService.create_notification` to accept and persist `aircraft` and `user` (and accept kwargs for future fields).
  - File: `backend/apps/notifications/services/notification_service.py`
  - Example API: `create_notification(title, message, type, aircraft=None, user=None)` and create with provided fields.
- Update `AlertEngine` callers to pass `aircraft` and `user` correctly (e.g., when calling from `run_mel_alerts`, pass `aircraft=item.aircraft` and an appropriate `user` if available).
  - File: `backend/apps/notifications/services/alert_engine.py`
- Add unit test(s) for `NotificationService` to assert `aircraft` and `user` fields are saved.
  - Tests: `backend/apps/notifications/tests/test_notification_service.py`
- Verify `run_engine` triggers Celery tasks and results show up via API polling:
  - Manually trigger: use the HTTP `run_engine` endpoint or call the Celery task locally in tests.

Acceptance criteria:

- Notifications created by `AlertEngine` have `aircraft` and/or `user` set when expected.
- `GET /api/notifications/notifications/by_aircraft/?aircraft_id={id}` returns notifications created by the engine.
- Unit tests cover the service behavior.

Quick commands to run locally (dev):

```bash
# Run Django tests (notifications only)
python -m pytest backend/apps/notifications -q

# Trigger engine via API (example using httpie)
http :8000/api/notifications/notifications/run_engine/ Authorization:"Bearer <token>"
```

Time estimate: 2-4 hours (code + tests)

---

## Step 2 — Add MEL audit logging and validation (Medium priority)

Goal: Ensure MEL updates are auditable and validated so frontend edits are traceable and safe.

Sub-tasks:

- Add audit logging on MEL updates:
  - Option A (quick): In `MELViewSet.perform_update` or `perform_update` hook, call `AuditService.log_update(...)` similar to AMP tasks.
  - Option B (cleaner): Move update logic into `MELService.update_status` and emit audit entries there.
  - Files: `backend/apps/mel/api/views/mel_viewset.py`, `backend/apps/mel/services/mel_service.py`
- Ensure service-level validation on MEL create/update (validate `aircraft_id` exists, status transitions allowed).
  - Add serializer `validate()` methods if needed.
  - Files: `backend/apps/mel/api/serializers/mel_serializer.py`
- Add unit tests for MEL update audit behavior.
  - Tests: `backend/apps/mel/tests/test_mel_audit.py`

Acceptance criteria:

- MEL update actions generate `AuditLog` entries including `user`, `before`, and `after` fields.
- Invalid MEL updates are rejected by serializer/service level validation.

Quick commands:

```bash
python -m pytest backend/apps/mel -q
```

Time estimate: 2-4 hours

---

## Step 3 — Frontend contract cleanup, UI fixes, docs, and tests (Low/Medium priority)

Goal: Align frontend params and UI with backend contracts, add select inputs, consolidate hooks, and add integration checks.

Sub-tasks:

- Fix audit query params in frontend:
  - Update `frontend/features/audits/api/get-audit-logs.ts` and `frontend/features/audits/hooks/use-audit-logs.ts` to send `aircraft_id` (not `aircraft`) and remove unsupported `search` param or map it to a backend-supported filter.
- Change record `type` input to dropdown using backend `Document.Type` options.
  - File: `frontend/app/(protected)/records/page.tsx`
  - Provide Type options in `frontend/lib/constants` or fetch from API if exposed.
- Consolidate duplicate audit hooks: pick one (e.g., `frontend/features/audits/hooks/use-audit-logs.ts`) and remove/redirect the other.
- Update `frontend/ARCHITECTURE.md` to document polling behavior and updated API param expectations.
- Add a lightweight integration test (optional): script or Playwright test that uploads a document, runs `run_engine`, and checks notifications appear in API response.

Acceptance criteria:

- Frontend uses `aircraft_id` and queries return expected data.
- Uploading a document with selected `type` succeeds without validation errors.
- Docs updated to reflect param names and polling strategy.

Quick commands (frontend dev):

```bash
# run frontend dev server
cd frontend
npm install
npm run dev

# run frontend tests (if setup)
npm test
```

Time estimate: 3-6 hours (UI + docs + optional tests)

---

## How to proceed

- Start with Step 1 (notifications) because it fixes a correctness bug that prevents the frontend from seeing engine-created alerts.
- After Step 1 is green, implement Step 2 (MEL audit) to add traceability.
- Finally, complete Step 3 to align frontend behavior and docs and add integration checks.

If you want, I can begin implementing Step 1 now and open PR-style patches for your review.
