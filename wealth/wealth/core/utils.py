import locale

def format_currency(value: float, fallback: str = "${:,.2f}") -> str:
    """Formats a float as a localized currency string. Falls back if locale fails."""
    try:
        locale.setlocale(locale.LC_ALL, "")
        return locale.currency(value, grouping=True)
    except Exception:
        return fallback.format(value)
