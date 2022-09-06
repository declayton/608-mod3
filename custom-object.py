# Deanna Clayton mod3 File4
## Create a Purchase object
class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0
    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

## Deanna Clayton, Give an amount to the purchase object
## Set the tax and tip percentages
purchase = Purchase(100.0)
taxPercent = 7.5
tipPercent = 20.0

## Deanna Clayton, Calculate the tax and tip, and display the findings
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

## Deanna Clayton, Display findings
print('Tax: ', tax)
print('Tip: ', tip)
print('Total: ', purchase.calculateTotal(taxPercent, tipPercent))
