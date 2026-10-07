n = int(input("No. of cards = "))
cards = map(int,input("Enter cards : ").split())
expected = (n*(n+1))/2
actual = sum(cards)
m = expected - actual
print(f"Missing card is {m}")