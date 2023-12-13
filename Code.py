import streamlit as st

def find_largest_number(n1, n2, n3):
  return max(n1,n2,n3)

def main():
  st.title("Find the Largest Number")

  n1 = st.number_input("Enter the First Number:")
  n2 = st.number_input("Enter the Second Number:")
  n3 = st.number_input("Enter the Third Number:")

  if st.button("Find Largest Number"):
    largest = find_largest_number(n1, n2, n3)
    st.success(f'The Largest number is: {largest}')

if _name_ == "_main_":
  main()
