{{- define "aerocompliance-pro.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- define "aerocompliance-pro.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "aerocompliance-pro.labels" -}}
app.kubernetes.io/name: {{ include "aerocompliance-pro.name" . }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}
