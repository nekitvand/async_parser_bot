class Checker:

    def create_ready_list_with_strings(self, markets_check: dict) -> list:
        checked_markets = []
        for market in markets_check:
            functions_names_and_values = markets_check.get(market)
            for one_function_name_and_one_value in functions_names_and_values:
                for key, value in one_function_name_and_one_value.items():
                    if value is True:
                        checked_markets.append(f"Есть совпадение в магазине {market} по цвету {key}")
        return checked_markets

    def combine_strings(self,ready_list:list) -> str:
        all_string = "\n".join(ready_list)
        return all_string