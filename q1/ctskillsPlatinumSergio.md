# Computational Thinking Exercise
## Smart School Canteen Queue

**Name:** Shanaye Brielle B. Sergio

**Section:** Platinum

**Last Name:** Sergio

**Date:** August 15, 2026

---

## Step 1: Identify the Big Problem
### Main Problem
The system struggles to keep up with transactions and orders due to the overwhelming queue of students and teachers at the canteen.
---
## Step 2: Identify the Sub-Problems
1. The system/internet may crash due to the overwhelming amount of orders.
2. Student-and-teacher users may accidentally swap, have duplicates, or lack items from their orders due to system errors.
3. Menu items may become unavailable for users and lead to shortages.
4. The cashier will have difficulty with calculations due to its slow, manual process.
---
## Step 3: Apply Computational Thinking Skills
| System/Internet Crash | Decomposition | Use data backups or revert back to manual queueing until data connectivity is restored. |

| Order Mix-Ups for Student and Teacher Users| Algorithm Design | Use automated user verification and data-matching programs that can ensure no mix-ups. |

| Menu Item Shortage | Pattern Recognition | Use a digital inventory that deletes unavailable items from the options. |

| Slow and Manual Calculations | Algorithm Design | Simplify manual calculations by creating an algorithm with a repeating, logical sequence. |

---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
3. Menu items may become unavailable for users and lead to a shortage.
### Pseudocode
START
 FOR EACH item IN menu_list DO
    current_stock = check_inventory(item.id)
    
    IF current_stock <= 0 THEN
      REMOVE item FROM visible_menu_options
    ELSE
      DISPLAY item ON visible_menu_options
    ENDIF
    
  ENDFOR
  
END

---
