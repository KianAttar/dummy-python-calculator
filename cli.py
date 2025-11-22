"""Command-line interface for the calculator."""

import argparse
import sys
from calculator import Calculator, validate_number
from calculator.scientific import (
    sin, cos, tan, log, ln, exp, sqrt, power, PI, E
)


def run_interactive():
    """Run calculator in interactive mode."""
    calc = Calculator()
    print("Calculator CLI - Interactive Mode")
    print("Commands: add, sub, mul, div, clear, history, value, set, quit")
    print("-" * 50)
    
    while True:
        try:
            command = input(">>> ").strip().lower()
            
            if command == 'quit' or command == 'exit':
                print("Goodbye!")
                break
            elif command == 'clear':
                calc.clear()
                print("Cleared")
            elif command == 'history':
                history = calc.get_history()
                if history:
                    for item in history:
                        print(f"  {item}")
                else:
                    print("No history")
            elif command == 'value':
                print(f"Current value: {calc.get_value()}")
            elif command.startswith('set '):
                try:
                    value = validate_number(command.split()[1])
                    calc.set_value(value)
                    print(f"Value set to {value}")
                except (IndexError, ValueError) as e:
                    print(f"Error: {e}")
            elif command.startswith('add '):
                try:
                    value = validate_number(command.split()[1])
                    result = calc.add(value)
                    print(f"Result: {result}")
                except (IndexError, ValueError) as e:
                    print(f"Error: {e}")
            elif command.startswith('sub '):
                try:
                    value = validate_number(command.split()[1])
                    result = calc.subtract(value)
                    print(f"Result: {result}")
                except (IndexError, ValueError) as e:
                    print(f"Error: {e}")
            elif command.startswith('mul '):
                try:
                    value = validate_number(command.split()[1])
                    result = calc.multiply(value)
                    print(f"Result: {result}")
                except (IndexError, ValueError) as e:
                    print(f"Error: {e}")
            elif command.startswith('div '):
                try:
                    value = validate_number(command.split()[1])
                    result = calc.divide(value)
                    print(f"Result: {result}")
                except (IndexError, ValueError, ZeroDivisionError) as e:
                    print(f"Error: {e}")
            elif command.startswith('pow '):
                try:
                    value = validate_number(command.split()[1])
                    result = power(calc.get_value(), value)
                    calc.set_value(result)
                    print(f"Result: {result}")
                except (IndexError, ValueError) as e:
                    print(f"Error: {e}")
            elif command == 'sqrt':
                try:
                    result = sqrt(calc.get_value())
                    calc.set_value(result)
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == 'sin':
                result = sin(calc.get_value())
                calc.set_value(result)
                print(f"Result: {result}")
            elif command == 'cos':
                result = cos(calc.get_value())
                calc.set_value(result)
                print(f"Result: {result}")
            elif command == 'tan':
                result = tan(calc.get_value())
                calc.set_value(result)
                print(f"Result: {result}")
            elif command == 'log':
                try:
                    result = log(calc.get_value())
                    calc.set_value(result)
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == 'ln':
                try:
                    result = ln(calc.get_value())
                    calc.set_value(result)
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == 'exp':
                result = exp(calc.get_value())
                calc.set_value(result)
                print(f"Result: {result}")
            elif command == 'pi':
                calc.set_value(PI)
                print(f"Value set to π: {PI}")
            elif command == 'e':
                calc.set_value(E)
                print(f"Value set to e: {E}")
            elif command == 'help':
                print("Available commands:")
                print("  Basic operations:")
                print("    add <number>  - Add number to current value")
                print("    sub <number>  - Subtract number from current value")
                print("    mul <number>  - Multiply current value by number")
                print("    div <number>  - Divide current value by number")
                print("  Scientific operations:")
                print("    sin           - Sine of current value (degrees)")
                print("    cos           - Cosine of current value (degrees)")
                print("    tan           - Tangent of current value (degrees)")
                print("    log           - Log base 10 of current value")
                print("    ln            - Natural log of current value")
                print("    exp           - e raised to current value")
                print("    sqrt          - Square root of current value")
                print("    pow <number>  - Raise current value to power")
                print("    pi            - Set value to π")
                print("    e             - Set value to e")
                print("  General:")
                print("    set <number>  - Set current value")
                print("    value         - Show current value")
                print("    clear         - Clear value and history")
                print("    history       - Show calculation history")
                print("    quit/exit     - Exit calculator")
            else:
                print("Unknown command. Type 'help' for available commands.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def run_direct(operation, num1, num2):
    """Run a direct calculation."""
    calc = Calculator()
    calc.set_value(num1)
    
    if operation == 'add':
        result = calc.add(num2)
    elif operation == 'subtract':
        result = calc.subtract(num2)
    elif operation == 'multiply':
        result = calc.multiply(num2)
    elif operation == 'divide':
        result = calc.divide(num2)
    else:
        print(f"Unknown operation: {operation}")
        return
    
    print(f"Result: {result}")


def run_cli():
    """Run the calculator CLI with argument parsing."""
    parser = argparse.ArgumentParser(
        description='Calculator CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Interactive mode
  %(prog)s add 5 3                  # Direct calculation: 5 + 3
  %(prog)s divide 10 2              # Direct calculation: 10 / 2
        """
    )
    
    parser.add_argument('operation', nargs='?', 
                       choices=['add', 'subtract', 'multiply', 'divide'],
                       help='Operation to perform')
    parser.add_argument('num1', nargs='?', type=float,
                       help='First number')
    parser.add_argument('num2', nargs='?', type=float,
                       help='Second number')
    
    args = parser.parse_args()
    
    if args.operation and args.num1 is not None and args.num2 is not None:
        run_direct(args.operation, args.num1, args.num2)
    elif args.operation or args.num1 is not None or args.num2 is not None:
        parser.error("For direct calculation, provide: operation num1 num2")
    else:
        run_interactive()


if __name__ == "__main__":
    run_cli()
