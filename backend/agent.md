Build and refactor the AeroCompliance Pro backend domain relationships into a real-world aviation operational architecture.

The backend already exists and is running.

Do NOT rebuild the project.

Your task is to normalize, relate, operationalize, and expose the domains correctly so the system behaves like real CAMO/MRO aviation software instead of isolated CRUD modules.

The goal is to make `Aircraft` the central operational entity while ensuring all domains:

- relate correctly
- expose operationally correct access patterns
- support aviation workflows
- support scalable frontend integration
- preserve traceability and compliance integrity

───────────────────────────────
CORE OBJECTIVE
───────────────────────────────

Refactor all domains so they interconnect operationally the way they do in real aviation environments.

The system must support:

- aircraft-centric operations
- compliance intelligence
- maintenance workflows
- operational dashboards
- audit traceability
- evidence tracking
- notification workflows
- role-based operational access

Frontend integration must become straightforward because backend relationships and access patterns are correctly structured.

Frontend must NOT:

- reconstruct relationships
- manually correlate domains
- compute operational logic
- infer aircraft state

───────────────────────────────
PRIMARY OPERATIONAL ENTITY
───────────────────────────────

`Aircraft` is the operational backbone of the platform.

Every major operational domain must connect to aircraft directly or indirectly where operationally appropriate.

Aircraft must operationally connect to:

- AMP Tasks
- MEL Items
- Airworthiness Directives
- Compliance Snapshots
- Audit Logs
- Document Records
- Notifications
- Maintenance History
- Operational Reports
- User Assignments
- Dashboard Aggregations
- Overview Metadata

───────────────────────────────
REAL AVIATION DOMAIN RELATIONSHIPS
───────────────────────────────

Implement proper aviation-grade relationships.

Examples:

Aircraft
→ has many AmpTasks

Aircraft
→ has many MelItems

Aircraft
→ has many AirworthinessDirectives

Aircraft
→ has one ComplianceSnapshot

Aircraft
→ has many DocumentRecords

Aircraft
→ has many Notifications

Aircraft
→ has many MaintenanceHistory records

Aircraft
→ has many AuditLogs

Aircraft
→ belongs to Operator

Aircraft
→ belongs to AircraftType

Users
→ may manage or be assigned to many Aircraft

AmpTask
→ may reference completed maintenance history

AmpTask
→ may link to evidence documents

MelItem
→ may generate notifications

MelItem
→ may generate audit events

AirworthinessDirective
→ may link to compliance evidence

ComplianceSnapshot
→ aggregates:

- AMP state
- MEL state
- AD state
- operational restrictions
- aircraft readiness
- risk level

Notifications
→ originate from operational events:

- overdue AMP
- MEL expiry
- overdue AD
- aircraft status degradation

AuditLogs
→ track operational changes across all major domains

OperationalReports
→ aggregate operational fleet intelligence

───────────────────────────────
DOMAIN ACCESS ARCHITECTURE
───────────────────────────────

Domains must be exposed and accessed according to real operational workflows.

Do NOT expose domains as disconnected generic CRUD resources.

Examples of proper access patterns:

Aircraft
→ operational root entity

Aircraft detail endpoint should expose:

- overview
- AMP summary
- MEL summary
- AD summary
- compliance snapshot
- maintenance history
- notifications
- audit history
- records
- operational metrics

AMP domain:

- accessible globally
- accessible by aircraft
- filterable by status/operator/due state

MEL domain:

- accessible globally
- accessible per aircraft
- filterable by expiry/severity/status

AD domain:

- accessible fleet-wide
- accessible per aircraft
- filterable by compliance state

Compliance domain:

- accessible fleet-wide
- accessible per aircraft
- treated as operational truth source

Audit domain:

- queryable by:
  - aircraft
  - user
  - operational event
  - timestamp
  - affected domain

Records domain:

- accessible by aircraft
- accessible by linked operational object
- immutable once finalized

Notifications:

- aircraft-linked
- severity-filterable
- operational-event-driven

Users:

- role-based operational access
- aircraft-linked responsibilities where appropriate

───────────────────────────────
RELATIONSHIP + QUERY REQUIREMENTS
───────────────────────────────

Use proper:

- ForeignKey
- OneToOneField
- ManyToManyField
- related_name
- db_index
- select_related
- prefetch_related

Relationships must support:

- reverse querying
- aircraft-centric APIs
- operational dashboards
- scalable aggregation
- future analytics

Avoid:

- disconnected models
- duplicated operational state
- circular dependencies
- frontend-side data stitching

───────────────────────────────
VIEWSET + SERIALIZER REFACTOR
───────────────────────────────

Refactor ViewSets, serializers, services, and querysets so operational manipulation is safe and aviation-grade.

Before any create/update/delete:

- validate linked entities
- validate aircraft linkage
- validate operational consistency
- validate immutable domains
- validate business constraints
- validate relational integrity

Use:

- atomic transactions
- service-layer validation
- serializer validation
- operational guards

Do NOT allow invalid operational writes.

───────────────────────────────
COMPLIANCE ARCHITECTURE
───────────────────────────────

ComplianceSnapshot is the operational truth layer.

Frontend must trust this completely.

Frontend must NEVER calculate:

- airworthiness
- MEL expiry
- AMP due logic
- AD applicability
- operational readiness

Backend computes all operational intelligence.

───────────────────────────────
AUDITABILITY REQUIREMENTS
───────────────────────────────

The platform must remain fully traceable.

Every operational action must preserve:

- who performed it
- what changed
- previous value
- new value
- timestamp
- linked aircraft
- linked operational domain

This is aviation software.

Traceability is mandatory.

───────────────────────────────
FINAL GOAL
───────────────────────────────

The final backend architecture should behave like:

- real CAMO software
- maintenance control infrastructure
- operational compliance intelligence software

NOT:

- disconnected CRUD apps
- isolated domain silos
- generic admin backends

The system must expose clean operational relationships and aircraft-centric access patterns so the frontend can integrate naturally, efficiently, and without duplicating aviation business logic.
