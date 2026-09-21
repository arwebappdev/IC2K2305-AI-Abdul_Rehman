
"""
Experiment 1: Production System
AI Lab - IC-709D

A simple rule-based room temperature controller.
"""


def get_temperature():
    """Accept and validate room temperature."""
    while True:
        try:
            temperature = float(input("Enter room temperature (°C): "))
            if -50 <= temperature <= 60:
                return temperature

            print("Please enter a realistic temperature between -50 and 60.")

        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def production_system(temperature):
    """Apply production rules to determine the required action."""

    rules = [
        {
            "condition": temperature >= 30,
            "rule": "IF temperature >= 30°C",
            "action": "Turn ON the cooling system."
        },
        {
            "condition": temperature <= 18,
            "rule": "IF temperature <= 18°C",
            "action": "Turn ON the heating system."
        },
        {
            "condition": 18 < temperature < 30,
            "rule": "IF temperature is between 18°C and 30°C",
            "action": "No action required. Room temperature is comfortable."
        }
    ]

    for rule in rules:
        if rule["condition"]:
            print("\nProduction Rule Matched:")
            print(rule["rule"])
            print("Action:", rule["action"])
            return

    print("No applicable production rule found.")


def main():
    """Main function."""
    print("=" * 45)
    print("   INTELLIGENT ROOM TEMPERATURE CONTROLLER")
    print("=" * 45)

    temperature = get_temperature()

    print(f"\nCurrent Temperature: {temperature}°C")
    production_system(temperature)


if __name__ == "__main__":
    main()
