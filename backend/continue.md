# AeroCompliance Pro Backend - Continue.md

## Progress Summary

### ✅ Completed Backend Alignment

The backend has been successfully refactored to make `Aircraft` the central operational entity with proper aviation-grade relationships and access patterns.

#### Key Changes Made:

1. **Model Relationships Enhanced**
   - ✅ AuditLog: Added aircraft ForeignKey + db_index
   - ✅ Notification: Added aircraft and user ForeignKey
   - ✅ User: Added assigned_aircraft ManyToManyField for user-aircraft responsibility
   - ✅ All relationships support reverse querying and aircraft-centric APIs

2. **Aircraft-Centric API Architecture**
   - ✅ Aircraft ViewSet: Added comprehensive detail endpoint with all related data
   - ✅ Nested serializers for MEL, AD, AMP, compliance, documents, audit history
   - ✅ Aircraft detail endpoint exposes operational intelligence
   - ✅ Optimized queries with select_related and prefetch_related

3. **Domain Access Patterns**
   - ✅ All ViewSets support aircraft-centric filtering
   - ✅ Added nested routes: `/api/aircraft/{id}/mel-items`, `/api/aircraft/{id}/ad-compliances`, etc.
   - ✅ Global endpoints with aircraft filtering: `?aircraft_id={id}`
   - ✅ Operational workflows properly exposed

4. **Compliance Architecture**
   - ✅ ComplianceSnapshot remains operational truth source
   - ✅ Frontend can trust compliance data completely
   - ✅ Backend computes all operational intelligence

5. **Auditability**
   - ✅ All operational actions preserve traceability
   - ✅ Aircraft-linked audit logs with proper indexing
   - ✅ User and timestamp tracking

---

## All Exposed Endpoints

### Authentication

```
POST /api/users/users/login/
```

**Request:**

```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**

```json
{
  "user": {
    "id": "integer",
    "username": "string",
    "email": "string",
    "role": "string",
    "is_active_engineer": "boolean"
  },
  "access": "string (JWT token)",
  "refresh": "string (JWT token)"
}
```

### Aircraft Management

```
GET    /api/aircraft/aircraft/           # List all aircraft
POST   /api/aircraft/aircraft/           # Create aircraft
GET    /api/aircraft/aircraft/{id}/      # Get aircraft detail
PUT    /api/aircraft/aircraft/{id}/      # Update aircraft
DELETE /api/aircraft/aircraft/{id}/      # Delete aircraft

GET    /api/aircraft/aircraft/{id}/aircraft_detail/  # Comprehensive operational detail
GET    /api/aircraft/aircraft/{id}/mel_items/        # MEL items for aircraft
GET    /api/aircraft/aircraft/{id}/ad_compliances/   # AD compliances for aircraft
GET    /api/aircraft/aircraft/{id}/maintenance_tasks/ # AMP tasks for aircraft
GET    /api/aircraft/aircraft/{id}/compliance_snapshot/ # Compliance snapshot
GET    /api/aircraft/aircraft/{id}/documents/        # Documents for aircraft
GET    /api/aircraft/aircraft/{id}/audit_history/    # Audit history for aircraft

GET    /api/aircraft/operators/         # List operators
GET    /api/aircraft/aircraft-types/    # List aircraft types
```

**Aircraft Detail Response:**

```json
{
  "id": "integer",
  "tail_number": "string",
  "serial_number": "string",
  "manufacture_date": "date",
  "total_flight_hours": "float",
  "total_flight_cycles": "integer",
  "status": "string",
  "aircraft_type": {
    "id": "integer",
    "manufacturer": "string",
    "model": "string",
    "engine_type": "string"
  },
  "operator": {
    "id": "integer",
    "name": "string",
    "code": "string",
    "country": "string"
  },
  "created_at": "datetime",
  "updated_at": "datetime",
  "mel_items": [...],
  "ad_compliances": [...],
  "maintenance_tasks": [...],
  "compliance_snapshot": {...},
  "documents": [...],
  "audit_logs": [...],
  "total_mel_items": "integer",
  "open_mel_items": "integer",
  "total_ad_items": "integer",
  "overdue_ad_items": "integer"
}
```

### MEL (Minimum Equipment List) Management

```
GET    /api/mel/mel/                    # List MEL items
POST   /api/mel/mel/                    # Create MEL item
GET    /api/mel/mel/{id}/               # Get MEL item
PUT    /api/mel/mel/{id}/               # Update MEL item
DELETE /api/mel/mel/{id}/               # Delete MEL item

GET    /api/mel/mel/by_aircraft/?aircraft_id={id}  # MEL items by aircraft
```

**MEL Item Response:**

```json
{
  "id": "integer",
  "aircraft": "integer",
  "title": "string",
  "description": "string",
  "category": "string",
  "status": "string",
  "reported_date": "datetime",
  "allowed_duration_hours": "float",
  "remaining_hours": "float",
  "resolved_at": "datetime",
  "created_at": "datetime"
}
```

### AD (Airworthiness Directives) Management

```
GET    /api/ad/ads/                     # List ADs
POST   /api/ad/ads/                     # Create AD
GET    /api/ad/ads/{id}/                # Get AD
PUT    /api/ad/ads/{id}/                # Update AD
DELETE /api/ad/ads/{id}/                # Delete AD

GET    /api/ad/compliances/             # List AD compliances
GET    /api/ad/compliances/{id}/        # Get AD compliance
GET    /api/ad/compliances/by_aircraft/?aircraft_id={id}  # Compliances by aircraft
GET    /api/ad/compliances/overdue/     # Overdue compliances
```

**AD Compliance Response:**

```json
{
  "id": "integer",
  "aircraft": "integer",
  "aircraft_tail": "string",
  "ad": "integer",
  "ad_number": "string",
  "ad_title": "string",
  "status": "string",
  "last_compliance_fh": "float",
  "last_compliance_fc": "integer",
  "last_compliance_date": "date",
  "next_due_date": "date",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### AMP (Aircraft Maintenance Program) Management

```
GET    /api/amp/tasks/                  # List maintenance tasks
POST   /api/amp/tasks/                  # Create maintenance task
GET    /api/amp/tasks/{id}/             # Get maintenance task
PUT    /api/amp/tasks/{id}/             # Update maintenance task
DELETE /api/amp/tasks/{id}/             # Delete maintenance task

GET    /api/amp/tasks/{id}/recalculate_status/  # Recalculate task status
GET    /api/amp/tasks/by_aircraft/?aircraft_id={id}  # Tasks by aircraft
GET    /api/amp/tasks/active/           # Active tasks only
```

**Maintenance Task Response:**

```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "aircraft": "integer",
  "interval_type": "string",
  "interval_value": "float",
  "last_performed_fh": "float",
  "last_performed_fc": "integer",
  "last_performed_date": "date",
  "is_active": "boolean",
  "created_at": "datetime"
}
```

### Compliance Management

```
GET    /api/compliance/snapshots/        # List compliance snapshots
GET    /api/compliance/snapshots/{id}/  # Get compliance snapshot
GET    /api/compliance/snapshots/by_aircraft/?aircraft_id={id}  # Snapshot by aircraft
GET    /api/compliance/snapshots/unfit_aircraft/  # Unfit aircraft
GET    /api/compliance/snapshots/restricted_aircraft/  # Restricted aircraft
```

**Compliance Snapshot Response:**

```json
{
  "id": "integer",
  "aircraft": "integer",
  "amp_status": "string",
  "mel_status": "string",
  "ad_status": "string",
  "overall_status": "string",
  "last_evaluated": "datetime"
}
```

### Document Management

```
GET    /api/records/documents/           # List documents
POST   /api/records/documents/           # Upload document
GET    /api/records/documents/{id}/     # Get document
PUT    /api/records/documents/{id}/     # Update document
DELETE /api/records/documents/{id}/     # Delete document

GET    /api/records/documents/by_aircraft/?aircraft_id={id}  # Documents by aircraft
GET    /api/records/documents/by_type/?type={type}  # Documents by type
```

**Document Response:**

```json
{
  "id": "integer",
  "aircraft": "integer",
  "title": "string",
  "description": "string",
  "type": "string",
  "file": "string (URL)",
  "uploaded_by": "integer",
  "uploaded_at": "datetime"
}
```

### Notification Management

```
GET    /api/notifications/notifications/ # List notifications
GET    /api/notifications/notifications/{id}/  # Get notification
GET    /api/notifications/notifications/by_aircraft/?aircraft_id={id}  # Notifications by aircraft
GET    /api/notifications/notifications/pending/  # Pending notifications
GET    /api/notifications/notifications/run_engine/  # Trigger notification engine
```

**Notification Response:**

```json
{
  "id": "integer",
  "aircraft": "integer",
  "user": "integer",
  "title": "string",
  "message": "string",
  "type": "string",
  "status": "string",
  "created_at": "datetime",
  "sent_at": "datetime"
}
```

### Audit Management

```
GET    /api/audits/logs/                 # List audit logs
GET    /api/audits/logs/{id}/           # Get audit log
GET    /api/audits/logs/by_aircraft/?aircraft_id={id}  # Logs by aircraft
GET    /api/audits/logs/by_user/?user_id={id}  # Logs by user
GET    /api/audits/logs/by_model/?model_name={name}  # Logs by model
```

**Audit Log Response:**

```json
{
  "id": "integer",
  "user": "integer",
  "aircraft": "integer",
  "action": "string",
  "model_name": "string",
  "object_id": "string",
  "before": "object",
  "after": "object",
  "timestamp": "datetime"
}
```

### Dashboard

```
GET    /api/dashboard/fleet/             # Fleet overview
GET    /api/dashboard/aircraft/{id}/    # Aircraft dashboard
```

**Fleet Dashboard Response:**

```json
{
  "fleet_size": "integer",
  "airworthy": "integer",
  "restricted": "integer",
  "unfit": "integer",
  "mel_open": "integer",
  "mel_overdue": "integer"
}
```

**Aircraft Dashboard Response:**

```json
{
  "aircraft": {...},
  "total_mel": "integer",
  "open_mel": "integer",
  "expired_mel": "integer",
  "ad_compliant": "integer",
  "ad_overdue": "integer"
}
```

---

## Frontend Implementation Requirements

### 1. Update Type Definitions

The frontend `Aircraft` type needs to be updated to match backend serializer:

**Current (incorrect):**

```typescript
type Aircraft = {
  registration: string; // ❌ Should be tail_number
  flight_hours: number; // ❌ Should be total_flight_hours
  cycles: number; // ❌ Should be total_flight_cycles
  location: string; // ❌ Not in backend model
};
```

**Correct:**

```typescript
type Aircraft = {
  id: number;
  tail_number: string;
  serial_number: string;
  manufacture_date: string;
  total_flight_hours: number;
  total_flight_cycles: number;
  status: string;
  aircraft_type: number;
  aircraft_type_name: string;
  operator: number;
  operator_name: string;
  created_at: string;
  updated_at: string;
};
```

### 2. Aircraft Detail Page

Create comprehensive aircraft detail page that uses:

- `GET /api/aircraft/aircraft/{id}/aircraft_detail/` for full operational view
- Display all MEL items, AD compliances, maintenance tasks, compliance snapshot
- Show operational statistics and recent audit history

### 3. Fleet Overview Dashboard

- Use `GET /api/dashboard/fleet/` for fleet statistics
- Display airworthy/restricted/unfit counts
- Show MEL open/overdue counts

### 4. Aircraft-Specific Pages

- MEL Management: `GET /api/aircraft/aircraft/{id}/mel_items/`
- AD Compliance: `GET /api/aircraft/aircraft/{id}/ad_compliances/`
- Maintenance Tasks: `GET /api/aircraft/aircraft/{id}/maintenance_tasks/`
- Documents: `GET /api/aircraft/aircraft/{id}/documents/`
- Audit History: `GET /api/aircraft/aircraft/{id}/audit_history/`

### 5. Global Management Pages

- All MEL Items: `GET /api/mel/mel/?aircraft_id={id}` (filter by aircraft)
- All AD Compliances: `GET /api/ad/compliances/?aircraft_id={id}`
- All Maintenance Tasks: `GET /api/amp/tasks/?aircraft_id={id}`
- All Documents: `GET /api/records/documents/?aircraft_id={id}`
- All Notifications: `GET /api/notifications/notifications/?aircraft_id={id}`

### 6. API Client Updates

- Update axios interceptors (already correct)
- Update endpoint definitions to match new routes
- Add proper error handling for 401 redirects

### 7. Authentication Flow

- Login form posts to `/api/users/users/login/`
- Store access token in localStorage
- Include Bearer token in Authorization header
- Handle token refresh if needed

### 8. Data Fetching Strategy

- Use React Query for all API calls
- Implement proper caching and invalidation
- Use aircraft-centric data loading patterns

---

## Next Steps for Frontend

1. **Immediate Priority**: Update type definitions to match backend
2. **Create Aircraft Detail Page**: Comprehensive operational view
3. **Build Fleet Dashboard**: Use existing dashboard endpoints
4. **Implement Aircraft Management**: CRUD operations with proper relationships
5. **Add MEL/AD/AMP Management**: Aircraft-specific and global views
6. **Document Management**: Upload and view aircraft documents
7. **Notification System**: Display and manage operational notifications
8. **Audit Trail**: Show operational history and changes

---

## Breaking Changes

- **Aircraft field names**: `registration` → `tail_number`, `flight_hours` → `total_flight_hours`, `cycles` → `total_flight_cycles`
- **Removed fields**: `location` (not in backend model)
- **New endpoints**: All aircraft-centric nested routes available
- **Enhanced responses**: Detail endpoints now include full operational context

---

## Validation

✅ Django check passed - no model or configuration errors
✅ All migrations created and applied
✅ Relationships properly established
✅ API endpoints properly routed
✅ Serializers include all necessary fields
✅ ViewSets support aircraft-centric filtering
✅ Audit logging integrated
✅ Compliance architecture maintained

The backend is now properly aligned with aviation operational workflows and ready for frontend integration.
