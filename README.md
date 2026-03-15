Interrupt Handler Agent (Python 3)
Overview

This project implements a basic interrupt handler agent in Python 3.
The agent runs continuously and safely handles system interrupts such as Ctrl + C (SIGINT) and termination signals (SIGTERM) by performing cleanup before exiting.

Features

Handles OS-level interrupts

Graceful shutdown mechanism

Simple agent-based structure

Written in pure Python 3

Requirements

Python 3.6 or higher

Works on Linux, macOS, and Windows (limited to SIGINT on Windows)

File Structure
.
├── interrupt_handler_agent.py
└── README.md
Usage

Save the code as:

interrupt_handler_agent.py

Run the agent:

python3 interrupt_handler_agent.py

Interrupt execution using:

Ctrl + C
Sample Output
[Agent] Agent started. Press Ctrl+C to interrupt.
[Agent] Working...
[Agent] Working...

^C
[Agent] Interrupt received (Signal: 2)
[Agent] Performing cleanup...
[Agent] Cleanup complete.
[Agent] Agent stopped safely.
How It Works

The agent registers signal handlers using Python’s signal module.

When an interrupt occurs, the handler function is triggered.

Cleanup operations are executed before the program terminates.

Customization

You can extend the agent by:

Adding resource management (files, sockets, databases)

Running background tasks

Integrating logging instead of print statements

Adding multi-threading or async execution

License

This project is open-source and free to use for educational purposes
