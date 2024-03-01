import uuid
import datetime

def analyze_uuid(uuid_str):
    """Extract clock sequence and node from the given UUID."""
    uuid_obj = uuid.UUID(uuid_str)
    return uuid_obj.clock_seq, uuid_obj.node

def get_time_from_uuid(uuid_str):
    """Convert UUID string to creation time."""
    uuid_obj = uuid.UUID(uuid_str)
    timestamp_100ns = uuid_obj.time
    timestamp_seconds = timestamp_100ns / 1e7
    start_date = datetime.datetime(1582, 10, 15, tzinfo=datetime.timezone.utc)
    creation_time = start_date + datetime.timedelta(seconds=timestamp_seconds)
    return creation_time

def create_uuid_with_timestamp(timestamp_str, clock_seq, node):
    """Create a new UUID using the given timestamp, clock sequence, and node."""
    dt = datetime.datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
    epoch_start = datetime.datetime(1582, 10, 15, tzinfo=datetime.timezone.utc)
    time_difference = dt - epoch_start
    intervals_since_epoch = int(time_difference.total_seconds() * 10000000)
    time_low = intervals_since_epoch & 0xffffffff
    time_mid = (intervals_since_epoch >> 32) & 0xffff
    time_hi_version = (intervals_since_epoch >> 48) & 0x0fff
    time_hi_version |= (1 << 12)
    clock_seq_hi_and_reserved = (clock_seq >> 8) | 0x80
    clock_seq_low = clock_seq & 0xff
    return uuid.UUID(fields=(time_low, time_mid, time_hi_version, clock_seq_hi_and_reserved, clock_seq_low, node))

# Your UUID
my_uuid_str = "ccfd6950-d0e2-11ee-b66e-f3b504efebdc"

# Analyze your UUID
clock_seq, node = analyze_uuid(my_uuid_str)
print(f"Your UUID ({my_uuid_str}) was created at: {get_time_from_uuid(my_uuid_str)}")

# User-provided timestamp
input_timestamp = "2024-02-21T17:57:44.869Z"

# Generate new UUID
new_uuid = create_uuid_with_timestamp(input_timestamp, clock_seq, node)
print(f"New UUID generated from timestamp {input_timestamp} is: {new_uuid}")
print(f"New UUID was created at: {get_time_from_uuid(str(new_uuid))}")