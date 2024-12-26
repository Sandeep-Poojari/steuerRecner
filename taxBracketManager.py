# Class maitiaining the tax bracket
class TaxBracketManager:
    TAX_BRACKETS = {
        2024: [
            (0, 11784, lambda x: 0.0),
            (11785, 17005, lambda x: (954.80 * ((x - 11784) / 10000) + 1400) * ((x - 11784) / 10000)),
            (17006, 66760, lambda x: (181.19 * ((x - 17005) / 10000) + 2397) * ((x - 17005) / 10000) + 991.21),
            (66761, 277825, lambda x: 0.42 * x - 10636.31),
            (277826, float('inf'), lambda x: 0.45 * x - 18971.06),
        ],
        2023: [
            (0, 11500, lambda x: 0.0),
            (11501, 16500, lambda x: (950.00 * ((x - 11500) / 10000) + 1350) * ((x - 11500) / 10000)),
            (16501, 65500, lambda x: (180.00 * ((x - 16500) / 10000) + 2300) * ((x - 16500) / 10000) + 950.00),
            (65501, 270000, lambda x: 0.41 * x - 10500.00),
            (270001, float('inf'), lambda x: 0.44 * x - 18000.00),
        ],
    }

    @classmethod
    def get_tax_brackets(cls, year: int):
        if year in cls.TAX_BRACKETS:
            return cls.TAX_BRACKETS[year]
        raise ValueError(f"No tax brackets defined for the year {year}")

