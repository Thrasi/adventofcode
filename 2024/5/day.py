import re
from typing import List, Dict, Tuple


class Day:

    def is_valid_page(page_order: List[int], index: int, page: int, rules: set, unique_pages: set) -> Tuple[bool, int, int]:
        for predecessor in rules.get(page,[]):
            if predecessor in unique_pages:
        #         # make sure that the predecessor is before the page
                if page_order.index(predecessor) < index:
                    continue
                else:
                    return False, page_order.index(predecessor), index
            else:
                continue  # maybe update the set of predecessors
        return True, None, None

    def fix_violating_pages(page_order: List[int], rules: Dict[int, set]):
        pages = set(page_order)
        while not Day.is_valid_page_order(page_order, rules):
            for i, page in enumerate(page_order[::-1]):
                valid, violating_index, page_index = Day.is_valid_page(page_order, len(page_order) - i - 1, page, rules, pages)
                if not valid:
                    page_order[violating_index], page_order[page_index] = page_order[page_index], page_order[violating_index]
                
    def is_valid_page_order(page_order: List[int], rules: Dict[int, set]) -> bool:
        pages = set(page_order)
        for i, page in enumerate(page_order[::-1]):
            if not Day.is_valid_page(page_order, len(page_order) - i - 1, page, rules, pages)[0]:
                return False
        return True

    def get_valid_page_orders(page_orders: List[List[int]], rules: Dict[int, set]) -> List[List[int]]:
        return [page_order for page_order in page_orders if Day.is_valid_page_order(page_order, rules)]

    def get_invalid_page_orders(page_orders: List[List[int]], rules: Dict[int, set]) -> List[List[int]]:
        return [page_order for page_order in page_orders if not Day.is_valid_page_order(page_order, rules)]
    
    def get_rules(task_input: str) -> Dict[int, set]:
        rules = {}
        rule_lines = task_input.split("\n\n")[0].splitlines()
        for rule_line in rule_lines:
            [page1, page2] = list(map(int, rule_line.split("|")))
            if page2 in rules:
                rules[page2].add(page1)
            else:
                rules[page2] = {page1}
        return rules
    
    def get_page_orders(task_input: str) -> List[List[int]]:
        page_orders = [ list(map(int, line.split(","))) for line in task_input.split("\n\n")[1].splitlines()]
        return page_orders

    def task1(task_input: str) -> int:
        rules = Day.get_rules(task_input)
        page_orders = Day.get_page_orders(task_input)
        valid_page_orders = Day.get_valid_page_orders(page_orders, rules)
        total = sum([page_order[len(page_order)//2] for page_order in valid_page_orders])
        return total


    def task2(task_input: str) -> int:
        rules = Day.get_rules(task_input)
        page_orders = Day.get_page_orders(task_input)
        invalid_page_orders = Day.get_invalid_page_orders(page_orders, rules)
        for page_order in invalid_page_orders:
            Day.fix_violating_pages(page_order, rules)
            
        total = sum([page_order[len(page_order)//2] for page_order in invalid_page_orders])
        return total
