import math
from datetime import datetime, time

def EOQ(demand, mean, STD, C, Ce, Cs, Ct):
  Qs=math.sqrt(2*Ct*demand/Ce)
  Ts=Qs/demand
  Ns=1/Ts
  TRC=Ct*(demand/Qs)+Ce*(Qs/2)
  TC=C*demand+TRC

  return TC

  #print("Qs: " + str(Qs))
  #print("Ts: " + str(Ts))
  #print("Ns: " + str(Ns))
  #print("TRC: " + str(TRC))
  #print("TC: " + str(TC))

def POM(TotalOrders, ErrorOrders):
  #Perfect Order Measurement; the percentage of orders that are error-free.

  r=round(((TotalOrders-ErrorOrders)/TotalOrders),4)
  return r
  #print("Perfect Order Measurement: " + str(r))

def FR(TotalItems, ShippedItems):
  #Fill Rate
  #The percentage of a customer’s order that is filled on the first shipment. This can be represented as the percentage of items, SKUs or order value that is included with the first shipment.
  r=round((1-((TotalItems-ShippedItems)/TotalItems)),4)
  return r
  #print("Fill Rate: " + str(r))

def IDS(InventoryOnHand,AvgDailyUsage):
  #Inventory Days of Supply
  #The number of days it would take to run out of supply if it was not replenished.
  r=round(InventoryOnHand/AvgDailyUsage,4)
  return r
  #print("Inventory Days of Supply: " + str(r))

def FCU(TotalFreightCost,NumberOfItems):
  #Freight cost per unit
  #Usually measured as the cost of freight per item or SKU.
  r=round(TotalFreightCost/NumberOfItems,4)
  return r
  #print("Freight cost per unit: " + str(r))

def IT(COGS,AvgInventory):
  #Inventory Turnover
  #The number of times that a company’s inventory cycles per year.
  r=round(COGS/AvgInventory,4)
  return r
  #print("Inventory Turnover: " + str(r))

def DOS(AvgInventory,MonthlyDemand):
  #Days of Supply (DOS)
  #DOS is the most common KPI used by managers in measuring the efficiency in supply chain.
  r=round(AvgInventory/MonthlyDemand,4)*30
  return r
  #print("Days of Supply (DOS): " + str(r))

def GMROI(GrossProfit, OpeningStock, ClosingStock):
  #Gross Margin Return on Investment (GMROI)
  #GMROI represents the amount of gross profit earned for every AED (or $, £, €, ₺) of the average investment made in inventory.
  r=round(GrossProfit/((OpeningStock-ClosingStock)/2),4)*100
  return r
  #print("Gross Margin Return on Investment (GMROI): " + str(r))

def IA(ItemCounts, TotalItemCounts):
  #Inventory Accuracy
  #Inventory accuracy is used to calculate the accuracy of your inventory.
  r=round((ItemCounts/TotalItemCounts),4)
  return r
  #print("Inventory Accuracy: " + str(r))
  
def SUR(InventoryCube, TotalWarehouseCube):
  #Storage Utilization Rate
  #Storage utilization rate reflects how efficiently you are utilizing the amount of available space in your warehouse or distribution center.
  r=round((InventoryCube/TotalWarehouseCube),4)*100
  return r
  #print("Storage Utilization Rate: " + str(r))
  
def TOCT(TimeOrderReceivedbyCustomer, TimeOrderPlaced,TotalNumberofOrdersShipped):
  #Total Order Cycle Time
  #Total order cycle time reflects the average length of time that passes between a customer placing an order and the order being shipped.
  date1 = datetime.strptime(TimeOrderPlaced, '%Y-%m-%d')
  date2 = datetime.strptime(TimeOrderReceivedbyCustomer, '%Y-%m-%d')
  timedelta = date2 - date1
  r=round(timedelta.days/TotalNumberofOrdersShipped,4)
  return r
  #print("Total Order Cycle Time: " + str(r))
  
def IOCT(TimeOrderShipped, TimeOrderReceived, NumberofOrdersShipped):
  #Date format: %Y-%m-%d; "2015-01-05"
  #Internal Order Cycle Time
  #Internal order cycle time reflects the average amount of time that it takes from the moment that a customer order is released into the warehouse for processing and the moment that the order is shipped.
  date1 = datetime.strptime(TimeOrderShipped, '%Y-%m-%d')
  date2 = datetime.strptime(TimeOrderReceived, '%Y-%m-%d')
  timedelta = date2 - date1
  r=round(timedelta.days/NumberofOrdersShipped,4)
  return r
  #print("Internal Order Cycle Time: " + str(r))
