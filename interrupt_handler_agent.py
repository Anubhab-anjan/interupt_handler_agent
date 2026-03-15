import signal
import time
import sys

class InterruptHandlerAgent:
    def __init__(self):
        self.running = True
        signal.signal(signal.SIGINT, self.handle_interrupt)
        signal.signal(signal.SIGTERM, self.handle_interrupt)

    def handle_interrupt(self, signum, frame):
        print(f"\n[Agent] Interrupt received (Signal: {signum})")
        print("[Agent] Performing cleanup...")
        self.cleanup()
        self.running = False

    def cleanup(self):
        print("[Agent] Cleanup complete.")

    def run(self):
        print("[Agent] Agent started. Press Ctrl+C to interrupt.")
        while self.running:
            print("[Agent] Working...")
            time.sleep(2)
        print("[Agent] Agent stopped safely.")
        sys.exit(0)

if __name__ == "__main__":
    agent = InterruptHandlerAgent()
    agent.run()
