
"""
regularExpressionConcept.py

A small, self-contained demonstration project for Python regular expressions.

Shows basic patterns and common operations: match, search, findall, fullmatch,
compiling patterns, and simple validators for email and phone numbers.

Run as a script to see example outputs.
"""

import re
from typing import List


def show_examples() -> None:
	examples = [
		(r"\d", "Any digit"),
		(r"[a-z]", "Any lowercase letter"),
		(r"^hello", "Starts with 'hello'"),
		(r"world$", "Ends with 'world'"),
		(r"\w+@\w+\.\w+", "Simple email-like pattern"),
	]
	print("Basic regex patterns and meanings:")
	for pat, desc in examples:
		print(f"  {pat:15} - {desc}")


def demo_search_operations(text: str) -> None:
	print(f"\nDemo text: {text!r}")
	pat = re.compile(r"\b\w+@\w+\.\w+\b")
	print("Using search to find first email-like substring:")
	m = pat.search(text)
	print("  Found:", m.group(0) if m else "None")

	print("Using findall to get all words with only letters:")
	words = re.findall(r"\b[a-zA-Z]+\b", text)
	print("  Words:", words)


def find_digits(text: str) -> List[str]:
	return re.findall(r"\d+", text)


def is_valid_email(addr: str) -> bool:
	# Simple validator (not RFC compliant) to illustrate fullmatch usage
	pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
	return bool(pattern.fullmatch(addr))


def is_valid_us_phone(number: str) -> bool:
	# Accept formats like 123-456-7890, (123) 456-7890, 1234567890
	pattern = re.compile(r"^(?:\(\d{3}\)\s?|\d{3}[- ]?)\d{3}[- ]?\d{4}$")
	return bool(pattern.fullmatch(number))


def main() -> None:
	show_examples()

	sample = "Contact us at help@example.com or sales@domain.org. Call 123-456-7890." 
	demo_search_operations(sample)

	print("\nDigits found:", find_digits(sample))

	tests = [
		"user@example.com",
		"bad-email@.com",
		"(555) 123-4567",
		"5551234567",
		"123-45-6789",
	]
	print("\nValidation examples:")
	for t in tests:
		print(f"  {t:20} email_valid={is_valid_email(t):5}  us_phone={is_valid_us_phone(t):5}")


if __name__ == "__main__":
	main()
