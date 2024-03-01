# README

Create a habit:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Exercise"}' http://127.0.0.1:5000/habits
```

Get all habits:

```bash
curl http://127.0.0.1:5000/habits
```

Record an event for a habit:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"habit_id": 4}' http://127.0.0.1:5000/events
```

Get all EVENTS:

```bash
curl http://127.0.0.1:5000/events
```
