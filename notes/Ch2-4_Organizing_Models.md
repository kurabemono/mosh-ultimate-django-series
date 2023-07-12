# Naive Approach

The following organization is too modularized. We will not implement a "Cart" functionality without "Products" to buy or "Orders" to place.

## Products

Product

Collection

Tag

## Customers

Customer

## Carts

Cart

CartItem

## Orders

Order

OrderItem

# Better Approach

Self contained, zero coupling

# Store

Product

Collection

Customer

Cart

CartItem

Order

OrderItem

# Tags

Tag

TaggedItem
