tareas_pendientes = [
    'Implementar login',
    'Diseñar pantalla principal',
]

tareas_completadas = [
    'Diseño de base de datos',
]

print('=== TAREAS PENDIENTES ===')

for t in tareas_pendientes:
    print(f'☐ {t}')

print('=== TAREAS COMPLETADAS ===')

for t in tareas_completadas:
    print(f'✓ {t}')