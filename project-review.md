# AeroCompliance Pro Review

## Summary

The project has a strong aviation operational architecture foundation.
The backend is aircraft-centric, the frontend is structured around domain hooks, and audit/record flows are implemented in key areas.
However, there are a few alignment issues to fix before the system is fully consistent and reliable.

## What aligns well

- `Aircraft` is treated as the operational backbone in the backend.
  - `AircraftDetailSerializer` returns MEL items, AD compliances, maintenance tasks, compliance snapshot, documents, and recent audit logs.
  - The backend exposes aircraft-centric actions such as `aircraft_detail`, `mel_items`, `ad_compliances`, `maintenance_tasks`, `compliance_snapshot`, `documents`, and `audit_history`.
- Audit trail is modeled correctly in the backend.
  - `AuditLog` stores `user`, `aircraft`, `action`, `model_name`, `object_id`, `before`, `after`, and `timestamp`.
  - Audit API supports filtering by `aircraft_id`, `user_id`, `action`, and `model_name`.
- Records upload and listing exist in the frontend.
  - The frontend page posts `FormData` to `/api/records/documents/` with `title`, `description`, `type`, `aircraft`, and `file`.
  - The backend `DocumentViewSet` accepts document uploads and stores them using `DocumentService.upload_document()`.
- The frontend has dedicated hooks and clear endpoint definitions.
  - `frontend/hooks/useAircraft.ts`, `frontend/hooks/useRecords.ts`, and `frontend/features/audits/hooks/use-audit-logs.ts` are consistent with the intended hook-based architecture.

## Key mismatches found

1. Audit filter parameter mismatch
   - Frontend uses `aircraft` and `search` query params in `frontend/features/audits/hooks/use-audit-logs.ts`.
   - Backend audit API expects `aircraft_id` and does not support `search`.
   - This means aircraft filtering and search on the audit page do not actually match backend expectations.

2. Records type input is free-text
   - The frontend document upload form accepts any text for `type`.
   - Backend `Document.type` is a `choices` field with allowed values such as `CRS`, `WORK_ORDER`, `INSPECTION`, `AD_EVIDENCE`, `MEL_EVIDENCE`, and `AMP_EVIDENCE`.
   - Using a dropdown or select list would prevent invalid submissions and make the frontend/backed contract stronger.

3. Documentation status may be stale
   - `frontend/ARCHITECTURE.md` marks some pages as TODO, yet `audits` and `records` pages are already implemented.
   - Keep architecture docs aligned with current implementation to avoid confusion during development.

4. Frontend/backend contract gaps are not fully verified by tests
   - There is no evidence in the review that API contracts are enforced by automated tests.
   - This is important for an aviation-grade traceability and operational system.

## Practical next steps

1. Fix audit filter parameter mapping
   - Update `frontend/features/audits/api/get-audit-logs.ts` to send `aircraft_id` instead of `aircraft`.
   - Either remove the unsupported `search` parameter from the frontend or implement search filtering in the backend.
   - Example: `params.aircraft_id = params.aircraft` before calling the API.

2. Convert the record type input to a dropdown
   - Replace the free-text `type` field in `frontend/app/(protected)/records/page.tsx` with a select list using the backend document type options.
   - This will ensure valid data is submitted and prevent backend validation errors.

3. Sync docs with implementation
   - Update `frontend/ARCHITECTURE.md` to reflect the actual implemented audit and records pages.
   - Add a brief note that audit filtering currently supports `aircraft_id`, `user_id`, `action`, and `model_name` only.

4. Add contract tests for key workflows
   - Add tests for `AuditLogViewSet` query params and `DocumentViewSet` upload behavior.
   - Add frontend integration or API smoke tests to verify aircraft detail payload structure and record upload flows.

5. Review `frontend` audit hook duplication
   - There are two audit hooks: `frontend/hooks/useAuditLogs.ts` and `frontend/features/audits/hooks/use-audit-logs.ts`.
   - Consider consolidating them to reduce confusion and ensure a single source of truth for audit behavior.

## Conclusion

Overall, the system is well-aligned with the design goal of aircraft-centric operational modeling.
Fixing the audit query param mapping, making document type selection explicit, and syncing the docs will bring the application much closer to the intended aviation-grade design.

## Verification: aircraft detail, MEL/AMP, notifications, and tasks

Findings:

- **Aircraft detail endpoints:** Implemented. `AircraftDetailSerializer` exposes `mel_items`, `ad_compliances`, `maintenance_tasks`, `compliance_snapshot`, `documents`, and `audit_logs`. The frontend `useAircraftDetail` hook calls the aircraft detail endpoint and pages render these related sections.

- **MEL domain:** Create and update are implemented. `MELViewSet` uses `MELService.create_mel()` which creates a `MELItem` and records `MELHistory`. `perform_update` delegates to `serializer.save()` so updates are allowed. Missing: update audit logging (no `AuditService` call on MEL updates).

- **AMP tasks:** Creation and update include audit logging. `MaintenanceTaskViewSet` logs create/update via `AuditService` and exposes `by_aircraft`, `active`, and `recalculate_status`. There is a Celery task `recalculate_all_tasks` that recomputes status for tasks across the fleet.

- **Notifications and background tasks:**
  - A notification engine exists: `apps.notifications.tasks.notification_tasks.run_notification_engine` calls `AlertEngine` methods which create notifications.
  - `AlertEngine` creates notifications via `NotificationService.create_notification`, and Celery is configured (`config/celery.py`).
  - **However,** `NotificationService.create_notification` currently only sets `title`, `message`, and `type` — it does not attach `aircraft` or `user` despite callers attempting to pass those values. As a result, notifications created by the engine are not reliably linked to aircraft or users.

- **Frontend consumption / streaming:**
  - The frontend uses polling (React Query `refetchInterval: 30000`) for notifications and audit lists. There is no real-time websocket or event-stream; updates appear within the polling interval.
  - The `run_engine` endpoint triggers `run_notification_engine.delay()` and `recalculate_all_tasks.delay()` so manual runs enqueue Celery tasks; task results are persisted and become visible to the frontend via subsequent polls.

Immediate recommended fixes (high priority):

1. Fix `NotificationService.create_notification` to accept and persist `user` and `aircraft` when provided by the `AlertEngine` (or change `AlertEngine` to pass explicit kwargs matching the service signature). This will ensure notifications are linkable and `by_aircraft` endpoints return expected results.

2. Add audit logging to MEL updates. Either call `AuditService.log_update()` in `MELViewSet.perform_update` or refactor `MELService.update_status` to perform the audit entry.

3. Optional: Add an integration test that runs `run_notification_engine` (in a controlled test environment) and asserts that notifications for a given aircraft are created and visible via the `by_aircraft` API.

4. If near-real-time UX is desired, add a websocket or SSE channel for notifications (or reduce poll interval) — otherwise document the polling behaviour in `frontend/ARCHITECTURE.md`.

Updated next steps in this review:

- Mark notification service linkage bug as high-priority fix.
- Implement MEL audit logging.
- Add an integration test for notification engine results.
