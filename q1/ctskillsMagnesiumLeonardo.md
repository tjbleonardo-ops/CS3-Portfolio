# Computational Thinking Exercise
## [Smart Vending Machine]
**Name:** Thomasse Jakob B. Leonardo
**Section:** Magnesium
**Last Name:** Leonardo
**Date:** 18/08/26
---

## Step 1: Identify the Big Problem
### Main Problem
The school vending machine is prone to user operational errors, 
gives incorrect change, has lack of current stock notifications, 
and has slow performance during heavy user usage.
---
## Step 2: Identify the Sub-Problems
1. Incorrect change calculation

2. Lack of current stock notifications

3. Slow performance during heavy user usage or input.

4. Bad interface or unfriendly interface that causes user error.

---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Incorrect change calculation | Algorithm Design | Fix the order of calculation by calculating change = payment - item price, while also using an if statement to check if change is less than 0, to check for insufficient money.|
| Lack of current stock notifications | Pattern Recognition | Track current stock on a list or database to check if any of the racks of the vending machine is empty, and then sending a message to maintenance which rack to fix the issue. |
| Slow performance during heavy user usage or input. | Decomposition | Split processes of multiple students into parallel tasks, like processing change while preparing the item to be dispensed.  |
| Bad interface or unfriendly interface that causes user error. | Abstraction | Simplify user interface or make the interactable inputs for the vending machine much simpler to understand and less prone to accidentally press a different input. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Incorrect change calculation

### Pseudocode
START

DISPLAY Items AND Item Price AND Item Count per Rack
FOR EVERY Items
  CHECK Item Count per Rack

  IF Item Count per Rack == 0:
    SEND message to Maintenance about Item Unavailable
    DISPLAY "Item Unavailable, please ask maintenance for help"
  END IF

IF Payment < Item Price:
  DISPLAY "Insufficient Payment"
  GIVE Payment
ELSE:
  SET Change = Payment < Item Price
  If Change <= Change in Vending Machine:
    GIVE Item
    Give Change
    CHANGE Item Count per Rack of Rack X
  ELSE
    SEND message to Maintenance about Change
    DISPLAY "There is no change in the Vending Machine, proceed to the Cashier to get your exact change."
    GIVE Payment
  END IF
END IF

END
---
