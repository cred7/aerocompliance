```txt
AEROCOMPLIANCE-PRO/
│
├── backend/
│   │
│   ├── config/
│   │   ├── settings/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── dev.py
│   │   │   ├── prod.py
│   │   │   └── test.py
│   │   │
│   │   ├── __init__.py
│   │   ├── urls.py
│   │   ├── celery.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── apps/
│   │   │
│   │   ├── users/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── aircraft/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   │   ├── aircraft.py
│   │   │   │   ├── operator.py
│   │   │   │   ├── aircraft_type.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── api/
│   │   │   │   ├── views.py
│   │   │   │   ├── urls.py
│   │   │   │   └── routers.py
│   │   │   │
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── amp/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   │   ├── amp_task.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── mel/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   │   ├── mel_item.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── ad/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   │   ├── airworthiness_directive.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── compliance/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   │   ├── compliance_snapshot.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── notifications/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   │   ├── notification.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── records/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   │   ├── document_record.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── audits/
│   │   │   ├── migrations/
│   │   │   ├── models/
│   │   │   │   ├── audit_log.py
│   │   │   │   └── __init__.py
│   │   │   │
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── permissions/
│   │   │   ├── filters/
│   │   │   ├── tasks/
│   │   │   ├── tests/
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   ├── dashboards/
│   │   │   ├── api/
│   │   │   ├── services/
│   │   │   ├── selectors/
│   │   │   ├── serializers/
│   │   │   ├── tests/
│   │   │   ├── apps.py
│   │   │   └── README.md
│   │   │
│   │   └── common/
│   │       ├── models/
│   │       ├── enums/
│   │       ├── constants/
│   │       ├── mixins/
│   │       ├── utils/
│   │       └── validators/
│   │
│   ├── core/
│   │   ├── authentication/
│   │   ├── permissions/
│   │   ├── middleware/
│   │   ├── exceptions/
│   │   ├── pagination/
│   │   ├── validators/
│   │   └── utils/
│   │
│   ├── requirements/
│   │   ├── base.txt
│   │   ├── dev.txt
│   │   └── prod.txt
│   │
│   ├── static/
│   ├── media/
│   ├── tests/
│   │
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── Makefile
│   ├── manage.py
│   └── README.md
│
│
├── frontend/
│   │
│   ├── app/
│   │   │
│   │   ├── login/
│   │   │   └── page.tsx
│   │   │
│   │   ├── (protected)/
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   │
│   │   │   ├── aircraft/
│   │   │   │   ├── page.tsx
│   │   │   │   │
│   │   │   │   └── [id]/
│   │   │   │       ├── layout.tsx
│   │   │   │       ├── page.tsx
│   │   │   │       │
│   │   │   │       ├── amp/
│   │   │   │       │   └── page.tsx
│   │   │   │       │
│   │   │   │       ├── mel/
│   │   │   │       │   └── page.tsx
│   │   │   │       │
│   │   │   │       ├── ad/
│   │   │   │       │   └── page.tsx
│   │   │   │       │
│   │   │   │       ├── records/
│   │   │   │       │   └── page.tsx
│   │   │   │       │
│   │   │   │       └── audits/
│   │   │   │           └── page.tsx
│   │   │   │
│   │   │   ├── compliance/
│   │   │   │   └── page.tsx
│   │   │   │
│   │   │   ├── notifications/
│   │   │   │   └── page.tsx
│   │   │   │
│   │   │   ├── records/
│   │   │   │   └── page.tsx
│   │   │   │
│   │   │   └── audits/
│   │   │       └── page.tsx
│   │   │
│   │   ├── globals.css
│   │   └── layout.tsx
│   │
│   ├── features/
│   │   │
│   │   ├── aircraft/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   ├── amp/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   ├── mel/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   ├── ad/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   ├── compliance/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   ├── notifications/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   ├── dashboard/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   ├── records/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   ├── audits/
│   │   │   ├── api/
│   │   │   ├── hooks/
│   │   │   ├── components/
│   │   │   └── types/
│   │   │
│   │   └── users/
│   │       ├── api/
│   │       ├── hooks/
│   │       ├── components/
│   │       └── types/
│   │
│   ├── components/
│   │   ├── auth/
│   │   ├── layout/
│   │   ├── ui/
│   │   └── shared/
│   │
│   ├── lib/
│   │   ├── api.ts
│   │   ├── endpoints.ts
│   │   ├── token.ts
│   │   ├── utils.ts
│   │   └── constants.ts
│   │
│   ├── providers/
│   │   └── query-provider.tsx
│   │
│   ├── types/
│   │   ├── api.ts
│   │   ├── pagination.ts
│   │   └── common.ts
│   │
│   ├── public/
│   │
│   ├── .env.local
│   ├── .gitignore
│   ├── components.json
│   ├── middleware.ts
│   ├── next.config.ts
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   └── README.md
│
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── deployment/
│   └── compliance/
│
├── infrastructure/
│   ├── nginx/
│   ├── docker/
│   ├── postgres/
│   └── redis/
│
├── scripts/
│
├── .gitignore
├── docker-compose.yml
├── LICENSE
└── README.md
```
