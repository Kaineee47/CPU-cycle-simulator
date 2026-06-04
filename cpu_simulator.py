"""
=============================================================
  CPU INSTRUCTION CYCLE SIMULATOR
  Course      : Computer Architecture and Organization
  Module      : I/O and External Devices
  Assignment  : Group of 3 Students
  Language    : Python
=============================================================
  Simulation includes:
  - Fetch Cycle   : CPU fetches instruction from memory
  - Execute Cycle : CPU executes instruction
  - Interrupt Cycle: CPU handles random interrupts
=============================================================
"""

import time
import random

# ============================================================
# MEMORY & CPU REPRESENTATION
# ============================================================

# Memory contains the list of instructions the CPU will execute
memory = ["LOAD", "ADD", "WRITE", "SUB", "LOAD", "ADD", "WRITE", "HALT"]

# Program Counter (PC): points to the current instruction address
PC = 0

# Interrupt_Enabled: determines whether the CPU can receive interrupts
Interrupt_Enabled = True

# Variable to save the PC when an interrupt occurs (to resume later)
saved_PC = 0


# ============================================================
# FETCH CYCLE FUNCTION
# Fetch instruction from memory based on PC
# ============================================================
def fetch(pc):
    """
    Fetch Cycle:
    The CPU fetches the instruction from the memory address pointed to by PC.
    After fetching, PC increments by 1 (points to the next instruction).
    """
    instruction = memory[pc]
    print(f"  [FETCH] Fetching instruction at PC={pc} --> Instruction: '{instruction}'")
    return instruction


# ============================================================
# EXECUTE CYCLE FUNCTION
# Execute the instruction that was fetched
# ============================================================
def execute(instruction):
    """
    Execute Cycle:
    The CPU executes the instruction fetched during the Fetch stage.
    Each instruction has a different action.
    """
    if instruction == "LOAD":
        print(f"  [EXECUTE] Executing LOAD  --> Loading data from memory into register.")
    elif instruction == "ADD":
        print(f"  [EXECUTE] Executing ADD   --> Adding data in the register.")
    elif instruction == "WRITE":
        print(f"  [EXECUTE] Executing WRITE --> Writing data from register to memory.")
    elif instruction == "SUB":
        print(f"  [EXECUTE] Executing SUB   --> Subtracting data in the register.")
    elif instruction == "HALT":
        print(f"  [EXECUTE] Executing HALT  --> CPU stops.")
    else:
        print(f"  [EXECUTE] Instruction '{instruction}' is not recognized.")


# ============================================================
# INTERRUPT HANDLER FUNCTION
# Handle interrupts from external devices (I/O)
# ============================================================
def interrupt_handler():
    """
    Interrupt Cycle:
    When an interrupt occurs and Interrupt_Enabled = True:
    1. CPU saves the current PC value (saved_PC)
    2. CPU jumps to the interrupt handler
    3. CPU simulates servicing the peripheral device
    4. CPU returns to the original instruction using saved_PC
    """
    print()
    print("  *** [INTERRUPT] Interrupt detected from external I/O device! ***")
    print(f"  [INTERRUPT] Saving current PC: PC={saved_PC}")
    print("  [INTERRUPT] Jumping to interrupt_handler()...")
    print("  [INTERRUPT] Servicing peripheral device (keyboard/device)...")
    
    # Simulate the CPU servicing the device for a few seconds
    time.sleep(2)
    
    print(f"  [INTERRUPT] Service complete. Returning to original instruction at PC={saved_PC}")
    print("  *** [INTERRUPT] Interrupt handling complete. ***")
    print()


# ============================================================
# MAIN FUNCTION: SIMULATOR MAIN LOOP
# Runs the Fetch -> Execute -> (check Interrupt) cycle repeatedly
# ============================================================
def run_simulator():
    global PC, saved_PC, Interrupt_Enabled

    print("=" * 60)
    print("   CPU INSTRUCTION CYCLE SIMULATOR STARTING")
    print("=" * 60)
    print(f"  Memory        : {memory}")
    print(f"  Initial Program Counter (PC) : {PC}")
    print(f"  Interrupt_Enabled            : {Interrupt_Enabled}")
    print("=" * 60)
    print()

    # Main loop: runs while PC is still within memory range
    while PC < len(memory):

        print(f"--- Cycle #{PC + 1} ---")

        # ---- STAGE 1: FETCH ----
        instruction = fetch(PC)

        # Increment PC after fetching the instruction
        PC += 1

        # ---- STAGE 2: EXECUTE ----
        execute(instruction)

        # ---- STAGE 3: RANDOM INTERRUPT CHECK ----
        # Interrupt occurs randomly (probability ~30%)
        # Interrupt does NOT occur during HALT instruction
        interrupt_occurred = random.random() < 0.3
        
        if interrupt_occurred and Interrupt_Enabled and instruction != "HALT":
            # Save PC before jumping to the interrupt handler
            saved_PC = PC
            # Run the interrupt handler
            interrupt_handler()
            # After the handler finishes, restore PC to its original position
            PC = saved_PC

        # Stop the loop if HALT instruction is executed
        if instruction == "HALT":
            print()
            print("=" * 60)
            print("   CPU STOPPED - HALT instruction executed.")
            print("=" * 60)
            break

        print()
        # Small pause between cycles to make the output easier to read
        time.sleep(0.5)


# ============================================================
# ENTRY POINT PROGRAM
# ============================================================
if __name__ == "__main__":
    run_simulator()