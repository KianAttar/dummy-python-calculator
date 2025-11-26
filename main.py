"""Main entry point for the calculator application.

This module provides the entry point for launching the calculator application
in either GUI or CLI mode.

Usage:
    python main.py           # Launch GUI (default)
    python main.py --gui     # Launch GUI explicitly
    python main.py --cli     # Launch CLI interactive mode
"""

import sys
import argparse


def main():
    """Main function to launch the calculator.
    
    Parses command-line arguments and launches the appropriate interface
    (GUI or CLI) based on user preference.
    """
    parser = argparse.ArgumentParser(
        prog='python-calculator',
        description='Python Calculator - A comprehensive calculator with GUI and CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s              Launch GUI calculator
  %(prog)s --cli        Launch CLI interactive mode
        """
    )
    parser.add_argument(
        '--cli',
        action='store_true',
        help='Use CLI mode (interactive)'
    )
    parser.add_argument(
        '--gui',
        action='store_true',
        help='Use GUI mode (default)'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    args = parser.parse_args()
    
    if args.cli:
        from cli import run_cli
        run_cli()
    else:
        # Default to GUI mode
        try:
            from gui.main_window import run_gui
            run_gui()
        except ImportError as e:
            print("Error: GUI dependencies not available.")
            print("Please install required packages: uv sync")
            print("\nAlternatively, use CLI mode: python main.py --cli")
            sys.exit(1)
        except Exception as e:
            print(f"Error launching GUI: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
