def calculate_attendance_probability(
    current_sequence: str, 
    consecutive_absences: int, 
    current_day: int, 
    has_missed_4_days: bool, 
    total_sequences: int, 
    last_day_absent_count: int, 
    total_days: int
) -> tuple[int, int]:
    # If there are already 4 consecutive absences, mark the flag and return current counts
    if consecutive_absences >= 4:
        has_missed_4_days = True
        return total_sequences, last_day_absent_count

    # If we have reached the total number of days, evaluate the sequence
    if current_day == total_days:
        if not has_missed_4_days and current_sequence and current_sequence[-1] == 'A':
            last_day_absent_count += 1
        total_sequences += 1
        return total_sequences, last_day_absent_count

    # Recursively explore both attendance and absence for the next day
    total_sequences, last_day_absent_count = calculate_attendance_probability(
        current_sequence + 'P', 0, current_day + 1, has_missed_4_days, total_sequences, last_day_absent_count, total_days
    )
    total_sequences, last_day_absent_count = calculate_attendance_probability(
        current_sequence + 'A', consecutive_absences + 1, current_day + 1, has_missed_4_days, total_sequences, last_day_absent_count, total_days
    )

    return total_sequences, last_day_absent_count


def compute_attendance_probability(total_days: int) -> tuple[int, int]:
    # Initialize counters for total sequences and sequences where the last day is absent
    total_sequences: int = 0
    last_day_absent_count: int = 0
    total_sequences, last_day_absent_count = calculate_attendance_probability(
        "", 0, 0, False, total_sequences, last_day_absent_count, total_days
    )

    return last_day_absent_count, total_sequences


if __name__ == '__main__':
    days: int = 5
    last_day_absent_count, total_sequences = compute_attendance_probability(days)
    print(f'{last_day_absent_count}/{total_sequences}')
