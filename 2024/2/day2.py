class Day2:

    def report_is_safe(report: str) -> bool:
        if report[0] == report[1]:
            return False
        increasing = report[1] > report[0]
        for i in range(1, len(report)):
            if report[i] == report[i - 1]:
                return False
            elif 3 >= report[i] - report[i - 1] > 0 and increasing:
                continue
            elif -3 <= report[i] - report[i - 1] < 0 and not increasing:
                continue
            else:
                return False

        return True

    def task1(task_input: str) -> int:
        reports = [list(map(int, report.split())) for report in task_input.splitlines()]
        return sum(map(Day2.report_is_safe, reports))

    def task2(task_input: str) -> int:
        reports = [list(map(int, report.split())) for report in task_input.splitlines()]
        counter = 0
        for report in reports:
            if Day2.report_is_safe(report):
                counter += 1
            else:
                for i in range(len(report)):
                    dampened_report = report[:i] + report[i + 1 :]
                    if Day2.report_is_safe(dampened_report):
                        counter += 1
                        break

        return counter
