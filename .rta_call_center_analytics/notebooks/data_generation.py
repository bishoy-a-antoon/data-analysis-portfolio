import csv
import random
import uuid
from datetime import datetime, timedelta
from itertools import cycle
from typing import Iterator, Dict, Any


# -------------------------
# Constants
# -------------------------
QUEUES = ("SALES", "SUPPORT", "BILLING")
RESOLUTIONS = ("Resolved", "Unresolved")
SENTIMENTS = ("Negative", "Neutral", "Positive")


# -------------------------
# Helpers
# -------------------------
def generate_uuid() -> str:
    return str(uuid.uuid4())[:12]


def generate_timestamp(start: datetime, seconds: int) -> datetime:
    return start + timedelta(seconds=seconds)


def cycle_enum(values: tuple[str, ...]) -> Iterator[str]:
    return cycle(values)


def bounded_rand(low: int, high: int) -> int:
    return random.randint(low, high)


def maybe_csatscore(sentiment: str) -> float | None:
    match sentiment:
        case "Negative":
            return random.choice([1.0, 2.0, None])
        case "Neutral":
            return random.choice([3.0, 4.0, None])
        case "Positive":
            return random.choice([4.0, 5.0, None])
    return None


def sla_check(wait: int, threshold: int = 20) -> bool:
    return wait <= threshold


# -------------------------
# Core row generator
# -------------------------
def generate_call(
    call_idx: int,
    base_time: datetime,
    queue_cycle: Iterator[str],
    sentiment_cycle: Iterator[str],
) -> Dict[str, Any]:
    ts = generate_timestamp(base_time, call_idx * bounded_rand(5, 15))
    queue = next(queue_cycle)
    sentiment = next(sentiment_cycle)
    wait = bounded_rand(1, 30)
    handle = bounded_rand(180, 600)
    csat = maybe_csatscore(sentiment)
    resolution = random.choice(RESOLUTIONS)

    return {
        "call_id": generate_uuid(),
        "arrival_ts": ts.isoformat(sep=" "),
        "interval_idx": (call_idx // 60) + 1,
        "queue": queue,
        "wait_t": wait,
        "handle_t": handle,
        "sentiment": sentiment,
        "csat": csat,
        "sla_met": sla_check(wait),
        "resolution": resolution,
    }


# -------------------------
# Dataset builder
# -------------------------
def generate_calls(n: int, start: datetime) -> list[Dict[str, Any]]:
    queue_cycle = cycle_enum(QUEUES)
    sentiment_cycle = cycle_enum(SENTIMENTS)
    return [generate_call(i, start, queue_cycle, sentiment_cycle) for i in range(n)]


# -------------------------
# CSV Writer
# -------------------------
def write_csv(data: list[Dict[str, Any]], filepath: str) -> None:
    if not data:
        return
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    start_time = datetime(2025, 8, 1, 0, 0, 0)
    calls = generate_calls(10, start_time)
    write_csv(calls, "../data/raw_calls.csv")
