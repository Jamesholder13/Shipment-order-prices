#!/usr/bin/env python
# coding: utf-8

# In[ ]:


weight = 90
#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
# more calculation
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
# more calculation
elif weight <= 10:
  cost_ground = weight + 4.0 + 20
# more calculation  
elif weight > 10:
  cost_ground = weight +2.20 + 20
# more calculation  
else: 
  answer = "Error"
#last calculation
print("Ground shipping Standard",cost_ground)
cost_ground_premium = 125.00
print("Ground shipping Premium $",cost_ground_premium)
#Drone Shipping
if weight <= 2:
  cost_ground = weight * 4.50 + 0
elif weight <= 6:
  cost_ground = weight * 9.00 + 0
elif weight <= 10:
  cost_ground = weight * 12.00 + 0
elif weight <= 10:
  cost_ground= weight * 14.25 + 0
else: 
  answer = "Error"
print("Drone Shipping $", cost_ground)

