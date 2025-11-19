"""Main entry point for the calculator application."""

import sys
import argparse


def main():
    """Main function to launch the calculator."""
    parser = argparse.ArgumentParser(
        description='Python Calculator - GUI and CLI modes',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--cli', action='store_true', 
                       help='Use CLI mode (interactive)')
    parser.add_argument('--gui', action='store_true', 
                       help='Use GUI mode (default)')
    
    args = parser.parse_args()
    
    if args.cli:
        from cli import run_cli
        run_cli()
    else:
        # Default to GUI mode
        try:
            from gui.main_window import run_gui
            run_gui()
        except ImportError:
            print("GUI not yet implemented. Use --cli for CLI mode.")
            print("Example: python main.py --cli")
            sys.exit(1)


if __name__ == "__main__":
    main()
